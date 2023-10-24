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


# Get all vendors
def get_vendors():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM vendor')
        vendors = cur.fetchall()
        conn.close()
        return jsonify(vendors),200
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Create a new vendor
def create_vendor():
    try:
        vendor_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO vendor (vendorID, vendorname, vendorphone, vendoremail) VALUES (%s, %s, %s, %s)',
            (vendor_data['vendorID'], vendor_data['vendorName'], vendor_data['vendorPhone'], vendor_data['vendorEmail'])
        )
        conn.commit()
        conn.close()
        return jsonify({"message":"successful"}), 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Get a specific vendor by ID
def get_vendor(vendor_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM vendor WHERE vendorid = %s', (vendor_id,))
        vendor = cur.fetchone()
        conn.close()
        if vendor is not None:
            return jsonify(vendor),200
        else:
            return 'vendor not found', 404
    except:
        return jsonify({"message":"unsuccessful"}), 400

# Update an existing vendor by ID
def update_vendor(vendor_id):
    try:
        vendor_data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            '''UPDATE vendor SET vendorid = %s, vendorname = %s, vendorphone = %s, vendoremail= %s WHERE vendorid = %s''',
            (vendor_data['vendorID'],vendor_data['vendorName'], vendor_data['vendorPhone'], 
             vendor_data['vendorEmail'], vendor_id)
        )

        conn.commit()
        conn.close()
        return 'vendor updated successfully', 200
    except:
        print(traceback.print_exc())
        return jsonify({"message":"unsuccessful"}), 400

# Delete an vendor by ID
def delete_vendor(vendor_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM vendor WHERE vendorid = %s', (vendor_id,))

        conn.commit()
        conn.close()
        return 'vendor deleted successfully', 200
    except:
        return jsonify({"message":"unsuccessful"}), 400
