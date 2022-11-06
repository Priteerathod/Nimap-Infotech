from django.contrib import admin
from .views import *
from django.urls import path


urlpatterns = [
            path('',get_client),
            path('get-project/',get_project),
            path('create/',create_client),
            path('put-client/<id>',put_client),
            path('patch-client/<id>',patch_client),
            path('delete-client/<id>',delete_client)
]
