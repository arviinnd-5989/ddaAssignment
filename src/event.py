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


# Get all events
def get_events():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM event')
        events = cur.fetchall()
        conn.close()
        return jsonify(events),200
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Create a new event
def create_event():
    try:
        event_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO event (eventID, organizerID, eventName, eventDate, eventDescription, venueID) VALUES (%s, %s, %s, %s, %s, %s)',
            (event_data['eventID'], event_data['organizerID'], event_data['eventName'], event_data['eventDate'], event_data['eventDescription'],event_data['venueID'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message":"successful"}), 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Get a specific event by ID
def get_event(event_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM event WHERE eventid = %s', (event_id,))
        event = cur.fetchone()
        conn.close()
        if event is not None:
            return jsonify(event),200
        else:
            return 'Event not found', 404
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Update an existing event by ID
def update_event(event_id):
    try:
        event_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            '''UPDATE event SET eventid = %s, organizerid = %s, eventname = %s, eventdate= %s, 
            eventdescription = %s, venueid = %s WHERE eventid = %s''',
            (event_data['eventID'], event_data['organizerID'], event_data['eventName'], 
             event_data['eventDate'],event_data['eventDescription'],event_data['venueID'],event_id)
        )

        conn.commit()
        conn.close()
        return 'Event updated successfully', 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Delete an event by ID
def delete_event(event_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM event WHERE eventid = %s', (event_id,))

        conn.commit()
        conn.close()
        return 'Event deleted successfully', 200
    except:
        return jsonify({"message":"unsuccessful"}), 400
