'''A module to make Python treat the directories as containing packages'''
#importing Flask
from flask import Flask
#Initialise the app
app = Flask(__name__, instance_relative_config=True)
#Load the views
from app import app
#Load the config files
app.config.from_object("config")