from django import forms
from blog.models import PostModel

class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title','content']