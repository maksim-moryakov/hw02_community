from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text')
        help_text = {
            'text': '*Введите текст поста',
            'group': 'Выберите группу, к которой будет относиться пост'
        }
