'''A module run that is used to call the app to run the webiste'''
from app.views import app
#method to call the app to run
if __name__ == '__main__':
    app.run(debug=True)
