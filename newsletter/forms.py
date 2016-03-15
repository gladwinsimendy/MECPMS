from django.contrib.auth.models import User
from django import forms
from .models import signup, sellerprofile,notifications,student_details


class SignUpForm(forms.ModelForm):
    class Meta:
        model = signup
        fields=['full_name','email']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        print email
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please make sure you use your USC email.")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address")
        return email
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
		#write validation code.
        return full_name


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class sellerProfileForm(forms.ModelForm):
    class Meta:
        model = sellerprofile
        fields=['project_title','batch','ptype']

class memberProfileForm(forms.ModelForm):
    class Meta:
        model = student_details
        fields=['name','rollno','email']


    # def __init__(self, *args, **kwargs):
    #   self.user = kwargs.pop('user')  # cache the user object you pass in
    #   super(memberProfileForm, self).__init__(*args, **kwargs)
    #   print self.user
        

    


    # def clean(self):
    #     print self.num1
    #     cleaned_data = self.cleaned_data
    #     try:
    #         student_details.objects.get(rollno=cleaned_data['rollno'])
    #     except student_details.DoesNotExist:
    #         pass
    #     else:
    #         raise ValidationError('This combination already exists')

    #     # Always return cleaned_data
    #     return cleaned_data
    # def clean_rollno(self):
    #     rno = []
    #     rollno = self.cleaned_data.get("rollno")
    #     print str(rollno)+"test"
    #     p=sellerprofile.objects.all()
    #     # for each in p:
    #     #     a=each.member.all()
    #     #     for each in a:
    #     #         print each.batch
    #         # for e in each.member:
    #         #     print e.rollno
    #     s=student_details.objects.all()
    #     # for each in s:
    #     #     g=each.group.member.all()
    #     #     for each in g:
    #     #         print each.batch
    #     for each in s:
    #         rno.append(each.rollno)
    #     print rno
    #     return rollno


        

    

class loginForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(widget=forms.PasswordInput())

class NotificationForm(forms.ModelForm):
    class Meta:
        model = notifications
        fields=['notification']
        widgets = {
            'notification': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

class DocumentForm(forms.Form):
    # doc_title = forms.CharField(max_length = 30)
    docfile = forms.FileField(
        label='Select a file',
        help_text='Max. 10mb'
    )

 
class pcForm(forms.Form):
    BATCH_CHOICES = (
        ('CSA', 'CSA'),
        ('CSB', 'CSB'),
        ('ECA', 'ECA'),
        ('ECB', 'ECB'),
        ('EEE', 'EEE'),
        ('BME', 'BME'),
    )
    batch= forms.ChoiceField(choices = BATCH_CHOICES)
    roll_no = forms.IntegerField(required = True)

class searchForm(forms.Form):
    BATCH_CHOICES = (
        ('---', '---'),
        ('CSA', 'CSA'),
        ('CSB', 'CSB'),
        ('ECA', 'ECA'),
        ('ECB', 'ECB'),
        ('EEE', 'EEE'),
        ('BME', 'BME'),
    )
    PROJECT_TYPE = (
        ('MINI','MINIPROJECT'),
        ('MAIN','MAINPROJECT'),
    )
    p_title = forms.CharField(max_length = 30,required = False)
    batch= forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'this.form.submit();'}),choices = BATCH_CHOICES)
    p_type = forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'this.form.submit();'}),choices = PROJECT_TYPE)

class approvalForm(forms.ModelForm):
    class Meta:
        model = sellerprofile
        fields=['approved']

class editform(forms.ModelForm):
    class Meta:
        model = student_details
        fields = ['name','rollno','email']

class FormsetForm(forms.Form):
    delete= forms.BooleanField(required=False, initial=False)