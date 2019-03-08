
'''
TODO's:
Needs to match confirm password and password values before registering
Needs to create Course Advisor Object Oriented
Needs an Expert System for Students to determine how much courses they should take
Needs to have an Expert System for Determining which courses should be retaken
Probation checker
Adding elective and capstone courses in database
adding them into prereq Knowledge Base
Add a friggin Front end for this project
the AI needs more classifiers

'''

from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from pyknow import *
from .engine import *
from django.contrib import sessions
from .prerequisites import Prereq
import math
# Create your views here.
#updates needed in line numbers
#42




class Studentasist:

    def index(request):
        return render(request, 'home.html')
        #return render(request, "login/login.html")

    def login(request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def loginaction(request):
        form = LoginForm(request.POST)
        if form.is_valid():
            uid = form.cleaned_data["nsu_id"]
            password = form.cleaned_data['password']
            u = Student.objects.get(uni_id = uid)
            if u.password == password:
                request.session["uni_id"] = u.uni_id
                return HttpResponseRedirect('/profile')
            else:
                return HttpResponse('<h1> password or username donot match</h1><h2>are you trying to do anything naughty?</h2>')

#registers users
    def register(request):
        form = RegistrationForm()
        return render(request, "register.html", {"form":form})

#gets the post data and creates a 46 grades data for each students
    def registeraction(request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            uid= form.cleaned_data["user_id"]
            fullname = form.cleaned_data["fullname"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            #check confirm password is similer or not
            stobj = Student(uni_id=uid,fullname=fullname,email=email,password=password)
            s = Courses.objects.all()

            for i in s:
                x = Grades(Student_id=uid, Course_name=i.coursename)
                x.save()


            stobj.save()
            return HttpResponseRedirect('/login')

    def gradecal(request):
        if request.session.has_key('uni_id'):
            form = GradeForm()
            return render(request,"gradecalculate.html", {'form':form})
        else:
            return HttpResponseRedirect('/login')

    #updates the grades of students
    #calculates cgpa

    def gradecalaction(request):
        grdparam = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0,
                    'F': 0.0}
        converter = {'1':'A','2':'A-','3':'B+','4':'B','5':'B-','6':'C+','7':'C','8':'C-','9':'D' }
        if request.session.has_key('uni_id'):
            uid = request.session['uni_id']
            form = GradeForm(request.POST)
            if form.is_valid():
                crsname= form.cleaned_data['coursename']
                crsgrade = form.cleaned_data['coursegrade']
                sem = form.cleaned_data['semester']
                crsgrade = converter[crsgrade]
                grdobj = Grades.objects.get(Student_id=uid, Course_name=crsname)
                grdobj.grdpa=grdparam[crsgrade]
                grdobj.grade = crsgrade
                grdobj.semnum = sem
                grdobj.save()
                std = Student.objects.get(uni_id= uid)

                std.updatecgpa()
                std.updatecatcgpa('SEPS')
                std.updatecatcgpa('UNI')
                std.updatecatcgpa('CORE')
                #cgpa update


                '''
                total_credit = 0
                m = 0


                grd = Grades.objects.filter(Student_id=uid)

                for g in grd:
                    if (g.grade != 'N'):
                        cr = Courses.objects.get(coursename=g.Course_name)
                        total_credit = total_credit + cr.credits
                        m = m + g.grdpa * cr.credits

                cgpa = m / total_credit
                stdobj = Student.objects.get(uni_id=uid)
                stdobj.total_credits = total_credit
                stdobj.cgpa = cgpa
                stdobj.save()
'''
                return HttpResponseRedirect('/gradecal')

    def gradehistory(request):
        if request.session.has_key('uni_id'):
            uid = request.session['uni_id']
            grdobj = Grades.objects.filter(Student_id = uid)
            d= []
            for g in grdobj:
                if(g.grade!= 'N'):
                    d.append(g)

            return render(request,'Gradehistory.html',{'gradedata': d})



    def profile(request):
        if request.session.has_key("uni_id"):
            stdid = request.session['uni_id']
            stddata = Student.objects.get(uni_id= stdid)
            stddata.updatecatcgpa('SEPS')
            stddata.updatecatcgpa('UNI')
            stddata.updatecatcgpa('CORE')
            context = {"stinfo": stddata}
            return render(request, 'profile.html', context)

    #generates facts & creates inference engine of prerequisites
    def courseadvise(request):

        if request.session.has_key('uni_id'):
            l=[]  #list of courses he can take
            l.clear()
            seps = []
            seps.clear()
            cse = []
            cse.clear()
            uni = []
            uni.clear()
            uid = request.session['uni_id']
            grdobj = Grades.objects.filter(Student_id= uid)
            engine = Prereq()
            engine.reset()
            for g in grdobj:

                engine.declare(Fact(g.Course_name,grade=g.grade))
            engine.run()

            #complicated sector
            maxcrd= 12 #max credit a student can take
            cfts = 0 # total credit he should be taking
            n = [] # list of courses he should be taking
            t = engine.listpass()
            a1 = engine.unicourses()
            a2 = engine.SEPScourses()
            a3 = engine.corecourses()
            p = 13
            for j1 in a1:
                unicrc = Courses.objects.get(coursename=j1)
                prio1 = unicrc.priority
                uni.append((prio1,j1))
            for j2 in a2:
                sepscrc = Courses.objects.get(coursename=j2)
                prio2 = sepscrc.priority
                seps.append((prio2, j2))

            for j3 in a3:
                csecrc = Courses.objects.get(coursename=j3)
                prio3 = csecrc.priority
                cse.append((prio3, j3))


            for m in t:
                crs = Courses.objects.get(coursename=m)
                if p >= crs.priority:
                    p = crs.priority
            catprio = {'CORE':1,'SEPS':2,'UNI':3}
            for m1 in t:
                crss = Courses.objects.get(coursename=m1)
                m2 = catprio[crss.category]
                ch = crss.credits
                print(crss.category)
                l.append((crss.priority, m2 ,ch, m1))
                #if p == crss.priority:
                #   l.append((crss.priority,m1))
            a1.clear()
            a2.clear()
            a3.clear()
            t.clear()
            l= sorted(l)
            '''Not perfectly Working '''
            for i in l:
                if cfts <= maxcrd:
                    n.append(i[3])
                    cfts = cfts + i[2]
                else:
                    break





        return render(request, "courseadvisor.html", {'suggested': n,'dat': l, 'csecore': sorted(cse), 'sepscore': sorted(seps), 'unicore': sorted(uni)})


    def showgradpath(request):
        if request.session.has_key("uni_id"):
            lst = []
            i=1
            stdid = request.session['uni_id']
            grdobj = Grades.objects.filter(Student_id=stdid)
            for grd in grdobj:
                c = Courses.objects.get(coursename= grd.Course_name)
                lst.append([c.credits,grd.Course_name,grd.grade])
                i=i+1
            obj = Gradepath(lst)
            d = obj.returncoursepath()
            print(d)

            return render(request,'coursepath.html',{'data':d})






    def logout(request):
        try:
            del request.session['uni_id']
        except:
            return HttpResponse("<h1> Could not logout for some reason</h1>")
        return HttpResponseRedirect('/login')





    #test views not functional
    def refreshgrade(request):
        total_credit =0
        m =0
        if request.session.has_key('uni_id'):
            uid = request.session['uni_id']
            grd = Grades.objects.filter(Student_id= uid)

            for g in grd:
                if (g.grade != 'N'):
                    cr = Courses.objects.get(coursename=g.Coursename)
                    total_credit = total_credit + cr.credits
                    m = m + grd.grdpa * cr.credits

            cgpa = m/total_credit

            stdobj = Student.objects.get(uni_id=uid)
            stdobj.total_credits = total_credit
            stdobj.cgpa = cgpa
            stdobj.save()
            return HttpResponse('<h1>cgpa updated</h1>')

