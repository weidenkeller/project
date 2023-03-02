from django.urls import path
from main_page.views import *


urlpatterns = [
    path('', index, name='main_page'),
    path('news/<int:newsid>/', news),


]