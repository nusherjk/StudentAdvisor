from django.db import models
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
    '''credits = models.IntegerField(default=0)
    cat1ptr = models.IntegerField(default=0)
    cat2ptr = models.IntegerField(default=0)
    cat3ptr = models.IntegerField(default=0)
    cat4ptr = models.IntegerField(default=0)'''

    def updatecgpa(self):
        total_credit = 0
        m = 0

        grd = Grades.objects.filter(Student_id=self.uni_id)

        for g in grd:
            if (g.grade != 'N'):
                cr = Courses.objects.get(coursename=g.Course_name)
                total_credit = total_credit + cr.credits
                m = m + g.grdpa * cr.credits

        self.cgpa = m / total_credit
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
            self.sepscgpa = m/cred
        elif set == 'UNI':
            self.unicgpa = m/cred
        elif set == 'CORE':
            self.corecgpa = m/cred
        else:
            print('Something went Wrong')

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
    credits = models.FloatField()
    priority = models.IntegerField()
    category = models.CharField(max_length=6)


    def __str__(self):
        return self.coursename
    '''cat1ptr = models.IntegerField(default=0)
    cat2ptr = models.IntegerField(default=0)
    cat3ptr = models.IntegerField(default=0)
    cat4ptr = models.IntegerField(default=0)'''

