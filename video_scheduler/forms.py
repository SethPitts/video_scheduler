from django import forms

class VideoForm(forms.Form):
    video_title = forms.CharField(label="video_title", max_length=100)
    video_length = forms.CharField(label="video_length", max_length=100)
    video_description = forms.CharField(label="video_description", max_length=100)