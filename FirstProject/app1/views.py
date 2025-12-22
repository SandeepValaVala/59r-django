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

def payment_api(request):
    orderid=request.GET.get("order")
    paymentmode=request.GET.get("payment")
    amount=request.GET.get("amount")
    transactionid = str(uuid.uuid4())
    
    info={"order_id":orderid,"payment_mode":paymentmode,"amount":amount,"Transaction_id":transactionid}
    return JsonResponse(info)


products = [
    {
        "id": 1,
        "name": "Wireless Mouse",
        "category": "Electronics",
        "price": 599,
        "stock": 150,
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Bluetooth Headphones",
        "category": "Electronics",
        "price": 1299,
        "stock": 80,
        "rating": 4.3
    },
    {
        "id": 3,
        "name": "Notebook",
        "category": "Stationery",
        "price": 120,
        "stock": 300,
        "rating": 4.1
    },
    {
        "id": 4,
        "name": "Water Bottle",
        "category": "Home",
        "price": 250,
        "stock": 200,
        "rating": 4.0
    },
    {
        "id": 5,
        "name": "Keyboard",
        "category": "Electronics",
        "price": 999,
        "stock": 60,
        "rating": 4.4
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
    
    
    
def productByrating(request,rating):
  rating = float(rating)
  filteredData = []
  
  for product in products:
    if product["rating"]>=rating:
      filteredData.append(product)
      
      
    len(filteredData)
    if len(filteredData)>0:
      return JsonResponse({"data":filteredData,"message":"products records successfully fetched"},status=200)
    elif len(filteredData)==0:
      return JsonResponse({"data":filteredData,"message":"no content is available as per ur requirement"},status=404)
    else:
      return JsonResponse({"error":"something went wrong"})
