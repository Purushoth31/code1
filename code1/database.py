import psycopg2

db_credentials = {
    "host": "your_host",
    "database": "student_details",
    "user": "postgres",
    "password": "12345"
}

def create_student_table():
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER,
            grade VARCHAR(10)
        );
    '''

    connection = psycopg2.connect(**db_credentials)

    cursor = connection.cursor()
    cursor.execute(create_table_query)   
    connection.commit()
    cursor.close()
    connection.close()

def insert_student_details(name, age, grade):
    insert_query = '''
        INSERT INTO students (name, age, grade)
        VALUES (%s, %s, %s);
    '''
    connection = psycopg2.connect(**db_credentials)
    cursor = connection.cursor()
    cursor.execute(insert_query, (name, age, grade))

    connection.commit()
    cursor.close()
    connection.close()
create_student_table()
insert_student_details("John Doe", 20, "A")