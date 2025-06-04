from faker import Faker
import random
from .models import Department, Student, StudentID

fake = Faker()

def seed_db(n=10) -> None:
    try:
        for i in range(n):
            department_list = Department.objects.all()
            if not department_list:
                print("No departments found.")
                continue

            random_index = random.randint(0, len(department_list) - 1)
            department = department_list[random_index]

            student_id = f"STU-0{random.randint(100, 999)}"
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )

        print(f"Successfully added {n} students.")

    except Exception as e:
        print(f"Error seeding database: {e}")
