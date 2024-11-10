from flask import Flask, request, jsonify
import mysql.connector

application = Flask(__name__)  # Rename app to application

def get_db_connection():
    return mysql.connector.connect(
        host='192.254.234.135',
        user='sektuies_login',
        password='Undeadarmy1!',
        database='sektuies_loginform'
    )

@application.route('/purchase_orders', methods=['GET'])
def get_purchase_orders():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM `Purchase Orders` WHERE Date BETWEEN %s AND %s"
    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

if __name__ == '__main__':
    application.run(debug=True)
