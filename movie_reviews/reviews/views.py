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
        # data=json.loads(request.body)  #when ever send the data in json format we have to use this
        data=request.POST # when we send data in form format  we have to use this
        rating_number=int(data.get('rating',0))
        rating_star="*"*rating_number
        movie=Movie_details.objects.create(
        movie_name=data.get('movie_name'),
        release_date=data.get('release_date'),
        budget=data.get('budget'),
        rating=rating_star
        )
        return JsonResponse({"status":"success","message":"inserting a record sccessfully",
                             "movie_name":movie.movie_name,"release_date":movie.release_date,"rating":movie.rating},status=200)
    # elif (request.method)=='GET':
        # ------method-1-------
        # results=list(Movie_details.objects.all().values())
        # print(results)
        # return JsonResponse({"status":"ok","data":results},status=200)
        # ------------method2------------

        # movie_info=Movie_details.objects.all()
        # movie_list=[]
        # for movie in movie_info:
        #     movie_list.append({
        #         "movie_name":movie.movie_name,
        #         "release_date":movie.release_date,
        #         "budget":movie.budget,
        #         "rating":movie.rating
        #     })
        # return JsonResponse ({"status":"success","data":movie_list},status=200)
    
        # # get movie datails in range of----rating more than 4
        # data=request.GET.get("rating")
        # ref_rating=int(data)
        # movies=Movie_details.objects.all()
        # result=[]
        # for movie in movies:
        #     if len(movie.rating)>ref_rating:
        #         result.append({
        #             "movie_name":movie.movie_name,
        #             "release_date":movie.release_date,
        #             "budget":movie.budget,
        #             "rating":movie.rating
        #         })
        # return JsonResponse({"status":"success","data":result},status=200)

    # get movie datails in  range of ---->more 25 cr and less than 45 cr
    elif (request.method)=='GET':


    # Read query params
        min_val = request.GET.get("min")
        max_val = request.GET.get("max")

        # Convert to float (if not provided, default)
        min_budget = float(min_val) 
        max_budget = float(max_val) 

        movies = Movie_details.objects.all()
        result = []

        for movie in movies:
            # Convert "400cr" → 400.0
            value = float(movie.budget.replace("cr", "").replace(" ", ""))

            # Check if within range
            if min_budget <= value <= max_budget:
                result.append({
                    "movie_name": movie.movie_name,
                    "budget": movie.budget,
                    "rating": movie.rating,
                    "release_date": movie.release_date
                })

        return JsonResponse({"movies": result})




        
        

    

    # elif (request.method)=='PUT':
    #     data=json.loads(request.body)
    #     ref_id=data.get("id")
    #     new_budget=data.get("budget")
    #     existing_movie=Movie_details.objects.get(id=ref_id)
    #     existing_movie.budget=new_budget
    #     existing_movie.save()
    #     updated_data=list(Movie_details.objects.filter(id=ref_id).values())
    #     return JsonResponse({"status":"data updated successfully","updated_data":updated_data},status=200)
    elif (request.method)=='PUT':
        data=json.loads(request.body)
        print("PUT data:",data) #check the incoming data
        ref_id=data.get("id")
        print("Reference ID:",ref_id)
        exiting_movie=Movie_details.objects.get(id=ref_id)
        print("Existing Movie:",exiting_movie) # check the exisiting movie object fetched from db
        if data.get("movie_name"):
            new_movie_name=data.get("movie_name")
            exiting_movie.movie_name=new_movie_name
            exiting_movie.save()
        elif data.get("release_date"):
            new_release_data=data.get("release_date")
            exiting_movie.release_date=new_release_data
            exiting_movie.save()
        elif data.get("budget"):
            new_budget=data.get("budget")
            exiting_movie.budget=new_budget
            exiting_movie.save()
        elif data.get("rating"):
            new_rating=data.get("rating")
            rating_star="*"*new_rating
            exiting_movie.rating=rating_star
            exiting_movie.save()
        return JsonResponse({"status":"success","message":"movie record updated successfully","data":data},status=200)



    
    elif(request.method)=='DELETE':
        data=json.loads(request.body)
        ref_id=data.get("id")
        get_deleting_data=list(Movie_details.objects.filter(id=ref_id).values())
        to_be_delete=Movie_details.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"req":"success","message":"movie record delete successfully","deleted data":get_deleting_data},status=200)

    return JsonResponse({"error":"error occured"},status=400)


# get movie datails in range of----rating more than 4
# get movie datails in  range of ---->more 25 cr and less than 45 cr


