from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.
def getquote(request):
        return render(request,'getinstantquote.html')#It returns the front page
def upload(request):
    if request.method=="POST":
        if len(request.FILES)!=0:
            file = request.FILES['Upload 3D file']#getting the uploaded file
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)  #saving the file to the media folder which is declared in the settings.py
            messages.success(request,'File '+filename+' Uploaded Succesfuly.')
            print(filename)
            return render(request,'upload.html')
        else:
            messages.error(request, 'File Upload Failed.')
            return render(request, 'upload.html')
    else:
        return render(request,'upload.html')