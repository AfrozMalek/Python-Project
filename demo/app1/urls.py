from django.urls import path
from app1.views import *
urlpatterns = [
    path('first/',first),
    path('login/',login,name='login1'),
    path('logout/',logout,name="logout1"),
    path('register/',register,name='register1'),
    path('table_all/',table_all),
    path('table_filter/',table_filter),
    path('table_get/',table_get),
    path("",index,name='index'),
    path('poduct-all/',productall,name='productall'),
    path('poduct-filter/<int:id>/',productcategorywise,name='productfilter1'),
    path('poduct-get/<int:id>/',singleproduct,name='productget1'),
    path('change-password',changepass,name='change'),
    path('contact/',contactus,name='contact1')
]