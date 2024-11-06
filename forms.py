from django import forms

class EmailForm(forms.Form):
    to = forms.EmailField(label='To')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    attachments = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), label='Attachments', required=False)
