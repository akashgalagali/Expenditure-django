from django.urls import path
from . import views
urlpatterns = [
    path('oweDashboard',views.oweDashboard,name='oweDashboard'),
    path('oweMoney',views.oweMoney,name='oweMoney'),
    path('oweNewMoney',views.oweNewMoney,name='oweNewMoney'),
    path('oweDelete/<int:id>',views.oweDelete,name='oweDelete'),
  ]