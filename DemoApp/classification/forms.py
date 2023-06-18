from django import forms
from .models import Prediction


class PredictionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PredictionForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Prediction
        exclude = ("predicted_value", "likelihood_indoor", "likelihood_outdoor")