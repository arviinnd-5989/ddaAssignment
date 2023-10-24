from flask import Flask, request, jsonify
import psycopg2
import traceback

# Define your PostgreSQL database connection parameters
db_config = {
    'dbname': 'eventmanagement',
    'user': 'indone',
    'password': 'Indone',
    'host': 'localhost'
}

# Function to establish a database connection
def get_db_connection():
    return psycopg2.connect(**db_config)


# Get all attendedbys
def get_attendedbys():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM attendedby')
        attendedbys = cur.fetchall()
        conn.close()
        return jsonify(attendedbys),200
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Create a new attendedby
def create_attendedby():
    try:
        attendedby_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO attendedby (eventID, attendeeID) VALUES (%s, %s)',
            (attendedby_data['eventID'], attendedby_data['attendeeID'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message":"successful"}), 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Get a specific attendedby by ID
def get_attendedby(event_id, attendee_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM attendedby WHERE eventid = %s and attendeeid = %s', (event_id,attendee_id))
        attendedby = cur.fetchone()
        conn.close()
        if attendedby is not None:
            return jsonify(attendedby),200
        else:
            return 'attendedby not found', 404
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Update an existing attendedby by ID
def update_attendedby(event_id, attendee_id):
    try:
        attendedby_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            '''UPDATE attendedby SET eventid= %s, attendeeid = %s WHERE eventid = %s and attendeeid = %s''',
            (attendedby_data['eventID'],attendedby_data['attendeeID'],event_id, attendee_id)
        )

        conn.commit()
        conn.close()
        return 'attendedby updated successfully', 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Delete an attendedby by ID
def delete_attendedby(event_id, attendee_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM attendedby WHERE eventid = %s and attendeeid = %s', (event_id,attendee_id))

        conn.commit()
        conn.close()
        return 'attendedby deleted successfully', 200
    except:
        return jsonify({"message":"unsuccessful"}), 400
