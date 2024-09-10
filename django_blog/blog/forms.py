from django import forms
from .models import Comment
from taggit.forms import TagWidget 
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only the content field is visible in the form
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in the form
        widgets = {
            'tags': TagWidget(),  # Use TagWidget for better tag input
        }