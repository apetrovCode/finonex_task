from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL configurations (Make sure to parameterize these in production)
app.config['MYSQL_DATABASE_USER'] = 'db_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'db_password'
app.config['MYSQL_DATABASE_DB'] = 'customers'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def get_content():
    conn = mysql.connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM customer_list")
    names = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

