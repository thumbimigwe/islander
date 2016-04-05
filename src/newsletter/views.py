from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.
def home(request):
    title = 'Sign Up Now'

# add A Form
    form = SignUpForm()
    context = {
        "title": title,
        "form": form
    }
    return render(request, "home.html", context)
