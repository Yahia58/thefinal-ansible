from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection():
    """ Create a database connection to the MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='db',  # Use the service name of your database server
            user='app_user',  # Use the created application user
            password='MySQL_DB_Password',  # Use the variable if stored securely
            database='app_db'  # The name of the database created
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

@app.route('/')
def home():
    return "Welcome to My Application!"

@app.route('/data')
def data():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM your_table_name")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

