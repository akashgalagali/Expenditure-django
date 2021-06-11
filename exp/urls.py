from django.urls import path
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('addevent',views.addevent,name='addevent'),
    path('addnewevent',views.addnewevent,name='addnewevent'),
  ]