from calendars.models import Calendar
from django.contrib import admin

# Register your models here.
class CalendarAdmin(admin.ModelAdmin):
	"""fieldsets = [
		(None,{'fields':['question']}),
		('Date Information',{'fields':['pub_date'],'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]"""
	list_display = ('group_match', 'name_match')

admin.site.register(Calendar,CalendarAdmin)

