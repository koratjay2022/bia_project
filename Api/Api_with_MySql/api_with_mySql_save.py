from flask import Flask, jsonify, request
import mysql.connector


app = Flask(__name__)

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Koratj@y54321',
        database='api_with_mysql'  # The database we will create
    )

# @app.route('/create_table', methods=['GET'])
# def create_table():
#     try:
#         conn = connect_to_db()
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS users (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(50),
#                 age INT
#             )
#         """)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return jsonify({"message": "Table 'users' created successfully!"})
#     except Exception as e:
#         return jsonify({"error": str(e)})
    
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

@app.route('/')
def hello_world():
    return 'Hello world'

def insert_row(name, age):
    try:
        conn = connect_to_db()
        if isinstance(conn, str):
            return jsonify({"error": conn})
        cursor = conn.cursor()
        query = "INSERT INTO users (name, age) VALUES (%s, %s)"
        cursor.execute(query, (name, age))
        conn.commit()
        # cursor.close()
        # conn.close()
        return jsonify({"message": "Row inserted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/insert_row', methods=['POST'])
def insert_row_route():
    name = request.form.get('name')
    age = request.form.get('age')
    if not name or not age:
        return jsonify({"error": "Missing 'name' or 'age'"}), 400

    try:
        age = int(age)
    except ValueError:
        return jsonify({"error": "'age' must be an integer"}), 400

    return insert_row(name, age)

@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        if isinstance(conn, str):
            return jsonify({"error": conn})
        
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        
        cursor.close()
        conn.close()

        result = [{"id": row[0], "name": row[1], "age": row[2]} for row in rows]

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
