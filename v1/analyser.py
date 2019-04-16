from .models import *
from .numofcourses import *
from pyknow import *
'''
if the student is in probation the priority of retakes goes up
we have to calculate which course effects the most in case of retakes

'''
class Analyse:
    def __init__(self, stid):
        self.student = Student.objects.get(uni_id=stid)
        self.gradesofstd= Grades.objects.filter(Student_id=stid)
        self.Coursesobj = []
        for g in gradesofstd:
        	cr = Courses.objects.get(coursename=g.Course_name)
        	self.Coursesobj.append(cr)


    def probationcheck(self):
    	if self.student.cgpa < 2.0:
    		print("currently on probation")
    	if self.student.cgpa <2.5:
    		print("risky area")

    def getretakes(retakes):
    	self.student.sepscgpa
    	self.student.unicgpa
    	self.student.corecgpa
    	rtkcrsobj = []
    	for r in retakes:
    		rtkcrsobj.append(Courses.objects.get(coursename=r))
    	#Core requires 2.5

    	if self.student.corecgpa < 2.5:
    		pass
    
    
    	

    	#SEPS requires 2.5
    	#Uni requires 2.0


        



if __name__ == '__main__':

