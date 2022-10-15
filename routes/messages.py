from flask import redirect, request,url_for, render_template
from ran import app 
import datetime



@app.route('/contact', methods=['GET', 'POST'] )
def contact():
    from models import Messages,db
    if request.method=="POST":
        name=request.form['u_name']
        email=request.form['u_email']
        message=request.form['u_message']
        msj=Messages(name=name,email=email,message=message, m_date=str(datatime.datatime.now()))
        db.session.add(msj)
        db.session.commit()
        return redirect('/messages')     
    return render_template('contact_form.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    from models import Messages,User,db
    user=User.query.get(1)
    if user.is_logged_in==True:
        message= Messages.query.all()
        return render_template('messages.html',message=message)
    else:
        return redirect('/login')

#delete fuksiyasi elave olundu
@app.route('/delete/<id>',methods=['GET','POST'] )
def delete(id):
    from models import Messages, db
    mesaj=Messages.query.get(id)
    db.session.delete(mesaj)
    db.session.commit()
    return redirect ('/messages')



@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    from models import Messages, db
    message=Messages.query.get(id)
    if request.method=="POST":
        message.name=request.form['u_name']
        message.email=request.form['u_email']
        message.message=request.form['u_message']
        db.session.commit()
        return redirect ('/messages')
    return render_template('update.html',message=message)

@app.route('/login',methods=['GET','POST'])
def login():
    from models import Messages,User,db
    user=User.query.get(1)
    if request.method=="POST":
        if request.form['u_email']==user.email and request.form['u_password']==user.password:
            user.is_logged_in=True
            db.session.commit()
            return redirect ('/messages')
        else:
            return redirect ('/login')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    from models import Messages,User,db
    user=User.query.get(1)
    user.is_logged_in=False
    db.session.commit()
    return redirect('/login')