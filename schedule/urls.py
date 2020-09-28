from django.urls import path,include
from .views import index,close,create,time_detail,enrollment,delete,content_detail,time_admin,content_admin,time_revise,content_revise

urlpatterns=[
    path('',index,name='index'),
    path('create/',create,name='create'),
    path('enrollment/<int:timeslot_id>/',enrollment,name='enrollment'),

    path('time_detail/<int:content_id>/',time_detail,name='time_detail'),
    path('content_detail/<int:content_id>/',content_detail,name='content_detail'),

    
    path('time_admin/<int:timeslot_id>/',time_admin,name='time_admin'),
    path('content_admin/<int:content_id>',content_admin,name='content_admin'),
    path('time_revise/<int:timeslot_id>/',time_revise,name='time_revise'),
    path('content_revise/<int:content_id>/',content_revise,name='content_revise'),

    path('delete/<int:timeslot_id>/',delete,name='delete'),
    path('close/<int:timeslot_id>/<int:content_id>/',close,name='close')
]