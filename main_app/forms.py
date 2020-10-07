from django.forms import ModelForm
from .models import Grading

class GradingForm(ModelForm):
   class Meta:
      model = Grading
      fields = ['letter','number','company']