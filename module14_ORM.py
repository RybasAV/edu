from peewee import *
import unittest

db_proxy = Proxy()

class BaseModel(Model):
    class Meta:
        database = db_proxy

class Students(BaseModel):
    student_id = AutoField()
    name = CharField()
    surname = CharField()
    age = IntegerField()
    city = CharField()

    @classmethod
    def search_students(cls, limit_age=None, course_name=None, city=None):
        query = cls.select().distinct()
        if limit_age:
            query = query.where(cls.age > limit_age)
        if city:
            query = query.where(cls.city == city)
        if course_name:
            query = (query
                     .join(StudentsCourses)
                     .join(Courses)
                     .where(Courses.course_name == course_name))
        return query

class Courses(BaseModel):
    course_id = AutoField()
    course_name = CharField()
    time_start = DateField()
    time_end = DateField()

class StudentsCourses(BaseModel):
    student = ForeignKeyField(Students, backref='courses')
    course = ForeignKeyField(Courses, backref='students')

test_db = SqliteDatabase(":memory:")

class TestUniversityORM(unittest.TestCase):
    def setUp(self):
        db_proxy.initialize(test_db)
        test_db.create_tables([Students, Courses, StudentsCourses])

    def tearDown(self):
        test_db.drop_tables([Students, Courses, StudentsCourses])
        test_db.close()

    def test_add_student(self):
        Students.create(name="Ivan", surname="Ivanov", age=20, city="Moscow")
        exists = Students.select().where(Students.name == "Ivan").exists()
        self.assertTrue(exists)

    def test_add_course(self):
        Courses.create(
            course_name="Data Science",
            time_start="2023-01-01",
            time_end="2023-05-01"
        )
        course = Courses.get(Courses.course_name == "Data Science")
        self.assertEqual(course.course_name, "Data Science")

    def test_delete_student(self):
        student = Students.create(name="Mark", surname="Delete", age=30, city="Tula")
        Students.delete().where(Students.student_id == student.student_id).execute()
        exists = Students.select().where(Students.student_id == student.student_id).exists()
        self.assertFalse(exists)

    def test_search_logic(self):
        s1 = Students.create(name="Ivan", surname="Ivanov", age=25, city="Moscow")
        c1 = Courses.create(course_name="Python", time_start="2023-01-01", time_end="2023-05-01")
        StudentsCourses.create(student=s1, course=c1)
        
        results = Students.search_students(limit_age=20, course_name="Python")
        self.assertEqual(results.count(), 1)
        self.assertEqual(results[0].name, "Ivan")

if __name__ == "__main__":
    unittest.main()