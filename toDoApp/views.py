
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import TasksSerializer, RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        user = request.user
        tasks = ToDoList.objects.filter(user= user)
        serializer = TasksSerializer(tasks, many=True)

        return Response({
            "tasks" : serializer.data
        })
        
    
    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TaskListModifyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = get_object_or_404(ToDoList, id=pk, user=request.user)
            print("My View Task : ", task)

            serializer = TasksSerializer(task)
            return Response(serializer.data)
        except Exception as e:
                print("ERROR:", e)
                return Response({'details': "Invalid task"})
        

    def put(self, request, pk):
        task = get_object_or_404(ToDoList, id=pk, user=request.user)
        print("My Updation Task : ", task)

        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        task = get_object_or_404(ToDoList, id=pk, user=request.user)
        print("My Deletion Task : ", task)

        task.delete()
        return Response(status=204)


class RegisterView(APIView):
    
    def post(self, request):
        serializer = RegisterSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "User Creted Successfully.",
                "data": serializer.data
            })
        return Response(serializer.errors, )

    
class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            })
        
        return Response({
            'details': 'invalid cradentials.',
        }, status=401)