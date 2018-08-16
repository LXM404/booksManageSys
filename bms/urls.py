#coding=utf-8
from bms import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/', views.index_view),
    url(r'^index1/', views.index1_view),
    url(r'^login/', views.login_view),
    url(r'^uselect/', views.uselect_view),
    url(r'^user/', views.user_view),
    url(r'^borrow/', views.borrow_view),
    url(r'^query/', views.query_view),
    url(r'^query1/', views.query1_view),
    url(r'^register/', views.register_view),
    url(r'^addbook/', views.addbook_view),
    url(r'^usermanage/', views.usermanage_view),
    url(r'^stuindex/', views.stuindex_view),
    url(r'^stuuselect/', views.stuuselect_view),
    url(r'^stuindex1/', views.stuindex1_view),
    url(r'^stuquery/', views.stuquery_view),
    url(r'^stuquery1/', views.stuquery1_view),
    url(r'^stuuser/', views.stuuser_view),
    url(r'^stuborrow/', views.stuborrow_view),
    url(r'^stulogin/', views.stulogin_view),
    url(r'^sturegister/', views.sturegister_view),
]