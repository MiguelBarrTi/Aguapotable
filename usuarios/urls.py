from django.urls import path
from .views import login_view, panel_habitante

urlpatterns = [
    path("login/", login_view, name="login"),
    path("mi-cuenta/", panel_habitante, name="panel_habitante"),

]