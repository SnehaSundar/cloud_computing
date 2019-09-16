from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://admin:cloud123@database-1.cbmjucn2aqjr.ap-south-1.rds.amazonaws.com:3306/Database1'
#'sqlite:///transactions.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, autoincrement=True)
    recepient = db.Column(db.String(50),default="ohio" ,nullable = False)
    amount = db.Column(db.Integer, default = 0,  autoincrement=True)

    def __repr__(self):
        return 'payment successful'
    
 
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
        task_recepient = request.form["recepient"]
        add_recepient = Todo(recepient = task_recepient)
        task_amount = request.form["amount"]
        add_amount = Todo(amount = task_amount)
        try:
            db.session.add(add_recepient)
            db.session.add(add_amount)

            db.session.commit()
            return redirect(url_for("success"))
        except:
            return "DB ERROR"
    else:
        return "TYPE METHOD ERROR"

@app.route('/success')
def success():
    return render_template('success.html')
    
if __name__ == "__main__":
    app.run(host='10.0.1.17', port=80)

