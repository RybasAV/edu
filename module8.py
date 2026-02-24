import sqlite3


conn = sqlite3.connect("module8.sqlite")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE students
               (id INT PRIMARY KEY ,
                name VARCHAR(15),
                surname VARCHAR(15),
                age INT,
                city VARCHAR(15))'''
 )
cursor.execute('''CREATE TABLE Courses
                (id INT PRIMARY KEY  ,
                name VARCHAR(30),
                time_start DATE,
                time_end DATE)'''
           )
cursor.execute('''CREATE TABLE Student_courses
               (student_id INT,
               course_id INT,
               FOREIGN KEY (student_id) REFERENCES students (id),
               FOREIGN KEY (course_id) REFERENCES courses (id))'''
            )
cursor.execute('''INSERT INTO courses (id, name, time_start, time_end) Values
    (1, 'python', '2021-07-21', '2021-08-21'),
    (2, 'java',   '2021-07-13', '2021-08-16')''')
cursor.execute('''INSERT INTO students (id, name, surname, age, city) VALUES
              (1, 'Max', 'Brooks', 24, 'Spb'),
              (2, 'John', 'Stones', 15, 'Spb'),
              (3, 'Andy', 'Wings', 45, 'Manhester'),
              (4, 'Kate', 'Brooks', 34, 'Spb')'''
               )
cursor.execute('''INSERT INTO student_courses VALUES
               (1, 1),
               (2, 1),
               (3, 1),
               (4, 2)'''
               )
cursor.execute(
    """SELECT * from students 
    where age > 30"""
)
print(cursor.fetchall())
cursor.execute(
    '''SELECT s.name, s.surname, c.name, s.age, s.city
                FROM Students as s
                JOIN Student_courses as sc ON s.id = sc.student_id
                JOIN Courses as c ON sc.course_id = c.id
                WHERE c.name = "python"'''
)
print(cursor.fetchall())
cursor.execute(
    '''SELECT s.name, s.surname, c.name, s.age, s.city
                FROM Students as s
                JOIN Student_courses as sc ON s.id = sc.student_id
                JOIN Courses as c ON sc.course_id = c.id
                WHERE c.name = "python" and s.city = "Spb"'''
)
print(cursor.fetchall())

conn.commit()
conn.close()
