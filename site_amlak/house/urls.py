from django.urls import path
from . import views


app_name="house"

urlpatterns = [
    path("",views.House_list,name="house_list"),
    path("about/",views.about,name="about"),
    path("search",views.search,name="search"),
    path("house_list/",views.House_total_list,name="house_total_list"),
    path("<int:id>/",views.House_detail,name="house_detail"),
    
]

