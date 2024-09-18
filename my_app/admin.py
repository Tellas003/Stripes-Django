from django.contrib import admin

# Register your models here.
from my_app.models import Verification

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','courseName','participantName','courseDate1','courseDate2','passportNo','issueDate','certificateNumber')
admin.site.register(Verification, CategoryAdmin)



from my_app.models import Verification1
admin.site.register(Verification1)