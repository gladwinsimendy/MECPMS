import django_tables2 as tables
from .models import sellerprofile,notifications
from django.utils.safestring import mark_safe
from django.utils.html import escape

class PersonTable(tables.Table):
    action = tables.TemplateColumn('<a href="{{record.id}}">notify</a>')
    class Meta:
        model = sellerprofile
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

class NotifTable(tables.Table):
	class Meta:
		model = notifications
		attrs = {"class": "paleblue"}

class sellerTable(tables.Table):
	class Meta:
		model = sellerprofile
		attrs = {"class": "paleblue"}