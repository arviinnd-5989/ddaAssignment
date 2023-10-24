from flask import Flask, request, jsonify
import psycopg2
import traceback

# Define your PostgreSQL database connection parameters
db_config = {
    'dbname': 'eventmanagement',
    'user': 'indone',
    'password': 'Indone',
    'host': 'localhost',
}

# Function to establish a database connection
def get_db_connection():
    return psycopg2.connect(**db_config)


# Get all organizers
def get_organizers():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM organizer')
        organizers = cur.fetchall()
        conn.close()
        return jsonify(organizers),200
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Create a new organizer
def create_organizer():
    try:
        organizer_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO organizer (organizerID, organizername, organizerphone, organizeremail) VALUES (%s, %s, %s, %s)',
            (organizer_data['organizerID'], organizer_data['organizerName'], organizer_data['organizerPhone'], organizer_data['organizerEmail'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message":"successful"}), 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Get a specific organizer by ID
def get_organizer(organizer_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM organizer WHERE organizerid = %s', (organizer_id,))
        organizer = cur.fetchone()
        conn.close()
        if organizer is not None:
            return jsonify(organizer),200
        else:
            return 'Organizer not found', 404
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Update an existing organizer by ID
def update_organizer(organizer_id):
    try:
        organizer_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            '''UPDATE organizer SET organizerid = %s, organizername = %s, organizerphone = %s, organizeremail= %s WHERE organizerid = %s''',
            (organizer_data['organizerID'],organizer_data['organizerName'], organizer_data['organizerPhone'], 
             organizer_data['organizerEmail'], organizer_id)
        )

        conn.commit()
        conn.close()
        return 'Organizer updated successfully', 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Delete an organizer by ID
def delete_organizer(organizer_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM organizer WHERE organizerid = %s', (organizer_id,))

        conn.commit()
        conn.close()
        return 'Organizer deleted successfully', 200
    except:
        return jsonify({"message":"unsuccessful"}), 400
