from django import forms


class MakeTransferForm(forms.Form):
    sender = forms.IntegerField()
    receiver = forms.IntegerField()
    amount = forms.IntegerField()
    title = forms.CharField(max_length=100)