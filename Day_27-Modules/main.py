# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo
MONGODB_URI = 'mongodb+srv://tester:30daysofpython@30daysofpython.r9b6xi4.mongodb.net/?appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)