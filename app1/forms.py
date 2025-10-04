from django import forms

class AddtaskForm(forms.Form):

    task=forms.CharField(label="Task description")
    date=forms.DateField(label="Deadline date")
