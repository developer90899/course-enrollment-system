# Initialize the data structures
courses = {
    "Math": set(),
    "English": set(),
    "History": set(),
    "Science": set()
}

students = {
    1: ('moaz', []),
    2: ('ali', []),
    3: ('sara', [])
}
def view_enrollments():
    for course, enrolled_students in courses.items():
        print(f'\n{course} has {len(enrolled_students)} student(s) enrolled')
        for student_id in enrolled_students:
            print(f"- {students[student_id][0]} (ID: {student_id})")

# Display Menu
def display_menu():
    print("\nCourse Enrollment System")
    print("1. Enroll a student in a course")
    print("2. View courses and enrolled students")
    print("3. Add a new course")
    print("4. Quit")

# Enroll a student
def enroll_student():
    try:
        student_id = int(input('Enter the student ID: '))
        # check ID exist
        if student_id in students:
            course = input('enter the course name: ').capitalize()
            # Check Course exist
            if course in courses:
                courses[course].add(student_id)
                students[student_id][1].append(course)
                print(f'{students[student_id][0]} has been enrolled in {course}')
            else:
                print('Course is not found')
        else:
            print('ID not found')
    except:
        print("ID is number")

# Add Course
def add_course():
    course = input("Enter the new course: ").capitalize()
    if course not in courses:
        courses.update({(course): set()})
        print (f"{course} has been added as a new course!")
    else:
        print("Course already exists.")

# Running project
while True:
    display_menu()
    choice = input("Enter an option (1-4): ")

    if choice == "1":
        enroll_student()
    elif choice == '2':
        view_enrollments()
    elif choice == '3':
        add_course()
    elif choice == '4':
        print('Goodbye!')
        exit()
    else:
        print('Invalid choice. Please Choose a number between 1 and 4.')






