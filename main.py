# Define a base class Person
class Person:
    def __init__(self, surname, firstname, email):
        self.surname = surname
        self.first_name = firstname
        self.email = email


# Define a subclass Lecturer inheriting from Person
class Lecturer(Person):
    def __init__(self, surname, firstname, email, academic_title):
        super().__init__(surname, firstname, email)
        self.academic_title = academic_title


# Define a subclass Student inheriting from Person
class Student(Person):
    def __init__(self, surname, firstname, email, matriculationnumber, university):
        super().__init__(surname, firstname, email)
        self.matriculationnumber = matriculationnumber
        self.university = university
        self.courses_registered = 0


# Define a class Course
class Course:
    def __init__(self, course_name, lecturer):
        self.name = course_name
        self.lecturer = lecturer
        self.participants = []

    # Method to register a student for the course
    def register_student(self, student):
        # Check if the course is full
        if len(self.participants) >= 10:
            return "The number of Students in a course cannot exceed 10"
        # Check if the student's email is already registered for the course
        for participant in self.participants:
            if participant.email == student.email:
                return "This email address has been taken!"
        # Check if an external student has already registered for another course
        if student.university != "university name" and student.courses_registered >= 1:
            return "External students are only limited to one course."
        # Add the student to the course participants
        self.participants.append(student)
        student.courses_registered += 1
        return "You have successfully Registered for a course."

    # Method to check the status of the course
    def status_of_the_course(self):
        if len(self.participants) < 3:
            return "Course will not take place."
        return " "

    # Method to get the number of available slots in the course
    def number_of_available_slots(self):
        return 10 - len(self.participants)

    # Method to represent the Course object as a string
    def __str__(self):
        return f"Course: {self.name}, Lecturer: {self.lecturer.academic_title} {self.lecturer.first_name} {self.lecturer.surname}, Participants: {len(self.participants)}"


# Function to register a student for a course
def register():
    first_name = input("Input your first name ")
    surname = input("Input your surname ")
    email = input("Input your email address ")
    university = input("Input the name of your university ")
    matriculation_number = input("Input your matriculation number: ")
    student = Student(surname, first_name, email, matriculation_number, university)

    print("Below is a list of the available courses")
    for i, course in enumerate(offered_courses):
        print(f"{i + 1}. {course.name}")

    course_choice = int(input("Input course number: ")) - 1
    result = offered_courses[course_choice].register_student(student)
    print(result)


# Sample Lecturer Data
first_lecturer = Lecturer("surname", "firstname", "email", "title")
second_lecturer = Lecturer("surname", "firstname", "email", "title")
third_lecturer = Lecturer("surname", "firstname", "email", "title")

# Sample Course Data
first_course = Course("Programming", first_lecturer)
second_course = Course("Databases", second_lecturer)
third_course = Course("Software Engineering", third_lecturer)

offered_courses = [first_course, second_course, third_course]


# Function to display the details of all courses
def list_of_courses():
    for course in offered_courses:
        print(course)
        for participant in course.participants:
            print(f" - {participant.first_name} {participant.surname}, {participant.email}, {participant.university}")
        if len(course.participants) < 3:
            print("  Course will not take place.")


# Function to display available courses with available slots
def list_of_available_courses():
    for course in offered_courses:
        if len(course.participants) < 10:
            print \
                (f"{course.name}: {course.number_of_available_slots()} slots available. Lecturer: {course.lecturer.academic_title} {course.lecturer.first_name} {course.lecturer.surname}")


# Function to terminate the program and notify participants of courses that will not take place
def terminate():
    print("Notification for courses that will not take place:")
    for course in offered_courses:
        if len(course.participants) < 3:
            for participant in course.participants:
                print(f"Notify: {participant.first_name} {participant.surname}, {participant.email}")


# Function to display the menu and handle user input
def menu():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Course details")
        print("3. Available courses")
        print("4. End")

        choice = input("Input a choice number: ")
        if choice == "1":
            register()
        elif choice == "2":
            list_of_courses()
        elif choice == "3":
            list_of_available_courses()
        elif choice == "4":
            terminate()
            break
        else:
            print("Your choice is invalid!")


# Main function to run the program
if __name__ == "__main__":
    menu()
