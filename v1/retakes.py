from pyknow import *

class Retakes(KnowledgeEngine):
    gradeparam = {'D':1, 'D+':2, 'C-': 3,'C':4, 'C+':5, 'B-':6, 'B':7}
    coreparam = {'CSE':1, 'SEPS': 2, 'UNI': 3, 'CAPS':4, 'TRAIL':5}
    retakes = []
    corere =[]
    sepsre = []
    unire = []
    #@Rule(Fact(MATCH.coursename, grade= ~L('N')& ~L('F')& ~L('A')& ~L('A-')& ~L('B+')))
    #def take(self, coursename):
     #   pass
    '''basic retaking list'''

    @Rule(AS.courses << Fact(name=W(), grade= ~L('N')& ~L('F')& ~L('A')& ~L('A-')& ~L('B+'), category="CSE"))
    def take2(self, courses):
        f = courses.as_dict()
        self.retakes.append([self.gradeparam[f['grade']],self.coreparam[f['category']],f['name']])
        self.corere.append([self.gradeparam[f['grade']], f['name']])

    @Rule(AS.courses << Fact(name=W(), grade=~L('N') & ~L('F') & ~L('A') & ~L('A-') & ~L('B+'), category="SEPS"))
    def takeseps(self, courses):
        f = courses.as_dict()
        self.retakes.append([self.gradeparam[f['grade']], self.coreparam[f['category']], f['name']])
        self.sepsre.append([self.gradeparam[f['grade']], f['name']])

    @Rule(AS.courses << Fact(name=W(), grade=~L('N') & ~L('F') & ~L('A') & ~L('A-') & ~L('B+'), category="UNI"))
    def takeuni(self, courses):
        f = courses.as_dict()
        self.retakes.append([self.gradeparam[f['grade']], self.coreparam[f['category']], f['name']])
        self.unire.append([self.gradeparam[f['grade']], f['name']])

    ''' calculating cgpa in different scenarios '''



    def listpass(self):
        return self.retakes