"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('', include(('core.urls','core'), namespace='core')),
    path('InternshipForm/',views.InternshipForm.as_view(), name="internshipForm",),
    path('OnlinecourseForm/',views.OnlinecourseForm.as_view(), name='onlinecourseForm'),
    path('ExpertTalkForm/',views.ExpertTalkForm.as_view(), name='expertTalkForm'),
    path('RegularForm/',views.RegularForm.as_view(), name='regularForm'),
    path('ContractForm/',views.ContractForm.as_view(), name='contractForm'),
    path('FacilityForm/',views.FacilityForm.as_view(), name='facilityForm'),
    path('MaintenanceForm/',views.MaintenanceForm.as_view(), name='maintenanceForm'),
]
