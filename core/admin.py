from django.contrib import admin

# Register your models here.

from core.models import Semester1,Semester2,Semester3,Semester4,Semester5,Semester6,Semester7,Semester8,InternshipTable,OnlinecourseTable,BTechProgram,ExpertTalk,VisionMission,ContactInfo,RegularEmployee,ContractEmployee,Maintenance,Facility

admin.site.register(InternshipTable)
admin.site.register(OnlinecourseTable)
admin.site.register(Semester1)
admin.site.register(Semester2)
admin.site.register(Semester3)
admin.site.register(Semester4)
admin.site.register(Semester5)
admin.site.register(Semester6)
admin.site.register(Semester7)
admin.site.register(Semester8)
admin.site.register(BTechProgram)
admin.site.register(ExpertTalk)
admin.site.register(VisionMission)
admin.site.register(ContactInfo)
admin.site.register(RegularEmployee)
admin.site.register(ContractEmployee)
admin.site.register(Facility)
admin.site.register(Maintenance)
