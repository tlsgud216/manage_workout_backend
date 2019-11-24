from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^v1/function-name$', FunctionName.as_view(), name='FunctionName'),
]