from django.views.generic import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student

