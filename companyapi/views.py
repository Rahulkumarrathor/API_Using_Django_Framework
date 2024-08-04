from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("home page request")
    friends=[
        'Ankit',
        'Ravi',
        'Raj',

    ]
    return JsonResponse(friends, safe=False)