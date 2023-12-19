from django.contrib import admin
from vrm.models.center import School, Center, Holiday
from vrm.models.course import Course, Topic, Session
# Register your models here.


admin.site.register(School, admin.ModelAdmin)
admin.site.register(Center, admin.ModelAdmin)
admin.site.register(Holiday, admin.ModelAdmin)

admin.site.register(Course, admin.ModelAdmin)
admin.site.register(Topic, admin.ModelAdmin)
admin.site.register(Session, admin.ModelAdmin)