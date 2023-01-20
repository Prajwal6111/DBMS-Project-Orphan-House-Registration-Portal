from flask import Flask, json,redirect,render_template,flash,request
from flask.globals import request, session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import login_required,logout_user,login_user,login_manager,LoginManager,current_user

from flask_mail import Mail
import json


# mydatabase connection
local_server=True
app=Flask(__name__)
app.secret_key="Prajwal"


with open('config.json','r') as c:
    prajwal=json.load(c)["prajwal"]



app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=prajwal['gmail-user'],
    MAIL_PASSWORD=prajwal['gmail-password']
)
mail = Mail(app)



# this is for getting the unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databsename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/orphan'
db=SQLAlchemy(app)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) or orphanhouseuser.query.get(int(user_id))


class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    orp=db.Column(db.String(20),unique=True)
    email=db.Column(db.String(50))
    dob=db.Column(db.String(1000))


class orphanhouseuser(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Ocode=db.Column(db.String(20))
    email=db.Column(db.String(50))
    password=db.Column(db.String(1000))

class regorp(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Oname=db.Column(db.String(20))
    age=db.Column(db.Integer)
    gender=db.Column(db.String(1))
    uaddress=db.Column(db.String(100))

class addorphanhouseuser(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Ocode=db.Column(db.String(20),unique=True)
    ohname=db.Column(db.String(50))
    ohdistrict=db.Column(db.String(50))
    ohstate=db.Column(db.String(50))
    ohpin=db.Column(db.Integer)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/admin',methods=['POST','GET'])
def admin():
 
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        if(username==prajwal['user'] and password==prajwal['password']):
            session['user']=username
            flash("login success","info")
            return render_template("addorphouse.html")
        else:
            flash("Invalid Credentials","danger")

    return render_template("admin.html")


@app.route('/usersignup',methods=['POST','GET'])
def signup():
    if request.method=="POST":
        orp=request.form.get('orp')
        email=request.form.get('email')
        dob=request.form.get('dob')
        # print(orpid,email,dob)
        encpassword=generate_password_hash(dob)
        user=User.query.filter_by(orp=orp).first()
        emailUser=User.query.filter_by(email=email).first()
        if user or emailUser:
            flash("Email or orpid is already taken","warning")
            return render_template("usersignup.html")
        db.engine.execute(f"INSERT INTO user (orp,email,dob) VALUES ('{orp}','{email}','{encpassword}') ")
                
        flash("SignUp Success Please Login","success")
        return render_template("userlogin.html")

    return render_template("usersignup.html")


@app.route('/userlogin',methods=['POST','GET'])
def login():
    if request.method=="POST":
        orp=request.form.get('orp')
        dob=request.form.get('dob')
        user=User.query.filter_by(orp=orp).first()
        if user and check_password_hash(user.dob,dob):
            login_user(user)
            flash("Login Success","info")
            return render_template("index.html")
        else:
            flash("Invalid Credentials","danger")
            return render_template("userlogin.html")


    return render_template("userlogin.html")

@app.route('/orplogin',methods=['POST','GET'])
def OrphanHouselogin():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=orphanhouseuser.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","info")
            return render_template("index.html")
        else:
            flash("Invalid Credentials","danger")
            return render_template("orplogin.html")


    return render_template("orplogin.html")

@app.route("/addorphanhouseinfo",methods=['POST','GET'])
def addorphanhouseinfo():
    email=current_user.email
    posts=orphanhouseuser.query.filter_by(email=email).first()
    code=posts.Ocode
    print(code)
    postsdata=addorphanhouseuser.query.filter_by(Ocode=code).first()

    if request.method=="POST":
        Ocode=request.form.get('Ocode')
        ohname=request.form.get('ohname')
        ohdistrict=request.form.get('ohdistrict')
        ohstate=request.form.get('ohstate')
        ohpin=request.form.get('ohpin')
        Ocode=Ocode.upper()
        huser=orphanhouseuser.query.filter_by(Ocode=Ocode).first()
        hduser=addorphanhouseuser.query.filter_by(Ocode=Ocode).first()
        if hduser:
            flash("Data is already Present you can update it..","primary")
            return render_template("addorphaninfo.html")
        if huser:            
            db.engine.execute(f"INSERT INTO addorphanhouseuser (Ocode,ohname,ohdistrict,ohstate,ohpin) VALUES ('{Ocode}','{ohname}','{ohdistrict}','{ohstate}','{ohpin}')")
            flash("Data Is Added","primary")
        else:
            flash("Orphan Code not Exist","warning")
    return render_template("addorphaninfo.html",postsdata=postsdata)



@app.route('/addOrphanUser',methods=['POST','GET'])
def OrphanUser():
   
    if('user' in session and session['user']==prajwal['user']):
      
        if request.method=="POST":
            Ocode=request.form.get('Ocode')
            email=request.form.get('email')
            password=request.form.get('password')        
            encpassword=generate_password_hash(password)  
            Ocode=Ocode.upper()     
            db.engine.execute(f"INSERT INTO orphanhouseuser (Ocode,email,password) VALUES ('{Ocode}','{email}','{encpassword}') ")
            mail.send_message('Orphan House Center',sender=prajwal['gmail-user'],recipients=[email],body=f"Welcome thanks for choosing us\nYour Login Credentials Are:\n Email Address: {email}\nPassword: {password}\n\nOrphan House Code {Ocode}\n\n Do not share your password\n\n\nThank You..." )
            flash("Data Sent and Inserted Successfully","warning")
            return render_template("addorphouse.html")
    else:
        flash("Login and try Again","warning")
        return render_template("addorphouse.html")
    
    return render_template("userlogin.html")

@app.route("/regorp",methods=['POST','GET'])
@login_required
def regorpd():
    query=db.engine.execute(f"SELECT *FROM addorphanhouseuser")
    if request.method=="POST":
        Ocode=request.form.get('Ocode')
        oname=request.form.get('oname')
        age=request.form.get('age')
        gender=request.form.get('gender').upper()
        uaddress=request.form.get('uaddress')
        check2=orphanhouseuser.query.filter_by(Ocode=Ocode).first()
        if not check2:
            flash("Orphan House Code Does Not Exists","warning")
            
        # code=Ocode
        # db.engine.execute(f"SELECT *FROM regorp WHERE regorp.Ocode='{code}' ")

        check=orphanhouseuser.query.filter_by(Ocode=Ocode).first()
        if(int(age)>0 and check):
            db.engine.execute(f"INSERT INTO regorp (oname,age,gender,uaddress) VALUES ('{oname}','{age}','{gender}','{uaddress}') ")
            flash("Your Orphan Has Booked Kindly Visit for further Procedure","success")
        else:
            flash("Something went Wrong!!","danger")
    return render_template("regorp.html",query=query)


# @app.route("/ordetails",methods=['POST','GET'])
# @login_required
# def ordetails():
#     data=regorp.query.filter_by(gender='M').first()
#     query=db.engine.execute("select count(*) from gender where table_name = 'tablename'")
#     return render_template("odetails.html",data=data)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))



# testing wheather db is connected or not  
@app.route("/test")
def test():
    try:
        a=Test.query.all()
        print(a)
        return f'MY DATABASE IS CONNECTED'
    except Exception as e:
        print(e)
        return f'MY DATABASE IS NOT CONNECTED {e}'

@app.route("/contact",methods=['POST','GET'])
def contact():
    return render_template("contact.html")

app.run(debug=True)