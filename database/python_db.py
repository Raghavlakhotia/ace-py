# install pip install psycopg2
import psycopg2

conn = psycopg2.connect(host='localhost',dbname="postgres",user='postgres',password='raghav123',port=5432)

curr = conn.cursor()

curr.execute('''CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR);'''
)

curr.execute('''
             INSERT INTO person(id, name,age, gender) VALUES 
             (1, 'Raghav', 30, 'M'),
             (2, 'Mark', 51, 'M'),
             (3, 'Luis', 33, 'F'),
             (4, 'Zak', 32, 'M');
             ''')

curr.execute('''
             SELECT * FROM person;''')

print(curr.fetchone())

for row in curr.fetchall():
    print(row)
    

conn.commit()

curr.close()
conn.close()