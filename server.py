import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(name)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return "Bot is Up & Running!"

api.add_resource(Greeting, '/')
app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
