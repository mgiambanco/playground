from flask import Flask, jsonify 
from db import configDB

class Cheetah:
    def __init__(app):
                
        @app.route('/pages', methods=['GET'])
        def getPages():
            conn = configDB.connect()
            out = []
            try:
                with conn.cursor() as cur:
                    cur.execute("select * from cheetah_endpoints")
                    row = cur.fetchone()

                    while row is not None:
                        out.append(row)
                        row = cur.fetchone()

            except (Exception, conn.DatabaseError) as error:
                    print(error)

            return jsonify(out)