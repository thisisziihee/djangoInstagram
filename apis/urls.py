from django.urls import path
from apis.views import (
    UserCreateView
)


urlpatterns = [
    path('apis/user/create/',UserCreateView.as_view(), name = "apis_user_create"),
]