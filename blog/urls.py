from django.urls import path, include
from rest_framework import routers
from blog import views 

router = routers.DefaultRouter()
router.register(r'blog', views.BlogView, 'blog')  

urlpatterns = [
    path('', include(router.urls)),
   
]
