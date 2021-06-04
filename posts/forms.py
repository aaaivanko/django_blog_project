from django import forms


class ContactForm(forms.Form):
    '''This form will allow users to send messages on admin email'''
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

