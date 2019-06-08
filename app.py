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
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

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