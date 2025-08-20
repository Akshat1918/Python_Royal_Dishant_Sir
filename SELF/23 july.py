import mysql.connector

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="emp"
    )
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            department VARCHAR(50)
        )
    """)

    # Optional: Clear old data (uncomment if needed)
    # cursor.execute("DELETE FROM employees")

    # Insert data (auto id will be generated)
    cursor.execute("INSERT INTO employees (name, age, department) VALUES ('het', 20, 'HR')")
    cursor.execute("INSERT INTO employees (name, age, department) VALUES ('dharmi', 21, 'IT')")
    cursor.execute("INSERT INTO employees (name, age, department) VALUES ('yashvi', 22, 'admin')")
    cursor.execute("INSERT INTO employees (name, age, department) VALUES ('parva', 23, 'manager')")

    # Save inserted data
    conn.commit()
    print("Data inserted successfully.\n")

    # --- UPDATE operation ---
    # Update 'yashvi' age from 22 to 25
    cursor.execute("UPDATE employees SET age = 25 WHERE name = 'yashvi'")
    conn.commit()
    print("Data updated successfully.\n")

    cursor.execute("Delete from employees where name = 'parva'")
    conn.commit()
    print("Data deleted successfully.\n")

    cursor.execute("SELECT * FROM employees WHERE department = 'IT'")
    it_employees = cursor.fetchall()
    print("Employees in IT department:")
    for emp in it_employees:
        print(emp)
    print("\n")
    

    # Fetch and display all records
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    #rows = cursor.fetchmany(10)  # Fetch up to 10 records

    print("All records in 'employees' table:")
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # Close the connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
