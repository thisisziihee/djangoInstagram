from django.urls import path
from apis.views import (
    UserCreateView, UserLoginView, UserLogoutView, ContentCreateView, UserInfoGetView, RelationCreateView, RelationDeleteView )



urlpatterns = [
    path('user/create/',UserCreateView.as_view(), name = "apis_user_create"),
    path('user/login/',UserLoginView.as_view(), name = "apis_user_login"),
    path('user/logout/',UserLogoutView.as_view(), name = "apis_user_logout"),

    path('content/create/', ContentCreateView.as_view(), name = "apis_content_create"),
    path('user/infoget/', UserInfoGetView.as_view(), name = 'apis_user_infoget'),

    path('relation/create', RelationCreateView.as_view(), name = "apis_relation_create"),
    path('relation/delete', RelationDeleteView.as_view(), name = "apis_relation_delete"),
]