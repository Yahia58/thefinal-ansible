from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='172.31.35.109',  # Replace with your DB server IP
        user='app_user',
        password='MySQL_DB_Password',  # Use your vault variable here
        database='app_db'
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT column1, column2 FROM your_table')  # Replace with your actual table name
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(host='172.31.35.109', port=5000)  # Debug mode for local development

