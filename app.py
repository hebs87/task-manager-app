# 1. Import Flask and os
import os
# 9. Import render_template, redirect, request and url_for libraries
from flask import Flask, render_template, redirect, request, url_for
# 5. Import PyMongo and ObjectId to talk to MongoDB, as MongoDB uses format of BSON
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# 2. Create new instance of Flask, or a Flask app
app = Flask(__name__)

#6. Add configuration to Flask app - add the MongoBD name and URL linking to database
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", 'mongodb://localhost')

# 7. Create instance of PyMongo and add app into it using constructor function
mongo = PyMongo(app)

# 8. Create function with decorator that includes a route to that function
@app.route('/')
# 10. We will use a string called get_tasks and assign the route to the function
# This is the default function that will be run when the app is run
@app.route('/get_tasks')
def get_tasks():
    # Redirect to existing tasks.html template and will return everything in our tasks collection
    # Create variables and pass that in to the render_template() method
    _tasks = mongo.db.tasks.find()
    task_list = [task for task in _tasks]
    return render_template("tasks.html", tasks=task_list)
# 11. Create new route decorator and add_task function
# Allows user to add a single task
@app.route('/add_task')
def add_task():
    # 12. Add categories from the database to the render_template() method
    # Create variables and pass that in to the method
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    return render_template("addtask.html", categories=category_list)
# 13. Create new route decorator to insert task when form is submitted
@app.route('/insert_task', methods=["POST"])
def insert_task():
    # 14. Add function to insert tasks to databases
    # Variables to store the task collection
    tasks = mongo.db.tasks
    # Insert the form request to the DB as a dictionary
    tasks.insert_one(request.form.to_dict())
    # Once submitted, redirect the user to the tasks.html file
    return redirect(url_for('get_tasks'))
# 15. Once we've created DONE and EDIT buttons, we wire them up, starting with EDIT button
# Create app.route to edit_task() function, and we want to edit our taks_id
@app.route('/edit_task/<task_id>')
# 16. We want to retrieve the task from the DB and display the task on an editable form
def edit_task(task_id):
    # We want to find a particular task by its _id and redirect the user to the edittask.html template
    # _id is the key in the DB, and the ObjectId is the task_id that's passed into the function
    _task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    # We need a list of the collections, as we want to present the categories on the edit form
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    # All the data will be prepopulated rather that blank fields in our edit template
    return render_template("edittask.html", task=_task, categories=category_list)
# 17. After we've displayed the data in the edittask.html, we want to update the taks when 'EDIT TASK' btn clicked
# Create app.route to update_task() function, and we want to update our taks_id
@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    # We call the tasks DB and store it in variable
    tasks = mongo.db.tasks
    # Then we call the update method
    tasks.update( {'_id': ObjectId(task_id)},
    {
        'task_name': request.form.get('task_name'),
        'category_name': request.form.get('category_name'),
        'task_description': request.form.get('task_description'),
        'due_date': request.form.get('due_date'),
        'is_urgent': request.form.get('is_urgent')
    })
    return redirect(url_for('get_tasks'))
# 18. We want to delete a task when the user clicks the 'DONE' button
@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    tasks = mongo.db.tasks
    tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('get_tasks'))
# 19. After creating categories.html, we create a get_categories route decorator
@app.route('/get_categories')
def get_categories():
    # Will return everything in our categories collection
    # we can return results directly in our return call rather than storing in variables
    return render_template("categories.html",
    categories=mongo.db.categories.find())


''' 3. Create test function with the default route which will display some text as a proof of concept
DELETE THIS WHEN COMPLETING STEP 8
@app.route('/')
def hello():
    return("Hello World... again!")
'''

# 4. Set up our IP address and port number so Cloud9 knows how and where to run app
if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),
            debug=True)