class Instructor:
    def __init__(self, course, duration, lecture_days, time, start_date, end_date, classroom, name):
        self.course = course
        self.duration = duration
        self.lecture = lecture_days
        self.time = time
        self.start = start_date
        self.end = end_date
        self.classroom = classroom
        self.name = name

    def instructor_details(self):
        print(f'''
        Instructor Name - {self.name} \n
        Course Name - {self.course}\n
        duration - {self.duration}\n
        Lecture Days - {self.lecture}\n
        Start Date - {self.start} \n
        End Date - {self.end} \n
        Classroom - {self.classroom}
        
        ''')


res = Instructor("PHYTON","2 MONTHS","Mon-Wed-Fri","9am - 1pm","08-04-2019", "09-06-2019","STUDIO 4","MR Kola")
res.instructor_details()