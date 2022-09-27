from flask import Flask, redirect,url_for,render_template,request
import sqlite3

app=Flask(__name__)
@app.route('/')
def home ():
    return render_template ('index.html')

@app.route('/demo',methods=["GET",'POST'])
def demo():
    if request.method=='POST':
        username=name=request.form['u_name']
        password=name=request.form['u_pass']
        conn =sqlite3.connect('project.db')
        query=f"INSERT INTO Workers (u_name,u_pass) VALUES ('{username}','{password}')" 
        conn.execute(query)
        conn.commit()
        
    return render_template ('demo.html')

@app.route('/delete/<id>')
def delete(id):
    conn = sqlite3.connect('project.db')
    query = f"delete from user where id = {id}"
    conn.execute(query)
    conn.commit()
    
    
@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    conn = sqlite3.connect('project.db')
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')  
        conn.execute("UPDATE user set username=?,usermail =? WHERE ID=?",[username, password,id])
        conn.commit()
        print('dogru')
    return render_template('update.html',x=id)


if __name__=='__main__':
    app.run(port=5000,debug=True)
    