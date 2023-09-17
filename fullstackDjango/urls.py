from django.contrib import admin
from django.urls import path,include

# urls are used to trigger views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('base.urls')),

]
