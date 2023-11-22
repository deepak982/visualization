from django.contrib import admin
from django.urls import path , include
from mainapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'data', DataViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('api/', include(router.urls)),
]
