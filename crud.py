import psycopg2

# Database connection parameters
hostname = 'localhost'
database = 'demo'
username = 'postgres'
password = 'Vishalrai2000@'
port_id = 5432

def main():
    conn = None
    cur = None

    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=password,
            port=port_id 
        )
        cur = conn.cursor()
        
        # Create table
        create_table(cur)
        
        # User input
        while True:
            print("\nOptions:")
            print("1. Insert Record")
            print("2. Update Record")
            print("3. Delete Record")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                insert_data(cur)
            elif choice == '2':
                update_data(cur)
            elif choice == '3':
                delete_data(cur)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        
        # Commit changes
        conn.commit()
        
    except Exception as error:
        print("Error:", error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
            
def create_table(cur):
    create_script = '''
    CREATE TABLE IF NOT EXISTS employee (
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        salary INTEGER,
        dept_id VARCHAR(30)
    )
    '''
    cur.execute(create_script)
    print("Table 'employee' created or already exists.")

def insert_data(cur):
    id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    salary = input("Enter employee salary: ")
    dept_id = input("Enter department ID: ")

    insert_script = 'INSERT INTO employee(id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
    cur.execute(insert_script, (id, name, salary, dept_id))
    print("Record inserted.")

def update_data(cur):
    emp_id = input("Enter employee ID to update: ")
    new_salary = input("Enter new salary: ")

    update_script = 'UPDATE employee SET salary = %s WHERE id = %s'
    cur.execute(update_script, (new_salary, emp_id))
    print("Record updated.")

def delete_data(cur):
    emp_id = input("Enter employee ID to delete: ")

    delete_script = 'DELETE FROM employee WHERE id = %s'
    cur.execute(delete_script, (emp_id,))
    print("Record deleted.")

if __name__ == '__main__':
    main()

