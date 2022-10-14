import django_filters
from .models import *

class blogFliter(django_filters.FilterSet):
    class Meta : 
        Model = Blog
        fields = ['categorie','title','published']