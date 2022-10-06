from flask import redirect, request,url_for, render_template
from ran import app 


@app.route('/contact', methods=['GET', 'POST'] )
def contact():
    from models import Messages,db
    if request.method=="POST":
        name=request.form['u_name']
        email=request.form['u_email']
        message=request.form['u_message']
        msj=Messages(name=name,email=email,message=message)
        db.session.add(msj)
        db.session.commit()
        return redirect('/messages')     
    return render_template('contact_form.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    from models import Messages, db
    messages=Messages.query.all()
    return render_template('/messages.html', messages=messages)
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
    if request.method==['GET','POST']:
        name=request.form['u_name']
        email=request.form['u_email']
        message=request.form['u_message']
        mesaj=Messages.query.get(id)
        mesaj.name=name
        mesaj.email=email
        mesaj.mesage=message
        db.session.update(msj)
        db.session.commit()
        return redirect ('/contact')
    return render_template('update.html',x=id)