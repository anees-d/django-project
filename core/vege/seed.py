from faker import Faker
import random
from .models import Department, Student, StudentID, SubjectMarks, Subjects
from django.db.models import Sum
from .models import ReportCard


fake = Faker()

def create_subject_marks(n=100):
    try:
        student_objs = Student.objects.all()
        subject_objs = Subjects.objects.all()

        if not student_objs.exists():
            print("No students found.")
            return

        if not subject_objs.exists():
            print("No subjects found.")
            return

        count = 0
        while count < n:
            student = random.choice(student_objs)
            subject = random.choice(subject_objs)

            # Optional: Avoid duplicates
            if not SubjectMarks.objects.filter(subject=subject, student=student).exists():
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0, 100)
                )
                count += 1
                print(f"✅ Created mark {count}: Student={student.id}, Subject={subject.id}")
            else:
                continue

        print(f"🎉 Successfully created {n} subject marks.")
        
    except Exception as e:
        print(f"❌ Error creating subject marks: {e}")


def seed_db(n=10):
    try:
        for i in range(n):
            department_list = Department.objects.all()
            if not department_list:
                print("No departments found.")
                continue

            department = random.choice(department_list)

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

        print(f"✅ Successfully added {n} students.")

    except Exception as e:
        print(f"❌ Error seeding database: {e}")

def generate_report_card():
    print('CALLLLLED')

    # Rank calculation logic
    ranks = Student.objects.annotate(
        marks=Sum('studentmarks__marks')
    ).order_by('-marks', '-student_age')

    i = 1
    for rank in ranks:
        print(rank)
        ReportCard.objects.create(
            student=rank,
            student_rank=i
        )
        i += 1