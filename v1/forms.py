from django import forms

'''
class RegisterForm(forms.Form):

    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':"form-control"}))
    last_name= forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':"form-control"}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    confirm_password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    address = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':"form-control"}))

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': "form-control"}))


class ComplaintForm(forms.Form):
    fullname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Full Name')
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Email Address')
    comment = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':"form-control"}), label='Comment')
'''


class RegistrationForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'University ID'}), label="University ID")
    fullname = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'type':'text','class':"form-control",'placeholder':'Fullname'}), label="Fullname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type':'text','class':"form-control",'placeholder':'Email ID'}), label="Email Address")
    password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type':'password','class':"form-control",'placeholder':'password'}))
    confirm_password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type':'password','class':"form-control",'placeholder':'password'}))

class LoginForm(forms.Form):
    user_id = forms.IntegerField(
        widget=forms.TextInput(attrs={'type':'int', 'class': "form-control", 'placeholder': 'University ID'}),
        label="University ID")
    password = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'type': 'password', 'class': "form-control", 'placeholder': 'password'}))

class GradeForm(forms.Form):

    c = [('1','A'),('2','A-'),('3','B+'),('4','B'),('5','B-'),('6','C+'),('7','C'),('8','C-'),('9','D') ]
    coursename = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'type':'text','class':"form-control",'placeholder':'Course Name'}), label='Course')
    coursegrade = forms.ChoiceField(choices=c,label='Grades',widget=forms.Select(attrs={'class':"form-control",'placeholder':'Course Grade'}))
    semester = forms.IntegerField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Semester number'}), label='Semester')





    '''first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=90)
    address = models.CharField(max_length=500)'''