from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """ Uses django forms to create a from from the Post model class """

    class Meta:
        # This meta class is what tells django what fields to include from 
        # the Post model class
        model = Post
        fields = ('title', 'text')