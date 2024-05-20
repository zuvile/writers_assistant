from .models import Novel
from django.shortcuts import get_object_or_404, render
from .forms import UploadFileForm
from .upload_processor import handle_uploaded_file
from django.http import HttpResponseRedirect


def index(request):
    novel_list = Novel.objects.all()
    return render(request, "assistant/index.html", {"novel_list": novel_list})


def novel(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    return render(request, "assistant/novel.html", {"novel": novel})


def success(request):
    return render(request, "assistant/success.html")


def upload_novel(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("success")
    else:
        form = UploadFileForm()
    return render(request, "assistant/upload.html", {"form": form})



