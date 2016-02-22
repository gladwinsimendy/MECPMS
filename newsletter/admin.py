from django.contrib import admin
from .models import signup
from .models import sellerprofile
from .models import notifications,student_details,adminregister,Document
# Register your models here.
admin.site.register(signup)
admin.site.register(sellerprofile)
admin.site.register(notifications)
admin.site.register(student_details)
admin.site.register(adminregister)
admin.site.register(Document)
