from django.urls import path, include

from users.views import Register

urlpatterns =[
    #home page
    path('', include('django.contrib.auth.urls')),
    
    #register
    path('register/', Register.as_view(), name='register'),

    


]