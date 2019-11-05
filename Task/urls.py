"""Task URL Configuration

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

from django.conf.urls.static import static
from django.views.generic import TemplateView

from Task import settings
from Task_app import views
from rest_framework import routers
from Task_app.views import Dataviewset#,Fileviewset
router=routers.DefaultRouter()
router.register('',Dataviewset)
#router.register('upload/',Fileviewset)
from Task_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s/',TemplateView.as_view(template_name='uploadfile.html')),
    path('save/',views.savefile),
    path('export/',views.export),
    path('getjson/',views.getjson),
    path('show/',views.show),
    #path('index/',views.import_xls_to_db),
    path('api/',include(router.urls)),
    # path('api/',include(router.urls))

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
