from django import forms
from .models import Feedback


# our new form
from django import forms


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'