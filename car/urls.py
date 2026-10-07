from django.urls import path

from car.views import car_list, car_detail

urlpatterns = [
    path("movies/", car_list, name="movie-list"),
    path("movies/<int:pk>/", car_detail, name="movie-detail"),
]

app_name = "car"
