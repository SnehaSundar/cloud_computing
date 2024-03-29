from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from sqlalchemy import create_engine
from flask import jsonify
engine = create_engine("mysql+pymysql://admin:cloud123@database-1.cuujcmal7p0q.ap-south-1.rds.amazonaws.com:3306/Database1")



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://admin:cloud123@database-1.cuujcmal7p0q.ap-south-1.rds.amazonaws.com:3306/Database1'
#'sqlite:///transactions.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, autoincrement=True)
    recepient = db.Column(db.String(50),default="ohio" ,nullable = False)
    amount = db.Column(db.Integer, default = 0,  autoincrement=True)

    def __repr__(self):
        return 'payment successful'
    
def __init__(self,recepient,amount):
    self.recepient = recepient
    self.amount = amount

@app.route('/')
def index():
     return render_template("login.html")
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST'  and request.form["password "] == "admin":  
        return redirect(url_for("/add"))  
    return redirect(url_for("login"))

    

@app.route('/add', methods=['POST','GET'])
def add_transaction():
    return render_template('add.html')

@app.route('/to_database', methods = ["POST"])  
def to_database():  
    if request.method == "POST":
        temp = Todo(recepient=request.form['recepient'],amount=request.form['amount'])
        try:
            db.session.add(temp)
            db.session.commit()
            return redirect(url_for("success"))
        except:
            return "DB ERROR"
    else:
        return "TYPE METHOD ERROR"

@app.route('/all')
def success():
     connection = db.engine.raw_connection()
     cur = connection.cursor()
     cur.execute("SELECT * FROM todo")
     data = cur.fetchall()
     return jsonify(data)

import logging
logging.basicConfig(filename='backup.log',level=logging.DEBUG)

import socket
ip_addr = socket.gethostbyname(socket.gethostname())
if __name__ == "__main__":
    app.run(host=ip_addr, port=80)

