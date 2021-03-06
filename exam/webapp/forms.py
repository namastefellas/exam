from django import forms

from webapp.models import GuestBook


class GuestBookForm(forms.ModelForm):

    class Meta:
        model = GuestBook
        fields = ('user_name', 'user_email', 'user_text')

