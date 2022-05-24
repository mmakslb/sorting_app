from django import forms


class SortForm(forms.Form):
    input_array = forms.FileField()
    algorithm_type = forms.ChoiceField(widget=forms.Select(), choices=([('Bubble', 'Bubble'),
                                                                        ('Insertion', 'Insertion'),
                                                                        ('Merge', 'Merge')]))

    def __init__(self, *args, **kwargs):
        super(SortForm, self).__init__(*args, **kwargs)
        self.fields['algorithm_type'].label = 'Choose algorithm type'
        self.fields['input_array'].label = 'Upload .txt file with unsorted integers(Split integers by spaces)'
