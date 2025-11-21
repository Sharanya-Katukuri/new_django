from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from  reviews.models import Movie_details


# Create your views here.

def greet(request):
    return HttpResponse("hello world")

@csrf_exempt
def movie_reviews(request):
    if (request.method)=='POST':
        data=json.loads(request.body)
        rating_number=int(data.get('rating',0))
        rating_star="*"*rating_number
        movie=Movie_details.objects.create(
        movie_name=data.get('movie_name'),
        realse_date=data.get('release_date'),
        budget=data.get('budget'),
        rating=rating_star
        )
        return JsonResponse({"status":"success","message":"inserting a record sccessfully",
                             "movie_name":movie.movie_name,"realse_date":movie.realse_date,"rating":movie.rating},status=200)
    return JsonResponse({"error":"error occured"},status=400)
        