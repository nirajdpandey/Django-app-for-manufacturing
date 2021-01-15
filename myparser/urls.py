from django.conf.urls import url
from .views import upload_file

urlpatterns = [
    url('', upload_file),
]
