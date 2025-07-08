from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'my-postgres-postgresql'),
        database=os.getenv('POSTGRES_DB', 'postgres'),
        user=os.getenv('POSTGRES_USER', 'postgres'),
        password=os.getenv('POSTGRES_PASSWORD', 'password')
    )
    return conn

@app.route('/api/data')
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT NOW()')  # простой запрос — текущая дата и время
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({'current_time': str(result[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)