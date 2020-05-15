import json
import sqlite3
from flask import Flask, request, g
from .utils import json_response, JSON_MIME_TYPE
import ast
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['DATABASE_NAME'])

@app.route('/delete_data',methods=['DELETE'])
def delete_data():
    d = request.json
    # print(d)
    mdata = request.data
    # mydata = mdata.decode('utf8')
    s = json.loads(mdata)
    da = json.dumps(s)
    remove_lef = da.replace('[', '')
    remove_right = remove_lef.replace(']', '')
    data = ast.literal_eval(remove_right)
    # print(data)
    id = data['HomeId']
    cursor =g.db.execute("SELECT * FROM sensor_data WHERE HomeId=?;",(id,))
    # Check if book exists
    if cursor.fetchone()[0] == 0:
        # Doesn't exist. Return 404.
        from flask_restful import abort
        abort(404)

    # Delete it

    g.db.execute("DELETE FROM sensor_data WHERE HomeId=?;",(id,))
    #delete_query = 'DELETE FROM book WHERE book.id = :id'
    g.db.commit()

    return json_response(status=204)


@app.errorhandler(404)
def not_found(e):
    return '', 404
