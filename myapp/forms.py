from django import forms

class AlignTextForm(forms.Form):
    uzbek_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        label="O'zbekcha Matn"
    )
    english_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        label="Inglizcha Matn"
    )
