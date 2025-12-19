from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    """
    Renders the About Page
    """

    if request.method == "POST":
        collaborate_form_result = CollaborateForm(data=request.POST)
        if collaborate_form_result.is_valid():
            collaborate_form_result.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your Collaboration request has been sent'
            )

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()



    return render(
        request,
        "about/about.html",
        {"about": about,
         'collaborate_form': collaborate_form},
    )