from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='Main'),
    path('members/',views.members,name='members'),
    path('members/details/<int:id>',views.membersDitails,name='details'),
    path('test/',views.testing,name='test'),
]
