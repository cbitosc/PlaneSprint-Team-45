from django.urls import path
from . import views
urlpatterns=[
    path('',views.signup,name='register'),
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('detail/<str:pk>',views.detail,name='detail'),
    path('explores/<str:pk>',views.explore,name='explore'),
    path('book',views.bookh,name='bookh')
]