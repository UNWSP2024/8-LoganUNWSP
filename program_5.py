#Logan H's Course Info (w/ PsuedoCode)
#
# BEGIN
# CREATE empty dictionary courses

# REPEAT
# PROMPT user to enter course ID( or type "done" to stop)
#  IF input is "done"
#             EXIT loop
#         PROMPT user to enter course name
#         STORE course ID and course name in courses dictionary
#
#     PROMPT user to enter a subject prefix (e.g., "COS")
#
#     DISPLAY all course ID and names where the course ID starts with the given subject prefix
#
# END

def get_courses_by_subject():
    courses = {}

    while True:
        course_id = input("Enter course ID (or type 'finished' to finish): ").strip()
        if course_id.lower() == 'finished':
            break

        course_name = input("Enter course name: ").strip()
        courses[course_id] = course_name

    subject = input("Enter a subject prefix to filter courses (e.g., 'COS'): ").strip()

    print("\nCourses matching subject:")
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")


get_courses_by_subject()
