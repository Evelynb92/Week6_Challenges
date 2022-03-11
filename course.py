class Course():
  def __init__(self, course_id, course_name, instructor, classroom, max_seats ="", enrolled_students ="", start_time ="", end_time ="", course_days ="", hybrid =""):
    
    self.course_id = course_id
    self.course_name = course_name
    self.instructor = instructor
    self.classroom = classroom
    self.max_seats = max_seats
    self.enrolled_students = enrolled_students
    self.start_time = start_time
    self.end_time = end_time
    self.course_days = course_days
    self.hybrid = hybrid

  