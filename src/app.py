from flask import Flask 
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'empleados'

mysql.init_app(app)

@app.route('/')
def Index():
    sql = "Insert into empleados (nombre, correo, foto) values ('eli', 'eli@gmail.com', 'eli.jpg');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    
    conn.commit()
    return render_template['empleados/index.html']

if __name__ == "__main__":
    app.run(debug=True)

