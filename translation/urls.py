from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('languages', views.ViewsetsLanguages)
app_name='translation'
urlpatterns = [
      path('', views.mixins_list.as_view()),
      path('/', include(router.urls)),

]