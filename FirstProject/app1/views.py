from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

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