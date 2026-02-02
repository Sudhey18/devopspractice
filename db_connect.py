import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",   # put your real MySQL password
        database="test_db"
    )

    if conn.is_connected():
        print("✅ Connected to MySQL database!")

        cursor = conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS employees(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       name VARCHAR(100),
                       Salary FLOAT
        )
            """)
        
        employees = [
            ("Sudharshan", 25000),
            ("Sagar", 30000),
            ("Harsha", 25000) 
        ]
        cursor.executemany(
            "INSERT INTO employees (name,Salary) VALUES (%s, %s)",
            employees
        )
        conn.commit()
        print("Employee records are inserted sucessfully")

except mysql.connector.Error as err:
    print("❌ Error:", err)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔒 Connection closed")
