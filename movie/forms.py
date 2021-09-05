from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'pub_date', 'running_time', 'description', 'poster']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'running_time' : forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'poster': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': '영화명',
            'director': '감독',
            'pub_date': '개봉일',
            'running_time': '상영시간(분)',
            'description': '영화소개',
            'poster': '포스터',
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(MovieForm, self).__init__(*args, **kwargs)

