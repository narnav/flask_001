from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3
con = sqlite3.connect("garage.db",check_same_thread=False)
cur = con.cursor()

try:
    cur.execute("CREATE TABLE users(pwd, user)")
except:
    print("table already exist")

# display index/form page (1)
@app.route('/',methods=['post','get'])
def hello():
    # add - post
    if request.method == 'POST':
        pwd = request.form['pwd']
        user = request.form['user']
        if len( user )>3:
            cur.execute(f"INSERT INTO users VALUES('{pwd}', '{user}')")
            con.commit()
    

    # read all users from db 
    res = cur.execute("SELECT rowid, * FROM users").fetchall()
    return render_template('index.html',data=res)


@app.route('/del/<int:id>',methods=['delete'])
def del_user(id):
    print("delete" , id)
    sql =f"delete from users where rowid = {id}"
    cur.execute(sql)
    con.commit()
    # print(sql)
    return "deleteeeeeeeeeeeeeeee"

@app.route('/upd/<int:id>',methods=['put'])
def upd_user(id):
    # print("update" , id)
    data = request.json
    user = data.get('user')
    pwd = data.get('pwd')
    print(user,pwd,id)
    sql =f"UPDATE users SET user = '{user}', pwd='{pwd}' WHERE  rowid = {id}"
    cur.execute(sql)
    con.commit()
    print(sql)
    return "updateeee"

if __name__ == '__main__':
    app.run(debug=True)
 