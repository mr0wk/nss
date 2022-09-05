from django import forms

 
class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["departure_from"].label = "Wyjazd z"
        self.fields["arrival_at"].label = "Przyjazd do"
        self.fields["date"].label = "Data odjazdu"
        self.fields["time"].label = "Czas odjazdu"
        self.fields["reminder_time"].label = "Czas przypomnienia"

    departure_from = forms.CharField(widget=forms.TextInput(attrs={"class": "tags"}))
    arrival_at = forms.CharField(widget=forms.TextInput(attrs={"class": "tags"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"})) 
    time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    reminder_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))