#sagar mhaske
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapp.serilizer import Userdataseriliazer
from restapp.models import Userdata

# Create your views here.
@api_view(['POST'])
def add(request):

   seriliazer=Userdataseriliazer(data=request.data)
   if seriliazer.is_valid():

      seriliazer.save()
   return Response(seriliazer.data)

@api_view(["GET"])
def view(request,name):
   userfromclient=Userdata.objects.get(name=name)
   seriliazer=Userdataseriliazer(userfromclient)
   return Response(seriliazer.data)

@api_view(["PUT"])
def update(request):
   userfromclient=request.data
   userfromdb=Userdata.objects.get(name=userfromclient['name'])
   seriliazer=Userdataseriliazer(userfromdb,data=userfromclient,partial=False)
   if seriliazer.is_valid():
      seriliazer.save()
   return Response(seriliazer.data)

@api_view(["DELETE"])
def delete(request,name):
   Userdata.objects.filter(name=name).delete()
   return Response("data deleted")