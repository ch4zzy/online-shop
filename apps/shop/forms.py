from django import forms

# Local
from apps.shop.models import Comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
