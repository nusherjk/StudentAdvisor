from .prerequisites import *
from pyknow import *
from .models import Courses


class Engine():
    l = []
    seps = []
    cse = []
    uni = []
    p = 11
    facts  = []

    def __init__(self):
        self.engine = Prereq()
        self.head = len(self.facts)

    def resetengine(self):
        self.engine.reset()

    def setfactdatalist(self, list):
        self.facts.append(list)
        self.head = len(self.facts)

    def getfactdatalist(self):
        return self.facts

    def getfactnumber(self):
        return self.head

    def definefacts(self):
        for f in self.facts:
            #print(f[0],f[1],f[2])
            self.engine.declare(Fact(f[1], grade=f[2]))




    def modifyfacts(self, coursename, grade):
        for h in self.facts:

            if h[1] == coursename:
                print(h[0],h[1],h[2])
                self.engine.retract(h[0])
                self.engine.declare(Fact(coursename, grade=grade))
                h[2] = grade
                h[0] = self.head
                self.head = self.head + 1
            self.facts = sorted(self.facts)

    def getrunning(self):
        n =[]
        srt=[]
        mvp = []
        credit_limit =13 # A knowledge engine for students how much credits should they take on this semester
        this_session_credit =0

        self.engine.run()
        t = self.engine.listpass()
        '''search the courses and sort them by the priority -> credits '''
        print('is it working?')
        for f in t:
            crs = Courses.objects.get(coursename= f)
            mvp.append([crs.priority,crs.credits,crs.coursename])
        t.clear()
        mvp = sorted(mvp)
        for m in mvp:
            if this_session_credit< credit_limit:
                srt.append(m)
                this_session_credit= this_session_credit + crs.credits

        #srt = sorted(srt)
        #print(srt)
        courselist =[]
        for s in srt:
            courselist.append(s[2])
        #p1,p2, courselist = zip(*srt)
        print(courselist)
        return courselist
        #return sorted(srt)
        #print(t)
        '''
        for to in t:
            n.append(to)
        t.clear()
        if len(n) > 4:
            return n[-4:]
        else:
            return n
        '''


    def simulation(self):
        s = self.getrunning()

        print(s)
        while(len(s)!=0):
            for s1 in s:
                self.modifyfacts(s1,'S')
            s.clear()
            s = self.getrunning()
            #print(self.engine.facts)
            #print(s)



class Gradepath():
    def __init__(self, f1):
        self.pathlist = []
        i=0
        while (self.checker(f1) == True):
            # print(f1)
            i = i + 1
            #print(i)
            p = self.runningengine(f1)
            if(len(p)==0):
                break
            self.pathlist.append(p)
            f1 = self.changinglist(p, f1)


    def returncoursepath(self):
        return self.pathlist

    def checker(self,d):
        i = 0
        # print(d)
        for d1 in d:
            # print(d1[2])
            if d1[2] == 'N':
                # print(d1)

                # print(d1[2])
                return True
            else:
                pass
        return False


    def runningengine(self,fprog):

        e = Engine()
        e.resetengine()
        for f2 in fprog:
            e.setfactdatalist(f2)
        e.definefacts()
        # print(e.getfactnumber())
        # e.simulation()
        p = e.getrunning()

        print(p)
        return p
    def changinglist(self,prevcrs,list):
        print("in changing list")
        print(prevcrs)
        for p1 in prevcrs:
            for w1 in list:
                if w1[1] == p1:
                    w1[2] = 'S'
        return list
'''
if __name__ == '__main__':
    lst=[]
    i =1
    grdobj = Grades.objects.filter(Student_id=stdid)
    for grd in grdobj:
        lst.append([i, grd.Course_name, grd.grade])
        i=i+1
    obj = Gradepath(lst)
    d = obj.returncoursepath()
    print(d)
'''