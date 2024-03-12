from flask import Flask
from users import Users
from cheetah import Cheetah

class Main:
    
    def __main__():
        
        # instance of flask application
        app = Flask(__name__)
        
        Users.__init__(app)
        Cheetah.__init__(app)
                
        # home route that returns below text 
        # when root url is accessed
        @app.route("/")
        def hello_world():
            return "<p>Hello, World!</p>"
        
        if __name__ == '__main__':
            app.run(debug=True, port=8000)

Main.__main__()
