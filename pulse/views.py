from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def details(request):
    return render(request, 'details.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the ContactMessage model
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            return JsonResponse({"success": "Your message has been sent. Thank you!"})
        else:
            return JsonResponse({"error": "Please correct the errors in the form."}, status=400)
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

