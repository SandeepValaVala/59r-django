from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import uuid


# Create your views here.
def view1(request):
    print(request.method)
    return HttpResponse("hello world, i am from view1")
def view2(request):
    return HttpResponse("hello world, i am from view2")
def view3(request):
    return HttpResponse("hello world, i am from view3")
def view4(request):
    return JsonResponse({"name":"sandeep","message":"hello world!"})
def view5(requset):
    return JsonResponse({"status":"success","response":"welcome"})

def dynamicview(request):
    qp1=request.GET.get("name","world") #getting quey param from url
    return HttpResponse(f"hello {qp1}")

# json always allow object only

def personInfo(request):
    name=request.GET.get("name","sandeep")
    city=request.GET.get("city","hyd")
    role=request.GET.get("role","trainer")
    info={"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":info})

# send dynamic Jsonresponse of movie booking information by using query params movie,showtime,ticket_cost,no_of_tickets

def movieInfo(request):
    movie =request.GET.get("movie","Akhanda 2")
    showtime=request.GET.get("showyime","6am")
    ticket_cost=request.GET.get("ticket_cost",250)
    total_no_of_tickets=request.GET.get("total_no_of_tickets",500)
    total_price=request.GET.get("total_price",125000)
    info={"movie":movie,"showtime":showtime,"ticket_cost":ticket_cost,"total_no_of_tickets":total_no_of_tickets,"total_price":total_price}
    return JsonResponse({"status":"success","data":info})


def temp1(request):
    return render(request,"./simple.html")
def temp2(request):
    return render(request,"./second.html")
def temp3(request):
    return render(request,"./first.html")

def payment_api(request):
    orderid=request.GET.get("order")
    paymentmode=request.GET.get("payment")
    amount=request.GET.get("amount")
    transactionid = str(uuid.uuid4())
    
    info={"order_id":orderid,"payment_mode":paymentmode,"amount":amount,"Transaction_id":transactionid}
    return JsonResponse(info)


# products = [
#     {
#         "id": 1,
#         "name": "Wireless Mouse",
#         "category": "Electronics",
#         "price": 599,
#         "stock": 150,
#         "rating": 4.5
#     },
#     {
#         "id": 2,
#         "name": "Bluetooth Headphones",
#         "category": "Electronics",
#         "price": 1299,
#         "stock": 80,
#         "rating": 4.3
#     },
#     {
#         "id": 3,
#         "name": "Notebook",
#         "category": "Stationery",
#         "price": 120,
#         "stock": 300,
#         "rating": 4.1
#     },
#     {
#         "id": 4,
#         "name": "Water Bottle",
#         "category": "Home",
#         "price": 250,
#         "stock": 200,
#         "rating": 4.0
#     },
#     {
#         "id": 5,
#         "name": "Keyboard",
#         "category": "Electronics",
#         "price": 999,
#         "stock": 60,
#         "rating": 4.4
#     }
# ]


products = [
    {
        "id": 1,
        "title": "Wireless Mouse",
        "category": "Electronics",
        "description": "Ergonomic wireless mouse with adjustable DPI",
        "price": 599,
        "rating": 4.5,
        "stock": 120,
        "image": "wireless_mouse.jpg"
    },
    {
        "id": 2,
        "title": "Bluetooth Headphones",
        "category": "Electronics",
        "description": "Noise-cancelling over-ear Bluetooth headphones",
        "price": 1999,
        "rating": 4.3,
        "stock": 60,
        "image": "bluetooth_headphones.jpg"
    },
    {
        "id": 3,
        "title": "Men's Casual T-Shirt",
        "category": "Fashion",
        "description": "100% cotton round-neck t-shirt",
        "price": 499,
        "rating": 4.1,
        "stock": 200,
        "image": "mens_tshirt.jpg"
    },
    {
        "id": 4,
        "title": "Running Shoes",
        "category": "Footwear",
        "description": "Lightweight running shoes with cushioned sole",
        "price": 2499,
        "rating": 4.6,
        "stock": 75,
        "image": "running_shoes.jpg"
    },
    {
        "id": 5,
        "title": "Smart Watch",
        "category": "Electronics",
        "description": "Fitness tracking smart watch with heart rate monitor",
        "price": 3499,
        "rating": 4.4,
        "stock": 50,
        "image": "smart_watch.jpg"
    },
    {
        "id": 6,
        "title": "Backpack",
        "category": "Accessories",
        "description": "Water-resistant backpack with laptop compartment",
        "price": 1299,
        "rating": 4.2,
        "stock": 90,
        "image": "backpack.jpg"
    }
]


def productsByitem(request,category):
    filteredData = []
    
    for product in products:
        if product["category"].lower()==category.lower():
            filteredData.append(product)
    
    len(filteredData)
    if len(filteredData)>0:
      return JsonResponse({"data":filteredData,"message":"products records successfully fetched"},status=200)
    elif len(filteredData)==0:
      return JsonResponse({"data":filteredData,"message":"no content is available as per ur requirement"},status=404)
    else:
      return JsonResponse({"error":"something went wrong"})
    
    
    
# def productByrating(request,rating):
#   cnvfrt_rating = float(rating)
#   print(cnvfrt_rating)
#   filteredData = []
  
#   for product in products:
#     if product["rating"]>=cnvfrt_rating:
#       filteredData.append(product)
      
      
#     len(filteredData)
#     if len(filteredData)>0:
#       return JsonResponse({"data":filteredData,"message":"products records successfully fetched"},status=200)
#     elif len(filteredData)==0:
#       return JsonResponse({"data":filteredData,"message":"no content is available as per ur requirement"},status=404)
#     else:
#       return JsonResponse({"error":"something went wrong"})


def productByrating(request,rating):
    try:
        cnvrt_rating = float(rating)
        if request.method == 'GET':
            filteredData = []
            for product in products:
                if product["rating"] >= cnvrt_rating: #(<=)
                    filteredData.append(product)
            if len(filteredData) == 0:
                msg = "No products found"
            else:
                msg = "Products fetch successfully"
            return JsonResponse({"status":"success","message":msg,"total no.of records":len(filteredData),"data":filteredData})
        return JsonResponse({"status":"failure","message":msg})
    
    except Exception as e:
        return JsonResponse({"message":"Something went wrong"})



jobs = [ 
{"id": 1, "title": "Python Developer", "location": "Hyderabad", "experience": 2}, 
{"id": 2, "title": "Java Developer", "location": "Bangalore", "experience": 3}, 
{"id": 3, "title": "Frontend Developer", "location": "Hyderabad", "experience": 1}, 
{"id": 4, "title": "Data Analyst", "location": "Chennai", "experience": 2} 
]

def job(request):
    if request.method == 'GET':
        return JsonResponse({"jobs":jobs})

def jobId(request,id):
    try:
        if request.method == 'GET':
            filteredData = []
            for job in jobs:
                if job["id"] == id:
                    filteredData.append(job)
            if len(filteredData) != 0:
                return JsonResponse(filteredData[0])
                # return JsonResponse(job)
            return JsonResponse({"error":"Job not found"},status=404)
              
    except Exception as e:
        return JsonResponse({"message":"Something went wrong"})
    
    
def jobBylocation(request,location):
    try:
        if request.method == 'GET':
            filteredData = []
            for job in jobs:
                if job["location"].lower()==location.lower():
                    filteredData.append(job)
            if len(filteredData) > 0:
                return JsonResponse({"total no.of records":len(filteredData),"data":filteredData})
        return JsonResponse({"error": "No jobs found for this location"})
    
    except Exception as e:
        return JsonResponse({"message":"Something went wrong"})
    
    
# def jobId(request,id):
#     try:
#         if request.method == 'GET':
#             for job in jobs:
#                 if job["id"]==id:
#                     return JsonResponse(job)
#                 return JsonResponse({"error":"Job not found"})
              
#     except Exception as e:
#         return JsonResponse({"message":"Something went wrong"})