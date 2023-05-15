
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    
    path("admin/", admin.site.urls),

    path('', include('webapp.urls')),
]

admin.site.site_header = "ProbeQ Administrator"
admin.site.site_title = "CMS Admin"
admin.site.index_title = " You logged in as SuperUser"