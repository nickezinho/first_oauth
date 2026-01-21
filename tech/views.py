from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def members(request):
    return render(request, 'members.html')



#from django.http import JsonResponse
#from decouple import config


#def debug_oauth(request):
#    return JsonResponse({
#        "CLIENT_ID": config("CLIENT_ID_GITHUB"),
#        "SECRET": config("SECRET_GITHUB"),
#    })
