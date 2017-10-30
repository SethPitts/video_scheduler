from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import VideoForm
from .models import Video


# Create your views here.

def index(request):
    return render(request, 'video_scheduler/index.html', context={})


def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video_title = form.cleaned_data['video_title']
            video_description = form.cleaned_data['video_description']
            video_length = form.cleaned_data['video_length']
            video = Video(video_title, video_length, video_description)
            video.save()
            print("in post")
            return HttpResponseRedirect('/video_scheduler/video_upload_successful/')
    else:
        print("in get")
        form = VideoForm()

    return render(request, 'video_scheduler/video_upload.html', {'form': form})


def video_upload_successful(request):
    return render(request, 'video_scheduler/video_upload_successful.html', dict())
