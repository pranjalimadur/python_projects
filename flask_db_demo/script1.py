from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/data_collector_height'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://dbmsippauaaqqn:41ef0ee58b6c218075f2564e8cf85f4ed76421fa597cdc00751d92c470bf0c6e@ec2-52-71-107-99.compute-1.amazonaws.com:5432/ddii3a10690q82?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data_height"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100), unique=True)
    height=db.Column(db.Integer)

    def __init__(self,email, height):
        self.email=email
        self.height=height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file=request.files["file"]
        file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename, "a") as f:
            f.write("This was added later!")
        #content=file.read()
        #print(content)
        #print(file)
        #print(type(file))
        #email=request.form["email_name"]
        #height=request.form["height_name"]
        #if db.session.query(Data).filter(Data.email==email).count()==0:
        #    data=Data(email,height)
        #    db.session.add(data)
        #    db.session.commit()
        #    avg_height=db.session.query(func.avg(Data.height)).scalar()
        #    avg_height=round(avg_height,1)
        #    count=db.session.query(Data.height).count()
        #    send_email(email, height,avg_height,count)
        return render_template("index.html", btn="download.html")
    #return render_template("index.html", text="This email already exists!")

@app.route("/download")
def download():
    return send_file("uploaded"+file.filename, attachment_filename="editedcereal.csv", as_attachment=True)

if __name__ == '__main__':
    app.debug=True
    app.run()
