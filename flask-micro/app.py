from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'Abhishekk'}

class Home(Resource):
    def get(self):
        return {'Abhishek': 'Restfull API'}

api.add_resource(HelloWorld, '/')
api.add_resource(Home, '/home')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  
