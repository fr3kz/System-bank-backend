from django import forms


class MakeTransferForm(forms.Form):
    sender = forms.IntegerField()
    receiver = forms.IntegerField()
    amount = forms.CharField()
    title = forms.CharField(max_length=100)