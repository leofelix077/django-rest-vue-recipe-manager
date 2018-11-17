from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token
from .views import AuthAPIView

urlpatterns = [

    url(r'^$', AuthAPIView.as_view()),
    url(r'^jwt/$', obtain_jwt_token),

]
