from django import forms
from community.models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        
        model = Board
        CHOICES = (
            ('한국영화', '한국영화'),
            ('외국영화', '외국영화'),
            ('자유글', '자유글'),
        )


        fields = ['title', 'content_type', 'content', 'file_image']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content_type': forms.Select(attrs={'class': 'form-select'}, choices=CHOICES),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'file_image': forms.FileInput(attrs={'class': 'form-control'})

        }
        labels = {

            'title': '제목',
            'content_type': '머리글',
            'content': '내용',
            'file_image': '파일첨부'

        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(BoardForm, self).__init__(*args, **kwargs)
        



