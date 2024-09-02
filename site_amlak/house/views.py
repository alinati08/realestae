from django.shortcuts import render
from .models import House , ContactAgent
from django.core.paginator import Paginator
from blog.models import Blog 
from agent.models import Agent
from .forms import ContactAgentForm
from django.contrib import messages


# Create your views here.

def House_list(request):
    house_list= House.objects.all()
    blog_list= Blog.objects.all()
    agent_list= Agent.objects.all()
    
    
    context={
        "houses" : house_list ,
        "blogs":blog_list,
        "agents":agent_list,
        
        }
    return render(request,"houses/index.html", context )

def House_total_list(request):
    houses= House.objects.all()
    paginator = Paginator(houses, 3)  # Show 3 house per page.
    page_number = request.GET.get("page") 
    house_list = paginator.get_page(page_number)
    
    context={
        "house_list":house_list
    }
    
    return render(request,"houses/house_total_list.html",context)
  
def House_detail(request,id):
    house=House.objects.get(id= id)
    contact_agent=ContactAgent.objects.all().filter(house=house,)
    agent=house.agent
    
    if request.method == "POST":
        form=ContactAgentForm(request.POST)
        if form.is_valid():
            new_name=form.cleaned_data['name']
            new_email=form.cleaned_data['email']
    
            new_message=form.cleaned_data['message']
        
            new_contact=ContactAgent( house=house,name=new_name,email=new_email, message=new_message,agent=agent)
            new_contact.save()
            messages.success(request, 'پیام شما ثبت شد ')
            
      
    context={
        "house" : house ,
        "contacts":contact_agent ,
        
        }
    
    return render(request,"houses/detail.html", context )
        
def search(request):
    if request.method == "GET" :
        q1=request.GET.get("search")
        q2=request.GET.get("select1")
        q3=request.GET.get("select2")
        q4=request.GET.get("select3")
        q5=request.GET.get("select4")
        q6=request.GET.get("select5")
 
    house_list= House.objects.filter(name__icontains=q1,house_statue__icontains=q2,address__icontains=q3 ,                                      
                                     room__icontains=q4,bathroom__icontains=q5,price__range=(q6,1000000000000))
        
    return render(request , "houses/house_total_list.html",{"house_list":house_list})
    
def about(request):
    
    agent_list= Agent.objects.all()
       
    context={
        
        "agents":agent_list,
        
        }
           
    return render(request,'houses/about.html', context )
    
  

