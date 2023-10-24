#!/bin/bash

# MySQL server connection details
DB_USER="your_username"
DB_PASSWORD="your_password"
DB_HOST="localhost"

# Name of the current database
DB_NAME="$1"

# Define the SQL query to create the table
SQL_QUERY="CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));"

# Run the MySQL command to create the table
mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME -e "$SQL_QUERY"
