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


# Get all venues
def get_venues():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM venue')
        venues = cur.fetchall()
        conn.close()
        return jsonify(venues),200
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Create a new venue
def create_venue():
    try:
        venue_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO venue (venueID, venuestate, venuecity, venuestreet, venuecapacity, venuename) VALUES (%s, %s, %s, %s, %s, %s)',
            (venue_data['venueID'], venue_data['venueState'], venue_data['venueCity'], venue_data['venueStreet'], venue_data['venueCapacity'], venue_data['venueName'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message":"successful"}), 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Get a specific venue by ID
def get_venue(venue_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM venue WHERE venueid = %s', (venue_id,))
        venue = cur.fetchone()
        conn.close()
        if venue is not None:
            return jsonify(venue),200
        else:
            return 'venue not found', 404
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Update an existing venue by ID
def update_venue(venue_id):
    try:
        venue_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            '''UPDATE venue SET venueid = %s, venuestate = %s, venuecity = %s, venuestreet= %s, venuecapacity = %s, venuename = %s WHERE venueid = %s''',
            (venue_data['venueID'],venue_data['venueState'], venue_data['venueCity'], venue_data['venueStreet'], 
             venue_data['venueCapacity'],venue_data['venueName'], venue_id)
        )

        conn.commit()
        conn.close()
        return 'venue updated successfully', 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Delete an venue by ID
def delete_venue(venue_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM venue WHERE venueid = %s', (venue_id,))

        conn.commit()
        conn.close()
        return 'venue deleted successfully', 200
    except:
        return jsonify({"message":"unsuccessful"}), 400
