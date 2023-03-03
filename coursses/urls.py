from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('languages', views.ViewsetsLanguages)
app_name='Coursses'
urlpatterns = [
    path('',views.Coursees_List.as_view())
      
]