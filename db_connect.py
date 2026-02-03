import mysql.connector
import csv
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
        
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()

        with open("employees.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([col[0] for col in cursor.description])
            writer.writerows(rows)
        print("Employees.csv file created sucessfully")


        
        # name = input("\nEnter the employee name to search: ")
        # cursor.execute(
        #     "SELECT * FROM employees WHERE name = %s",
        #     (name,)
        # )
        # results = cursor.fetchall()

        # if results:
        #     print("\n Search Results:")
        #     for row in results:
        #         print(row)
        # else:
        #     print("\n No Employee found with that name")
        
        # employees = [
        #     ("Sudharshan", 25000),
        #     ("Sagar", 30000),
        #     ("Harsha", 25000) 
        # ]
        # cursor.executemany(
        #     "INSERT INTO employees (name,Salary) VALUES (%s, %s)",
        #     employees
        # )

        # conn.commit()


        # cursor.execute("SELECT * FROM employees")
        # print("\n Employee's Records")
        # for row in cursor.fetchall():
        #     print(row)

        # cursor.execute("UPDATE employees SET Salary = 70000 WHERE id =2")
        # conn.commit()
        # print("Employee salary updated sucesfully")

        # emp_id = int(input("\nEnter the employee ID to delete: "))

        # cursor.execute(
        #     "DELETE FROM employees WHERE id = %s",
        #     (emp_id,)
        # )
        # cursor.execute("""
        # CREATE TABLE IF NOT EXISTS products (
        #     product_id INT AUTO_INCREMENT PRIMARY KEY,
        #     product_name VARCHAR(100),
        #     price FLOAT,
        #     employee_id INT,
        #     FOREIGN KEY (employee_id) REFERENCES employees(id)
        # )
        # """)

        # cursor.execute("""
        # SELECT p.product_name, p.price, e.name
        # FROM products p 
        # JOIN employees e ON p.employee_id = e.id              
        # """)

        # results = cursor.fetchall()
        # print("\n Producst with employee Names: ")
        # for row in results:
        #     print(row)




        # conn.commit()
        # print("✅ Products table created successfully")
        # if cursor.rowcount > 0:
        #     print("Employee record has been deleted sucessfully")
        # else:
        #     print("No employee found with that id")

except mysql.connector.Error as err:
    print("❌ Error:", err)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔒 Connection closed")
