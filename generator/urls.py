from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.index,
        name="index"
    ),

    path(
        "generate/",
        views.generate_world,
        name="generate_world"
    ),
]