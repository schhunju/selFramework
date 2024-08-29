import psycopg2
from configparser import ConfigParser
from selenium import webdriver


# Function to read database configuration from the config file
def config(filename='database.ini', section='postgresql'):
    # Create a parser
    parser = ConfigParser()
    # Read the config file
    parser.read(filename)

    # Get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db


# CRUD Operations
try:
    # Connecting to the PostgreSQL database
    params = config()  # Read connection parameters from database.ini
    connection = psycopg2.connect(**params)
    cursor = connection.cursor()

    # Creating the 'student' table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS student (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        address VARCHAR(255),
        age INT
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    print("Table 'student' created successfully")

    # Inserting a new student record (Create)
    insert_query = """
    INSERT INTO student (name, address, age)
    VALUES (%s, %s, %s)
    RETURNING id;
    """
    cursor.execute(insert_query, ('Archana', 'Kapan', 23))
    connection.commit()
    student_id = cursor.fetchone()[0]
    print(f"Inserted student with ID: {student_id}")

    # Reading the student records (Read)
    select_query = "SELECT * FROM student;"
    cursor.execute(select_query)
    records = cursor.fetchall()
    print("Student records:")
    for row in records:
        print(row)

    # Updating a student record (Update)
    update_query = """
    UPDATE student
    SET name = %s, address = %s, age = %s
    WHERE id = %s;
    """
    cursor.execute(update_query, ('Amrit', 'Budhanilkantha', 23, student_id))
    connection.commit()
    print(f"Updated student with ID: {2}")

    # Deleting a student record (Delete)
    delete_query = "DELETE FROM student WHERE id = 16;"
    cursor.execute(delete_query)
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while performing CRUD operations", error)

