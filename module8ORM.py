import sqlite3
from peewee import *

db = SqliteDatabase("module8-ORM.db")


class students(Model):
    student_id = IntegerField(column_name="student_id", primary_key=True)
    name = CharField(column_name="name")
    surname = CharField(column_name="surname")
    age = IntegerField(column_name="age")
    city = CharField(column_name="city")

    class Meta:
        database = db

    def seach_students(limit_age=None, course_name=None, city=None):
        answer = students.select()
        if limit_age:
            answer = answer.where(students.age > limit_age)
        if city:
            answer = answer.where(students.city == city)
        if course_name:
            answer = (
                answer.join(students_courses)
                .where(students_courses.course_id == courses.course_id)
                .join(courses)
                .where(courses.course_name == course_name)
            )
        for i in answer:
            print(i.name, i.surname, i.age, i.city)


students.create_table()

max_brooks = students.get_or_create(
    student_id=1, name="Max", surname="Brooks", age=24, city="Spb"
)
djon_stones = students.get_or_create(
    student_id=2, name="John", surname="Stones", age=15, city="Spb"
)
andy_wings = students.get_or_create(
    student_id=3, name="Andy", surname="Wings", age=45, city="Manhester"
)
kate_brooks = students.get_or_create(
    student_id=4, name="Kate", surname="Brooks", age=34, city="Spb"
)


class courses(Model):
    course_id = IntegerField(column_name="course_id", primary_key=True)
    course_name = CharField(column_name="course_name")
    time_start = DateField(column_name="time_start")
    time_end = DateField(column_name="time_end")

    class Meta:
        database = db


courses.create_table()

python = courses.get_or_create(
    course_id=1, course_name="python", time_start="2021-07-21", time_end="2021-08-21"
)
java = courses.get_or_create(
    course_id=2, course_name="java", time_start="2021-07-13", time_end="2021-08-16"
)


class students_courses(Model):
    student_id = ForeignKeyField(students, column_name="student_id")
    course_id = ForeignKeyField(courses, column_name="course_id")

    class Meta:
        database = db


students_courses.create_table()
x1 = students_courses.get_or_create(student_id=1, course_id=1)
x1 = students_courses.get_or_create(student_id=2, course_id=1)
x1 = students_courses.get_or_create(student_id=3, course_id=1)
x1 = students_courses.get_or_create(student_id=4, course_id=2)


students.seach_students(limit_age=None, course_name=None, city=None)
