# 1. Import Flask and os
import os
from flask import Flask

# 2. Create new instance of Flask, or a Flask app
app = Flask(__name__)

# 3. Create test function with the default route which will display some text as a proof of concept
@app.route('/')
def hello():
    return("Hello World... again!")

# 4. Set up our IP address and port number so Cloud9 knows how and where to run app
if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),
            debug=True)