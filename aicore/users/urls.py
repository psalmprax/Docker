from django.urls import path

from aicore.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    test_view,    
)

app_name = "users"
urlpatterns = [
    path("test/", view=test_view, name="test"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
