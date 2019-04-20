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

		#categories
		self.softpoint= 0
		self.hpoint= 0
		self.mathpoint = 0
		self.litpoint = 0
		self.msoftpoint= 0
		self.mhpoint= 0
		self.mmathpoint = 0
		self.mlitpoint = 0
		#boolian datas
		self.probation = False
		self.risk = True
		self.corereqrisk = False
		self.unireqrisk = False
		self.sepsreqrisk = False

	def probationcheck(self):
		if self.student.cgpa < 2.0:
			self.probation = True
			self.risk = True
		if self.student.cgpa <2.5:
			self.risk = True

	def dec1(self):
		if self.probation == True or self.risk == True:
			pass

	def analysis(self):
		for g in gradesofstd:
			s = Courses.objects.get(coursename=g.Course_name)
			self.softpoint +=s.software*(g.grdpa/4)
			self.hpoint += s.hardware*(g.grdpa/4)
			self.mathpoint += s.math*(g.grdpa/4)
			self.litpoint += s.literature*(g.grdpa/4)
			self.msoftpoint += s.software
			self.mhpoint += s.hardware
			self.mlitpoint += s.literature
			self.mmathpoint += s.math
		print(self.msoftpoint, self.mmathpoint)




	def getretakes(self,retakes):
		self.student.sepscgpa
		self.student.unicgpa
		self.student.corecgpa
		rtkcrsobj = []
		for r in retakes:
			s = Courses.objects.get(coursename=r)
			rtkcrsobj.append(s)
			

		#Core requires 2.5

		if self.student.corecgpa < 2.5:
			self.corereqrisk = True
		else:
			self.corereqrisk = False

	
	
		

		#SEPS requires 2.5
		#Uni requires 2.0


		



if __name__ == '__main__':
	sed = Analyse(6)
	sed.analysis()

