from django.contrib import admin
from .models import *

#Student registration

admin.site.register(Student)

#Grades registration

admin.site.register(Grades)

#Courses registration

admin.site.register(Courses)

#Complain box Table registration

admin.site.register(ComplainBox)

# lost and found Table registration

admin.site.register(LostandFound)


admin.site.register(EvaluationScripts)