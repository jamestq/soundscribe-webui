from django.urls import path
from . import views

from soundscribe_webui.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("", views.UserListView.as_view(), name="user-manage"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("update/<str:username>/", views.UserUpdateView.as_view(), name="user-update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
