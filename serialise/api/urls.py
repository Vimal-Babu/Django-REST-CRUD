from django.urls import path
from quickstart.views import index,person

urlpatterns = [
    path('index/', index,name = 'index' ),
    path('person/',person, name = 'person'),
]