from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page requested: Get Method is called !!")
    friends=['jayesh','arpit','aditiya']
    return JsonResponse(friends, safe=False)       