import sqlite3
from flask import Flask, request, g, render_template, send_file

total_sensor = 30
app = Flask(__name__)

def db_connect():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

# in: sensor -> db
@app.route("/post_data", methods = ['POST'])
def post_data():
    conn = db_connect()
    cmd = 'update sensor set status=' + request.values.get('val') + ' where id=' + request.values.get('id')
    print('id=' + request.values.get('id'))
    print('val=' + request.values.get('val'))
    conn.execute(cmd)
    conn.commit()
    return 'done'

# in: lamp -> db
# out: lamp on/off
@app.route("/get_data_lamp", methods = ['GET'])
def get_data_lamp():
    conn = db_connect()
    target_lamp = request.values.get('id')
    target_sensor = 0
    for i in range(3):
        cmd = 'select * from sensor where id=' + str(int(target_lamp)*3+i)
        # print(cmd)
        data = conn.execute(cmd).fetchone()
        target_sensor += data['status']
    conn.close()
    return str(target_sensor)

# in: ipad -> db
# out: 
@app.route("/get_data_all", methods = ['GET'])
def get_data_all():
    conn = db_connect()
    cmd = 'select * from sensor'
    data = conn.execute(cmd).fetchall()
    conn.close()
    return str(data['status'])

@app.route("/ipad/<ipad_id>", methods = ['GET'])
def ipad(ipad_id):
    return render_template("/ipad.html", ipad_id=ipad_id)

@app.route("/img_status", methods = ['GET'])
def img_status():
    target_id = int(request.values.get('id'))
    target_status = -1
    conn = db_connect()
    cmd = 'select * from sensor where id=' + str(target_id)
    target_status = conn.execute(cmd).fetchone()['status']
    conn.close()
    return str(target_status)

@app.route("/img", methods = ['GET'])
def img():
    target_id = int(request.values.get('id'))
    return send_file("img/" + str(target_id) + ".png")

# for debug only
@app.route("/")
def hello():
    conn = db_connect()
    data = conn.execute('select * from sensor where id=2').fetchone()
    conn.close()
    return 'hello' + str(data['status'])