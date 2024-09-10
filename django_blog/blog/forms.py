from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only the content field is visible in the form
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
