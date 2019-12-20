from django.db import models
from django.db.models import Max
'''
Each Courses are either from SEPS or University General Education or from CSE core courses 
and a student must have to maintain a specific CGPA in these category in the end of the degree

'''
class Student(models.Model):
    uni_id = models.IntegerField(unique=True, primary_key=True)
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    cgpa = models.FloatField(default=0.00)
    total_credits = models.FloatField(default=0.0)
    sepscgpa = models.FloatField(default=0.0)
    corecgpa = models.FloatField(default=0.0)
    unicgpa = models.FloatField(default=0.0)
    semunmber = models.IntegerField(default=0)
    

    def updatecgpa(self):
        total_credit = 0
        m = 0

        grd = Grades.objects.filter(Student_id=self.uni_id)

        for g in grd:
            if (g.grade != 'N'):
                cr = Courses.objects.get(coursename=g.Course_name)
                total_credit = total_credit + cr.credits
                m = m + g.grdpa * cr.credits
        if total_credit!=0:
            self.cgpa = m / total_credit
        else:
            self.cgpa = 0
        self.total_credits= total_credit
        self.save()

    def updatecatcgpa(self, set):
        cred = 0
        m = 0

        gr = Grades.objects.filter(Student_id = self.uni_id)
        for g in gr:
            if g.grade != 'N':

                cr = Courses.objects.get(coursename=g.Course_name)
                if cr.category == set:
                    cred = cred + cr.credits
                    m = m + g.grdpa * cr.credits
        if set == 'SEPS':
            if cred != 0:
                self.sepscgpa = m / cred
            else:
                self.sepscgpa = 0
        elif set == 'UNI':
            if cred != 0:
                self.unicgpa = m / cred
            else:
                self.unicgpa = 0

        elif set == 'CORE':
            if cred != 0:
                self.corecgpa = m / cred
            else:
                self.corecgpa = 0

        else:
            print('Something went Wrong')

        self.save()

    def getsemnumber(self):
        try:
            grd = Grades.objects.filter(Student_id=self.uni_id).aggregate(Max('semnum'))
            self.semunmber = grd["semnum__max"] + 1
        except e:
            self.semunmber = 0 + 1    
        print(self.semunmber)
        self.save()
        


    def __str__(self):
        return self.fullname





class Grades(models.Model):
    grdsrl = models.AutoField(unique=True,primary_key=True)
    grdpa = models.FloatField(default=0.0)
    grade = models.CharField(max_length=1, default='N')
    semnum = models.IntegerField(default=0)
    Student_id = models.IntegerField()
    Course_name = models.CharField(max_length=5)

    #Student_id = models.ForeignKey('Student' ,on_delete=models.CASCADE)
    #course_id = models.ForeignKey('Courses', on_delete=models.CASCADE)
'''
    cat1ptrern = models.IntegerField(default=0)
    cat2ptrern = models.IntegerField(default=0)
    cat3ptrern = models.IntegerField(default=0)
    cat4ptrern = models.IntegerField(default=0)

'''
class Courses(models.Model):
    courseid = models.AutoField(unique=True, primary_key=True)
    coursename = models.CharField(max_length=5)
    coursetitle = models.CharField(max_length= 100)
    credits = models.FloatField()
    priority = models.IntegerField()
    category = models.CharField(max_length=6)
    software = models.IntegerField(default=0, null=False)
    hardware = models.IntegerField(default=0, null=False)
    math = models.IntegerField(default=0, null=False)
    literature = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.coursename


class ComplainBox(models.Model):
    Complain_number = models.AutoField(unique=True, primary_key= True)
    Complaining_person = models.CharField(max_length=30)
    Complainer_email = models.CharField(max_length= 40)
    message = models.CharField(max_length= 300)

class LostandFound(models.Model):
    lost_id = models.AutoField(unique=True, primary_key= True)
    finders_id = models.IntegerField(null= False)
    itemtype = models.CharField(max_length=30)
    loser_id = models.IntegerField(null=True, default=None)
    finder_contact_email = models.CharField(max_length=40)
    lost_item = models.CharField(max_length=400)
    status = models.BooleanField(default=False)


class EvaluationScripts(models.Model):
    #eval_id = models.AutoField(unique=True, primary_key=True)
    faculty_name = models.CharField(max_length= 200)
    option1_input = models.CharField(max_length= 100)
    option2_input = models.CharField(max_length= 100)
    option3_input = models.CharField(max_length= 100)
    option4_input = models.CharField(max_length= 100)
    option5_input = models.CharField(max_length= 100)
    option6_input = models.CharField(max_length= 100)
    commentinput = models.CharField(max_length= 1000)
    submitter_id = models.IntegerField()


