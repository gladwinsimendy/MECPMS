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
        help_text='max. 42 megabytes'
    )

class MyForm(forms.Form):
    original_field = forms.CharField()
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 3)

        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()


 
class pcForm(forms.Form):
    BATCH_CHOICES = (
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
    batch= forms.ChoiceField(choices = BATCH_CHOICES)
    p_type = forms.ChoiceField(choices = PROJECT_TYPE)
    roll_no = forms.IntegerField(required = True)

class searchForm(forms.Form):
    BATCH_CHOICES = (
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
    batch= forms.ChoiceField(choices = BATCH_CHOICES)
    p_type = forms.ChoiceField(choices = PROJECT_TYPE)
    p_title = forms.CharField(max_length = 30,required = False)

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