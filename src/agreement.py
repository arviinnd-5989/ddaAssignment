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


# Get all agreements
def get_agreements():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM agreement')
        agreements = cur.fetchall()
        conn.close()
        return jsonify(agreements),200
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Create a new agreement
def create_agreement():
    try:
        agreement_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO agreement (vendorid, organizerid, contractdate, contractamount) VALUES (%s, %s, %s, %s)',
            (agreement_data['vendorID'], agreement_data['organizerID'], agreement_data['contractDate'], agreement_data['contractAmount'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message":"successful"}), 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Get a specific agreement by ID
def get_agreement(vendor_id, organizer_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM agreement WHERE vendorid = %s AND organizerid = %s', (vendor_id,organizer_id,))
        agreement = cur.fetchone()
        conn.close()
        if agreement is not None:
            return jsonify(agreement),200
        else:
            return 'agreement not found', 404
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Update an existing agreement by ID
def update_agreement(vendor_id, organizer_id):
    try:
        agreement_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            '''UPDATE agreement SET vendorid = %s, organizerid = %s, contractdate = %s, contractamount= %s WHERE vendorid = %s AND organizerid = %s''',
            (agreement_data['vendorID'],agreement_data['organizerID'], agreement_data['contractDate'], 
             agreement_data['contractAmount'], vendor_id, organizer_id)
        )

        conn.commit()
        conn.close()
        return 'agreement updated successfully', 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Delete an agreement by ID
def delete_agreement(vendor_id, organizer_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM agreement WHERE vendorid = %s AND organizerid = %s', (vendor_id, organizer_id,))

        conn.commit()
        conn.close()
        return 'agreement deleted successfully', 200
    except:
        return jsonify({"message":"unsuccessful"}), 400
