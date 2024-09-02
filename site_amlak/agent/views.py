from django.shortcuts import render
from .models import Agent
from house.models import House
from django.core.paginator import Paginator

# Create your views here.


def agent_list(request):
    agents= Agent.objects.all()
    paginator = Paginator(agents, 3)  # Show 3 house per page.
    page_number = request.GET.get("page") 
    agent_list = paginator.get_page(page_number)
    
    context={
        "agent_list":agent_list
    }
    
    return render(request,"agent/agent_list.html",context)



def agent_detail(request,id):
    agent=Agent.objects.get(id= id)
    house_list= House.objects.filter(agent=agent)
    
      
    context={
        "agent" : agent,
        "house_list" : house_list ,
        
        }
    
        
    
    return render(request,"agent/agent_detail.html", context )