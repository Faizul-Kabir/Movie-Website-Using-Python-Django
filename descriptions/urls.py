from django.urls import path
from . import views

app_name='descriptions'
urlpatterns = [
    path('',views.descriptions_list,name="list"),
    path('addmovie/',views.addmovie_form,name="addmovie"),
    path('<title>/',views.details,name="detail"),

]