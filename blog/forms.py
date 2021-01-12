from django import forms
from blog.models  import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ("title","body","img")
        widgets = {
            'title':forms.TextInput(attrs={'class':'editable'}),
            'body':forms.Textarea(attrs={'class':'editable medium-editor-textarea','cols': 100, 'rows': 20}),
        } 
    
    

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text' :forms.Textarea(attrs={'class':'editable medium-editor-textarea','cols': 100, 'rows': 20}),
        } 


    