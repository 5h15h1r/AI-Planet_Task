
from rest_framework.response import Response
from rest_framework import status
from .models import Hackathon
from rest_framework.views import APIView
from .serializers import UserSerializer,HackathonSerializer, SubmissionSerializer, getHackathonSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes



class Home(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response("Home Page",status=status.HTTP_200_OK)

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Hackathons(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        hackathon = Hackathon.objects.all()
        serialzer = HackathonSerializer(hackathon,many=True)
        return Response(serialzer.data,status=status.HTTP_200_OK)
    
    
    def post(self,request):
        if not request.user.is_staff:
            return Response({"message":"You are not allowed to create Hackathon"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "title": request.data.get('title'),
            "description": request.data.get('description'),
            "hackathonImage":request.data.get('hackathonImage'),
            "typeofSubmission":request.data.get('typeofSubmission'),
            "start":request.data.get('start'),
            "end":request.data.get('end'),
            "reward":request.data.get('reward'),
        }
        serializer = HackathonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class register(APIView):
     def post(self, request,pk):
        hackathon = Hackathon.objects.get(id=pk)
        hackathon.participants.add(request.user)
        
        serializer = UserSerializer(hackathon.participants,many=True) 
        return Response(serializer.data ,status=status.HTTP_200_OK)
     
class Enrolled(APIView):
     permission_classes = [IsAuthenticated]
     def get(self,request):
       
        hackathons = Hackathon.objects.filter(participants__in=[request.user])
        serialzer = getHackathonSerializer(hackathons,many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
        

class submission(APIView):

    def post(self,request,pk):
        
        hackathon = Hackathon.objects.get(id=pk)   
        Enrolledhackathon = Hackathon.objects.get(participants__id=request.user.id,id=pk)
        if Enrolledhackathon is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        else:
            
            if hackathon.typeofSubmission == "link":
                context = {
                    "name": request.data.get("name")    ,
                    "summary": request.data.get("summary"),
                    "participant": request.user.id,
                    "hackathon": pk,
                    "urlSubmission": request.data.get("urlSubmission"),
                    }
            if hackathon.typeofSubmission == "image":
                context = {
                    "name": request.data.get("name")    ,
                    "summary": request.data.get("summary"),
                    "participant": request.user.id,
                    "hackathon": pk,
                    "imageSubmission": request.FILES.get("imageSubmission"),
                    }
                
            if hackathon.typeofSubmission == "file":
                context = {
                    "name": request.data.get("name")    ,
                    "summary": request.data.get("summary"),
                    "participant": request.user.id,
                    "hackathon": pk,
                    "fileSubmission": request.FILES.get("fileSubmission"),
                    }
        serializer = SubmissionSerializer(data=context)
        
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getSubmission(APIView):
    def get(self,request):
        user=request.user.id
        hackathons = Hackathon.objects.filter(participants=user, submission__participant=user)
        serialzer = getHackathonSerializer(hackathons, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
    