from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    
    contacts=Contact.objects.all()
    
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            new_name=form.cleaned_data['name']
            new_email=form.cleaned_data['email']
            new_subject=form.cleaned_data['subject']
            new_content=form.cleaned_data['content']
        
            new_contact=Contact(name=new_name,email=new_email, content=new_content, subject=new_subject)
            new_contact.save()
            
    context={
        
    "contacts":contacts ,
    }
    
    return render(request,"contact/contact.html",context)