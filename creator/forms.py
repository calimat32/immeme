from django import forms

class MacroForm(forms.Form):
    top_text = forms.CharField(max_length=155)
    bottom_text = forms.CharField(max_length=155)
