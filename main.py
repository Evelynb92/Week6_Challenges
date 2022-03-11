from course import Course
from professor import Professor
from student import Student
import random


# first_name, last_name, nationality, classification,student_id, gpa="",advisor="", major="", second_major="", minor="", courses_taken="", courses_enrolled =""
student_1 =Student("Samantha", "Smith","American", "Sophomore", "SS1254632")
student_2 =Student("Bobby", "Flores","British", "Freshman", "BF1254630",major="Chemistry")
student_3 =Student("Carolyn", "Green","Dutch", "Senior", "CG1254635", courses_taken="Organic Chemistry 1")
student_4 =Student("Eugene", "Nelson","Greek", "Senior", "EN12546371")
student_5 =Student("Roy", "Collins","Colombian", "Junior", "RC12546331")
student_6 =Student("Juan", "Reyes","Czech", "Junior", "JR125463S81")
student_7 =Student("Arthur", "Edwards","Danish", "Sophomore", "AE12546311")
student_8 =Student("Lawrence", "Cruz","Egyptian", "Sophomore", "LC12546321")
student_9 =Student("Sean", "Diaz","American", "Freshman", "SD12546341")
student_10 =Student("Janet", "Parker","British", "Sophomore", "JP12546351")
student_11 =Student("Ethan", "Carter","British", "Freshman", "EC12546361")
student_12 =Student("Kyle", "Roberts","Armenian", "Sophomore", "KR12546391")
student_13 =Student("Nathan", "Evans","American", "Senior", "NE12546301")
student_14 =Student("Megan", "Kelly","Belgian", "Sophomore", "MK12546361")
student_15 =Student("Christina", "Murphy","Jamaican", "Freshman", "CM12546371")
student_16 =Student("Diane", "Morris","Antiguan", "Junior", "DM12546361")
student_17 =Student("Noah", "Cook","Barbadian", "Senior", "NC15546371")
student_18 =Student("Douglas", "Morgan","Australian", "Sophomore", "DM13546331")
student_19 =Student("Terry", "Smith","British", "Junior", "TS1254631")
student_20 =Student("Evelyn", "Reed","Afghan", "Senior", "ER12546351", major="Business", gpa=3.1, courses_taken =["Biology","Math"])

student_list = [student_1,student_2,student_3,student_4,student_5,student_6,student_7,student_8,student_9,student_10,student_11,student_12,student_13,student_14,student_15,student_16,student_17,student_18,student_19,student_20]


# for disciple in student_list:
#   print(disciple.first_name, disciple.last_name)


# i = 0
# while i < 5:
#   rand = random.choice(student_list)
#   print(rand.first_name, rand.last_name)
#   i +=1

# first_name, last_name, specialty, office_location, salary, tenure, courses_taught="", office_hours_start="", office_hours_stop="", office_hour_days=""

professor_1 = Professor('Greg', 'Joseph', 'Science', 'Bldg 4', 90000, '10 years', 'Biology', '8 am', '2 pm')
professor_2 = Professor('Michael', 'Wilson', 'Art', 'Bldg 1', '70000', '4 years', 'Biology', '8 am', '2 pm')
professor_3 = Professor('Charles', 'Davis', 'Physics', 'Bldg 7', '80000', '5 years', 'Biology', '8 am', '2 pm')
professor_4 = Professor('Maria', 'Jackson', 'Nuclear Engineering', 'Bldg C', '98000', '7 years', 'Biology', '8 am', '2 pm')
professor_5 = Professor('Matthew', 'Thomas', 'Genetics', 'Bldg A', '97000', '9 years', 'Biology', '8 am', '2 pm')
professor_6 = Professor('Mark', 'Clark', 'Astronomy', 'Bldg 6', '65000', '1 month',office_hours_start= '8 am')
professor_7 = Professor('Victoria', 'Lewis', 'Chemistry', 'Bldg 5', '95000', '6 years', 'Biology', '8 am', '2 pm')
professor_8 = Professor('Rachel', 'King', 'Biochemistry', 'Bldg B', '100000', '12 years', 'Biology', '8 am', '2 pm')
professor_9 = Professor('Nicole', 'Scott', 'Marine Biology', 'Bldg 2', '89000', '5 years', 'Biology', '8 am', '2 pm')
professor_10 = Professor('Elijah', 'Allen', 'Cellular Biology', 'Bldg 3', '105000', '11 years', 'Biology', '8 am', '2 pm')

professor_list = [professor_1,professor_2,professor_3,professor_4,professor_5,professor_6,professor_7,professor_8,professor_9,professor_10]

# prof_length = len(professor_list)
# sum = 0
# for i in professor_list:
#   i.salary
#   sum += int(i.salary)

# avg = sum/prof_length
# print(f"The average salary for the {prof_length} professor is {avg}\n")
  
# print(professor_1.salary)

# course_id, course_name, instructor, classroom, max_seats ="", enrolled_students ="", start_time ="", end_time ="", course_days ="", hybrid =""

course_1 = Course('CE1', 'Engineering', 'Mr Joseph','Room 103', 20, 15)
course_2 = Course('CE1', 'Engineering', 'Mr Joseph','Room 103', 20, 15)
course_3 = Course('CE1', 'Engineering', 'Mr Joseph','Room 103', 20, 15)
course_4 = Course('CE1', 'Engineering', 'Mr Joseph','Room 103', 20, 15)
course_5 = Course('CE1', 'Engineering', 'Mr Joseph','Room 103', 20, 15)

course_list = [course_1,course_2,course_3,course_4,course_5]

# print(course_1.course_name)




#############################################################

# Team 3 will build a university platform. Starting with Classes of Student, Course, Professor.

# Student class should have the following instance attributes:

# first_name*, last_name*, nationality*, student_id*, gpa, classification*, advisor, major, second_major, minor, courses_taken, courses_enrolled

# Course class should have the following instance attributes:

# course_id*, course_name*, instructor*, max_seats, enrolled_students, classroom*, start_time, end_time, course_days, hybrid

# Professor class should have the following instance attributes:

# first_name*, last_name*, specialty*, courses_taught, office_location*, office_hours_start, office_hours_stop, office_hour_days, salary*, tenure*


###############################################################

# Tasks (split the work so everyone get practice, I advise sharing a replit with your partner)
#1. Create each classs on a seperate file (name the file the same as the class name). For example, class Animal would be on a file calle animal.py √√

#2. Find out how to import your class to your main file.√√

#3. In your main file, create 20 Passengers, 20 Skus, 20 Students (depending on your respective team). Place them all into a list.√√

#4. In your main file, create 5 Flights, 5 Channels, 5 Courses (depending on your respective team). Place them all into a list.√√

#5. In your main file, create 10 Destinations, 10 Vendors, 10 Professors (depending on your respective team). Place them all into a list.√√

#6. What is the average age of your passengers, price of your Sku, or professor salary?√√

#7. list the full name of each passenger, make and model of each Sku, or full name of every students.√√

#8. randomly print out the name of 5 passengers, 5 sku or 5 students.√√

#9. Check-in Time - Book a time to show me your progress (remote replit share is good)