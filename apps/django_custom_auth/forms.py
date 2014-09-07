from django import forms
from .models import User


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'newsletter_subscribed')

#    def save(self, user):
#        user.first_name = self.cleaned_data['first_name']
#        user.last_name = self.cleaned_data['last_name']
#        user.user_type = self.cleaned_data['user_type']
#        user.save()


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    newsletter_subscribed = forms.BooleanField(required=False, initial=True)
    agreement = forms.BooleanField(required=True, initial=False)

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.newsletter_subscribed = self.cleaned_data['newsletter_subscribed']
        #user.user_type = self.cleaned_data['user_type']
        user.save()

    def clean_agreement(self):
        data = self.cleaned_data['agreement']
        if not data:
            raise forms.ValidationError("You must accept the agreement")
        return data
