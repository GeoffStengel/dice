from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePage, PetProfile, AboutPage, PrivacyPage, TermsPage
# Create your views here.

def home(request):
    # Fetch all HomePage objects
    all_banner_info = HomePage.objects.all()
    # Fetch all PetProfile objects
    all_pet_profiles = PetProfile.objects.all()
    # Fetch all PetProfile objects
    six_pet_prof = PetProfile.objects.all()[:8]
    # Fetch all PetProfile objects

    context = {
        'all': all_banner_info,
        'pets': all_pet_profiles,
        'six_pets': six_pet_prof
    }

    return render(request, 'home/index.html', context)


def pets(request):
    all_pet_profiles = PetProfile.objects.all()
    
    context = {
        'all_pets': all_pet_profiles
    }    
    
    return render(request, 'home/pets.html', context )


def about(request):
    #about_description = AboutPage.objects.all()
    about_page = AboutPage.objects.first()

    context = {
        'about_page': about_page

    }   

    return render(request, 'home/about.html', context )  


def contact(request):
    

    return render(request, 'home/contact.html')


def privacy(request):
    privacy_text = PrivacyPage.objects.first()

    context = {
        'privacy_text': privacy_text

    }

    return render(request, 'home/privacy.html', context)

def terms(request):
    terms_text = TermsPage.objects.first()

    context = {
        'terms_text': terms_text
    }

    return render(request, 'home/terms_of_use.html', context)
