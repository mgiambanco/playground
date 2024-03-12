from flask import Flask,jsonify,request 
from db import configDB

class Users:
    def __init__(app):
                
        @app.route('/users', methods=['GET'])
        def getUsers():
            return jsonify({
                "users": [
                    {"name": "Mario"},
                    {"name": "Sarah"},
                ]
            })
        
        @app.route('/blog/<postID>') 
        def show_blog(postID): 
            return 'Blog Number %d' % postID 
        
        @app.route('/rev/<revNo>') 
        def revision(revNo): 
            return 'Revision Number %f' % revNo 
