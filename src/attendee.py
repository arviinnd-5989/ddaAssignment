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


# Get all attendees
def get_attendees():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM attendee')
        attendees = cur.fetchall()
        conn.close()
        return jsonify(attendees),200
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Create a new attendee
def create_attendee():
    try:
        attendee_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO attendee (attendeeID, attendeename, attendeeemail, attendeebirthdate) VALUES (%s, %s, %s, %s)',
            (attendee_data['attendeeID'], attendee_data['attendeeName'], attendee_data['attendeeEmail'], attendee_data['attendeeBirthdate'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message":"successful"}), 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Get a specific attendee by ID
def get_attendee(attendee_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM attendee WHERE attendeeid = %s', (attendee_id,))
        attendee = cur.fetchone()
        conn.close()
        if attendee is not None:
            return jsonify(attendee),200
        else:
            return 'attendee not found', 404
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Update an existing attendee by ID
def update_attendee(attendee_id):
    try:
        attendee_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            '''UPDATE attendee SET attendeeid = %s, attendeename = %s, attendeeemail = %s, attendeebirthdate= %s WHERE attendeeid = %s''',
            (attendee_data['attendeeID'],attendee_data['attendeeName'], attendee_data['attendeeEmail'], 
             attendee_data['attendeeBirthdate'], attendee_id)
        )

        conn.commit()
        conn.close()
        return 'attendee updated successfully', 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Delete an attendee by ID
def delete_attendee(attendee_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM attendee WHERE attendeeid = %s', (attendee_id,))

        conn.commit()
        conn.close()
        return 'attendee deleted successfully', 200
    except:
        return jsonify({"message":"unsuccessful"}), 400
