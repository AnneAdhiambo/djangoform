from django.conf import settings
from django.template.context_processors import static
from django.urls import path
from.import views

urlpatterns = [
        path('', views.home, name='home'),

]