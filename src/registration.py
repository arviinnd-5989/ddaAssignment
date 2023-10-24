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


# Get all registrations
def get_registrations():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM registration')
        registrations = cur.fetchall()
        conn.close()
        return jsonify(registrations),200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Create a new registration
def create_registration():
    try:
        registration_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO registration (registrationID, registrationdate, attendeeid, eventid) VALUES (%s, %s, %s, %s)',
            (registration_data['registrationID'], registration_data['registrationDate'], registration_data['attendeeID'], registration_data['eventID'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message":"successful"}), 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Get a specific registration by ID
def get_registration(registration_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM registration WHERE registrationid = %s', (registration_id,))
        registration = cur.fetchone()
        conn.close()
        if registration is not None:
            return jsonify(registration),200
        else:
            return 'registration not found', 404
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Update an existing registration by ID
def update_registration(registration_id):
    try:
        registration_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            '''UPDATE registration SET registrationid = %s, registrationdate = %s, attendeeid = %s, eventid= %s WHERE registrationid = %s''',
            (registration_data['registrationID'],registration_data['registrationDate'], registration_data['attendeeID'], 
             registration_data['eventID'], registration_id)
        )

        conn.commit()
        conn.close()
        return 'registration updated successfully', 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Delete an registration by ID
def delete_registration(registration_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM registration WHERE registrationid = %s', (registration_id,))

        conn.commit()
        conn.close()
        return 'registration deleted successfully', 200
    except:
        return jsonify({"message":"unsuccessful"}), 400
