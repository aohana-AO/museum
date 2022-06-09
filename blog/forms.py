
from django import forms


class PostForm(forms.Form):
    title=forms.CharField(max_length=30,label='タイトル',widget=forms.Textarea(attrs={'cols': '180', 'rows': '1'}))
    image=forms.ImageField(label='イメージ画像',required=False)
    content=forms.CharField(label='内容',widget=forms.Textarea(attrs={'cols': '180', 'rows': '10'}))
