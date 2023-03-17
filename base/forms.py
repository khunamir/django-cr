from base.models import Rental
from django.forms import ModelForm

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'