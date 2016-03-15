from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from .forms import SignUpForm ,approvalForm,FormsetForm,editform, UserForm,searchForm,approvalForm, sellerProfileForm,loginForm,NotificationForm,memberProfileForm,DocumentForm,pcForm
from .models import sellerprofile,notifications,student_details,Document
from django_tables2   import RequestConfig
from django.forms import formset_factory
from .tables  import PersonTable,NotifTable,sellerTable
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.template.loader import get_template
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.
def home(request):
    details = []
    form = searchForm(request.POST or None)
    title = 'PMS'
    context={
        'form':form,
        'title':title,
        'details':details
    }
    if form.is_valid():
    	s_class = form.cleaned_data.get("batch")
        p_type = form.cleaned_data.get("p_type")
        p_title = form.cleaned_data.get("p_title")
        s=sellerprofile.objects.filter(Q(batch = s_class)&Q(ptype = p_type)&Q(project_title__contains=p_title)&Q(approved = "YES"))
        for each in s:
            l=[]
            print each.id
            l.extend([each.seller,each.batch,each.project_title,each.ptype,each.id])	
            details.append(l)
       
        return render(request,"home.html",context)

    return render(request,"home.html",context)

def searchpage(request,num):
	print num
	d = Document.objects.filter(Q(gpno = num)&Q(doc_title__contains='abstract'))
	p=sellerprofile.objects.get(id=num)
	s = student_details.objects.filter(group = p)
	return render(request,"commonresult.html",{'d':d,'s':s,'title':p.project_title})
		
    


# request.GET or None
def contact(request):
    registered = False
    title = 'welcome'
    profile = student_details.objects.filter(group__pk=15)
    print profile
    for each in profile:
        print each.group.id
    user_form = UserForm(request.POST or None)
    profile_form = sellerProfileForm(request.POST or None)
    
    context = {
      'userform':user_form,
      'profileform':profile_form,
      'title':title
      }

    if user_form.is_valid() and profile_form.is_valid():
        print int(request.POST['no_of_members'])+1
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        profile=profile_form.save(commit=False)
        profile.seller = user
        profile.save()
        print profile.id
        return HttpResponseRedirect('/memberregister/'+request.POST['no_of_members']+'/'+str(profile.id))
        # for form in member_form:
        #       member = form.save(commit=False)
        #       member.group =  profile
        #       member.save()
        
    return render(request,"contact.html",context)





def memberregister(request,num,num1):
    
    # ,initial={'batch': profile.batch}
    profile = sellerprofile.objects.get(id = num1)
    print profile.batch
    memberFormSet = formset_factory(memberProfileForm, extra=int(num))
    
    member_form = memberFormSet(request.POST or None)
        
     # for i in range(int(num))
     # , extra=int(num)
     # initial=[{'batch': profile.batch}]
    # member_form = memberFormSet(initial=[{'batch': profile.batch} for i in range(int(num))])
        
    title = "Add Members"
    context = {
      'memberform':member_form,
      'title':title
      }

    if member_form.is_valid():
        # p = sellerprofile.objects.filter(batch = profile.batch)
        for form in member_form:
            member = form.save(commit=False)
            member.group =  profile
            member.save()

            

        
        messages.success(request, 'Profile details updated.')
        title = "Your Response Has been Recorded" 
        return HttpResponseRedirect('/login/')
        # return render(request,"memberregister.html",{'messages':messages})
    return render(request,"memberregister.html",context)       

def search(request):
    table = PersonTable(project.objects.all())
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    return render(request, "search.html", {'table': table})

def myview(request):
    if request.method == 'POST':
    	print request.POST.get('extra_field_count')
        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            print "valid!"
    else:
        form = MyForm()
    return render(request, "test1.html", { 'form': form })

def pclogin(request):
    login_form = loginForm(request.POST or None)
    title='PCLogin'
    context = {
     'form':login_form,
     'title':title
    }
    if login_form.is_valid():
        usern = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(username=usern, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_staff:
                    return HttpResponseRedirect('/pclogin/pcview')
                title='Unauthorised login'
                context = {
                'title':title
                } 
            else:
                context = {'title':'Account is currently disabled'} 

        else:
            messages.warning(request, 'Username and Password mismatch')
            context = {'form':login_form,'title':title}
                           

            
    return render(request,"login.html",context)

def sellerlogin(request):
    login_form = loginForm(request.POST or None)
    title='Login'
    context = {
     'form':login_form,
     'title':title
    }
    if login_form.is_valid():
        usern = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(username=usern, password=password)
        
        if user is not None:

            if user.is_active:
                
                login(request, user)
                #print {{ser.username}}
                
                if user.is_superuser:
                    return HttpResponseRedirect('/login/admin/'+usern+'/')
                return HttpResponseRedirect('/login/'+usern+'/')    
                user=User.objects.get(username=usern)
                table= NotifTable(notifications.objects.filter(idno=user.sellerprofile.id))
                RequestConfig(request,paginate={"per_page": 25}).configure(table)
                table1= NotifTable(notifications.objects.filter(category='public'))
                RequestConfig(request,paginate={"per_page": 25}).configure(table)
                return render(request, "loggedin.html", {'table': table,'table1':table1})

        		#print sellerprofile.seller.Username
        		#print s.id
        		#return render(request, "loggedin.html", {})
            else:
        	    context = {'title':'Account is currently disabled'}

        else:
            messages.warning(request, 'Username and Password mismatch')
            context = {'form':login_form,'title':title}

    return render(request,"login.html",context)


def loggout(request):
	logout(request)
	context = {'title':'logging you out'}
	return HttpResponseRedirect('/')

def notify(request,num):
    details=[]
    form = NotificationForm(request.POST or None)
    p=sellerprofile.objects.get(id = num)
    print p.approved
    if request.method == 'POST':
        appform = approvalForm(request.POST,initial={'approved': p.approved})
    else:
        appform = approvalForm(initial={'approved': p.approved})
    # p=sellerprofile.objects.get(id = num)
    print p.seller.username
    d = Document.objects.filter(gpno = num)
    try:
     s = student_details.objects.filter(group=p)
     for sh in s:     
     	l=[]
        l.extend([sh.name,sh.rollno,sh.email])	
        details.append(l)
        print details
    except student_details.DoesNotExist:
     s = None
    context={
        'form':form,
        'appform':appform,
        'details':details,
        'documents':d
    }
    if form.is_valid() and appform.is_valid():
    	
    	# s=sellerprofile.objects.filter(id=num)
    	# print s
        a = appform.cleaned_data.get("approved")
        print a
    	instance = form.save(commit=False)
    	instance.idno = num
        instance.batch = p.batch
    	instance.save()
        # app = appform.save(commit=False)
        p.approved = a
        p.save()
        # app.save()
    	form = NotificationForm()
        messages.success(request, 'Notification successfully sent.')
        return HttpResponseRedirect('../')
        # appform = approvalForm()
    	context={
        'form':form,
        'appform':appform,
        'details':details,
        'documents':d
        }
    return render(request, "notify.html", context)

def userpage(request,username):
    user=User.objects.get(username=username)
    print user.sellerprofile.batch
    table= notifications.objects.filter(idno=user.sellerprofile.id).only('notification','time_stamp')
    table1 = notifications.objects.filter(Q(category='public')&Q(batch = user.sellerprofile.batch)).only('notification','time_stamp')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            print request.POST['doc_title']
            user=User.objects.get(username=username)
            print user.sellerprofile.id
            print 'hellloooo'
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.gpno = user.sellerprofile.id
            newdoc.doc_title = request.POST['doc_title']
            newdoc.save()
            
            
            # Redirect to the document list after POST
            # return HttpResponseRedirect(reverse('newsletter.views.userpage'))
    else:
        form = DocumentForm() # A empty, unbound form
    documents = Document.objects.filter(gpno=user.sellerprofile.id)
    print documents
    return render(request, "loggedin.html", {'table': table,'table1':table1,'form':form,'documents':documents})

def adminpage(request,username):
    user=User.objects.get(username=username)
    batch = user.adminregister.Managing_class
    p_type = user.adminregister.project_type
    print batch
    print p_type 
    
    # try:
    #  s = sellerprofile.objects.get(batch = batch)
    # except sellerprofile.DoesNotExist:
    #  s = None 
    table = PersonTable(sellerprofile.objects.filter(Q(batch = batch)&Q(ptype = p_type)))
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    notform = NotificationForm(request.POST or None)
    if notform.is_valid():
        print 'hai'
        instance = notform.save(commit=False)
        instance.category='public'
        instance.batch = batch
        instance.save()
        notform = NotificationForm()
        messages.success(request, 'Notification successfully sent.')
        return render(request, "loggedin.html", {'table': table,'form':notform})

    return render(request, "loggedin.html", {'table': table,'form':notform})


def delete(request,num):
    print num
    name = sellerprofile.objects.get(id = num)
    print name.seller.username
    if request.method != 'POST':
        raise Http404
    docId = request.POST.get('docfile', None)
    print docId
    docToDel = get_object_or_404(Document, pk = docId)
    print docToDel.gpno
    docToDel.docfile.delete()
    docToDel.delete()
   
    # return render(request,"delete.html",{'title':'Deleted'})
    return HttpResponseRedirect('/login/'+name.seller.username+'/')

def pcview(request):
    # print num
    f=0
    form = pcForm(request.POST or None)
    title = 'Placement Cell'
    context={
        'form':form,
        'title':title
    }
    if form.is_valid():
        s_class = form.cleaned_data.get("batch")
        p_type = form.cleaned_data.get("p_type")
        
        rollno = form.cleaned_data.get("roll_no")
        mini=sellerprofile.objects.filter(Q(batch = s_class)&Q(ptype = 'MINI'))
        main = sellerprofile.objects.filter(Q(batch = s_class)&Q(ptype = 'MAIN'))

        for each in main:
            s = student_details.objects.filter(Q(group=each) & Q(rollno = rollno))
            if len(s) == 1:
                f = 1
            for e in s:
                titlemain = e.group.project_title
                d1 = Document.objects.filter(gpno = e.group.id)
                s1 = student_details.objects.filter(group=e.group.id)

                

        for each in mini:
            s = student_details.objects.filter(Q(group=each) & Q(rollno = rollno))
            if len(s) == 1:
                f = 1
            for e in s:
                titlemini = e.group.project_title
                d = Document.objects.filter(gpno = e.group.id)
                s = student_details.objects.filter(group=e.group.id)
        if f==0:
            messages.warning(request, 'Not a valid combination')       

        return render(request,"searchresult.html",{'d':d,'s':s,'titlemini':titlemini,'d1':d1,'s1':s1,'titlemain':titlemain})
        
        	# else:
        	# 	return render(request,"error.html",{'title':'Not a valid combination'})


        		# seller = sellerprofile.objects.filter(id = e.group)
        		# print seller.id

        # s = student_details.objects.all()

    return render(request,"placement.html",context)



def config(request,username):
    print username
    user=User.objects.get(username=username)
    p = sellerprofile.objects.get(id = user.sellerprofile.id)
    print p.project_title
    s = student_details.objects.filter(group=p)
    for each in s:
        print each.id
    return render(request,"config.html",{'s':s})

def edit(request,username,num):
    print username,num
    
    # p = sellerprofile.objects.get(id = num)
    s = student_details.objects.get(id=num)
    if request.method == 'POST':
        form = editform(request.POST ,initial={'name': s.name,'rollno':s.rollno,'email':s.email})
    else:
        form = editform(initial={'name': s.name,'rollno':s.rollno,'email':s.email})

    if form.is_valid():
        name = form.cleaned_data.get("name")
        rollno = form.cleaned_data.get("rollno")
        email = form.cleaned_data.get("email")
        s.name = name
        s.rollno = rollno
        s.email = email
        s.save()
        messages.success(request, 'Changes Updated successfully.')
        return HttpResponseRedirect('/login/'+username+'/config')

    return render(request,"edit.html",{'form':form})


def project_marks(request,num):
    details = []
            # s.marks_obtained = requ
    if request.method == 'GET':
        for key in request.GET:
            print int(key)
            s = student_details.objects.get(id = key)
            print request.GET[key]
            s.marks_obtained = request.GET[key]
            s.save()
            messages.success(request, 'Marks successfully updated.')
            return HttpResponseRedirect('../')
    p=sellerprofile.objects.get(id = num)
    try:
     s = student_details.objects.filter(group=p)
    except student_details.DoesNotExist:
     s = None

    return render(request,"marks.html",{'s':s})













# def test(request):
#     table= PersonTable(project.objects.filter(member_names='drone'))
#     RequestConfig(request,paginate={"per_page": 25}).configure(table)
#     return render(request, "test.html", {'table': table})

# def test(request):
# 	title = 'welcome'
# 	form = ContactForm(request.POST or None)
# 	context = {
# 	  'form':form,
# 	  'title':title
# 	}
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		print instance.member_names
# 		name=instance.member_names
# 		table= PersonTable(project.objects.filter(member_names=name))
# 		RequestConfig(request,paginate={"per_page": 25}).configure(table)
# 		context = {'table' : table}
# 	return render(request,"test.html",context)
	
