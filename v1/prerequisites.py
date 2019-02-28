from pyknow import *
import pyknow.fact

class Prereq(KnowledgeEngine):

    s=[]
    CSEcore = []
    SEPScore =[]
    UNIcore = []

    #def clean(self):
     #   self.s.clear()

    # NO prereq needed
    @Rule(Fact('EEE154', grade=L('N')))
    def do154(self):
        self.s.append('EEE154')
        self.SEPScore.append('EEE154')

        # UNIVERSITY CORE
        # Humanities

    @Rule(Fact('PHI104', grade=L('N')))
    def dophi(self):
        self.s.append('PHI104')
        self.UNIcore.append('PHI104')

        # UNIVERSITY CORE
        # Humanities

    @Rule(Fact('HIS102', grade=L('N')))
    def dohis102(self):
        self.s.append('HIS102')
        self.UNIcore.append('HIS102')

        # UNIVERSITY CORE
        # Humanities

    @Rule(Fact('HIS103', grade=L('N')))
    def dohis103(self):
        self.s.append('HIS103')
        self.UNIcore.append('HIS103')

        # UNIVERSITY CORE
        # Social Sciences

    @Rule(Fact('POL101', grade=L('N')))
    def dopol(self):
        self.s.append('POL101')
        self.UNIcore.append('POL101')


        # UNIVERSITY CORE
        # Social Sciences

    @Rule(Fact('ECO101', grade=L('N')))
    def doeco(self):
        self.s.append('ECO101')
        self.UNIcore.append('ECO101')



    @Rule(Fact('BIO103', grade=L('N')))
    def dobio(self):
        self.s.append('BIO103')
        self.UNIcore.append('BIO103')

        @Rule(Fact('BIO103', grade=L('N')))
        def dobio(self):
            self.s.append('BIO103L')
            self.UNIcore.append('BIO103L')
        # UNIVERSITY CORE
        # Social Sciences

    @Rule(Fact('ENV203', grade=L('N')))
    def doenv(self):
        self.s.append('ENV203')
        self.UNIcore.append('ENV203')

    @Rule(Fact('EEE452', grade=L('N')))
    def doeee452(self):
        self.s.append('EEE452')
        self.SEPScore.append('EEE452')

    # UNIVERSITY CORE
    #Languages

    @Rule(Fact('ENG102', grade=L('N')))
    def do102(self):
        self.s.append('ENG102')
        self.UNIcore.append('ENG102')

    # UNIVERSITY CORE
    # Languages

    @Rule(Fact('ENG102', grade=~L('F') & ~L('N')), Fact('ENG103', grade=L('N')))
    def do103(self):
        self.s.append('ENG103')
        self.UNIcore.append('ENG103')

    # UNIVERSITY CORE
    # Languages

    @Rule(Fact('ENG103', grade=~L('F') & ~L('N')), Fact('ENG111', grade=L('N')))
    def do111(self):
        self.s.append('ENG111')
        self.UNIcore.append('ENG111')

    # UNIVERSITY CORE
    # Languages

    @Rule(Fact('ENG103', grade=~L('F') & ~L('N')), Fact('BEN205', grade=L('N')))
    def doben(self):
        self.s.append('BEN205')
        self.UNIcore.append('BEN205')

    # CSE SECTIONS PREREQUISITES

    @Rule(Fact('CSE115', grade=L('N')))
    def do115(self):
        self.s.append('CSE115')
        self.SEPScore.append('CSE115')


    @Rule(Fact('CSE115', grade=~L('F') & ~L('N')), Fact('CSE173', grade=L('N')))
    def do173(self):
        self.s.append('CSE173')
        self.CSEcore.append('CSE173')

    @Rule(Fact('CSE173', grade=~L('F') & ~L('N')), Fact('CSE215', grade=L('N')))
    def do215(self):
        self.s.append('CSE215')
        self.CSEcore.append('CSE215')

    @Rule(Fact('CSE215', grade=~L('F') & ~L('N')), Fact('CSE225', grade=L('N')))
    def do225(self):
        self.s.append('CSE225')
        self.CSEcore.append('CSE225')


    @Rule(Fact('CSE215', grade=~L('F') & ~L('N')), Fact('CSE231', grade=L('N')))
    def do231(self):
        self.s.append('CSE231')
        self.CSEcore.append('CSE231')

    @Rule(Fact('CSE231', grade=~L('F') & ~L('N')), Fact('CSE332', grade=L('N')))
    def do332(self):
        self.s.append('CSE332')
        self.CSEcore.append('CSE332')

    '''
    @Rule(Fact('CSE225', grade=~L('F') & ~L('N') & ~L('D') & ~L('C-') & ~L('C')), Fact('CSE311', grade=L('N')))
    def do311(self):
        self.s.append('CSE311')
        self.CSEcore.append('CSE311')
'''

    @Rule(Fact('CSE225', grade=~L('F') & ~L('N')),
          Fact('MAT361', grade=~L('F') & ~L('N')),
          Fact('CSE373', grade=L('N')))
    def do373(self):
        self.s.append('CSE373')
        self.CSEcore.append('CSE373')

    @Rule(Fact('CSE332', grade=~L('F') & ~L('N')), Fact('CSE323', grade=L('N')))
    def do323(self):
        self.s.append('CSE323')
        self.CSEcore.append('CSE323')

    @Rule(Fact('CSE225', grade=~L('F') & ~L('N') ), Fact('CSE311', grade=L('N')))
    def do311(self):
        self.s.append('CSE311')
        self.CSEcore.append('CSE311')

    @Rule(Fact('CSE311', grade=~L('F') & ~L('N')), Fact('CSE327', grade=L('N')))
    def do327(self):
        self.s.append('CSE327')
        self.CSEcore.append('CSE327')

    @Rule(Fact('CSE323', grade=~L('F') & ~L('N')), Fact('CSE331', grade=L('N')))
    def do331(self):
        self.s.append('CSE331')
        self.CSEcore.append('CSE331')

    @Rule(Fact('CSE327', grade=~L('F') & ~L('N')), Fact('CSE425', grade=L('N')))
    def do425(self):
        self.s.append('CSE425')
        self.CSEcore.append('CSE425')

    # MATH SECTION PREREQUISITES
    @Rule(Fact('MAT116', grade=L('N') | L('F')))
    def do116(self):
        self.s.append('MAT116')
        self.SEPScore.append("MAT116")


    @Rule(Fact('MAT116', grade=~L('F') & ~L('N')), Fact('MAT120', grade=L('N')))
    def do120(self):
        self.s.append('MAT120')
        self.SEPScore.append("MAT120")

    @Rule(Fact('MAT116', grade=~L('F') & ~L('N')), Fact('MAT120', grade=L('N')))
    def do125(self):
        self.s.append('MAT125')
        self.SEPScore.append("MAT125")

    @Rule(Fact('MAT120', grade=~L('F') & ~L('N')), Fact('MAT130', grade=L('N')))
    def do130(self):
        self.s.append('MAT130')
        self.SEPScore.append("MAT130")

    @Rule(Fact('MAT130', grade=~L('F') & ~L('N')), Fact('MAT250', grade=L('N')))
    def do250(self):
        self.s.append('MAT250')
        self.SEPScore.append("MAT250")

    @Rule(Fact('MAT250', grade=~L('F') & ~L('N')), Fact('MAT350', grade=L('N')))
    def do350(self):
        self.s.append('MAT350')
        self.SEPScore.append("MAT350")

    @Rule(Fact('MAT250', grade=~L('F') & ~L('N')), Fact('MAT361', grade=L('N')))
    def do361(self):
        self.s.append('MAT361')
        self.SEPScore.append("MAT361")

    # Physics Part

    @Rule(Fact('MAT120', grade=~L('F') & ~L('N')), Fact('PHY107', grade=L('N')))
    def do107(self):
        self.s.append('PHY107')
        self.SEPScore.append("PHY107")

    @Rule(Fact('MAT120', grade=~L('F') & ~L('N')), Fact('PHY107L', grade=L('N')))
    def do107(self):
        self.s.append('PHY107L')
        self.SEPScore.append("PHY107L")

    @Rule(Fact('MAT130', grade=~L('F') & ~L('N')),
          Fact('PHY107', grade=~L('F') & ~L('N')),
          Fact('PHY107', grade=L('N')))
    def do108(self):
        self.s.append('PHY108')
        self.SEPScore.append("PHY108")

    @Rule(Fact('MAT130', grade=~L('F') & ~L('N')),
          Fact('PHY107', grade=~L('F') & ~L('N')),
          Fact('PHY107', grade=L('N')))
    def do108(self):
        self.s.append('PHY108L')
        self.SEPScore.append("PHY108L")

    # EEE Part

    @Rule(Fact('MAT120', grade=~L('F') & ~L('N')),
          Fact('PHY107', grade=~L('F') & ~L('N')),
          Fact('EEE141', grade=L('N')))
    def do141(self):
        self.s.append('EEE141')
        self.CSEcore.append('EEE141')

    @Rule(Fact('EEE141', grade=~L('F') & ~L('N')), Fact('EEE111', grade=L('N')))
    def doeee111(self):
        self.s.append('EEE111')
        self.CSEcore.append('EEE111')

    # others
    @Rule(Fact('MAT350', grade=~L('F') & ~L('N')), Fact('CHE101', grade=L('N')))
    def doche(self):
        self.s.append('CHE101')
        self.SEPScore.append("CHE101")

    @Rule(Fact('MAT350', grade=~L('F') & ~L('N')), Fact('CHE101', grade=L('N')))
    def doche(self):
        self.s.append('CHE101L')
        self.SEPScore.append("CHE101L")

    def listpass(self):
        return self.s

    def SEPScourses(self):
        return self.SEPScore
    def unicourses(self):
        return self.UNIcore
    def corecourses(self):
        return self.CSEcore