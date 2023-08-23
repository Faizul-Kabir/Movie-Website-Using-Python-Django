from django.urls import path
from . import views


app_name='account'
urlpatterns = [
    path('signup/',views.signup_form,name="signup"),
    path('login/',views.login_form,name="login"),
    path('logout/',views.log_out,name="logout"),
    

]