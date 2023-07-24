# from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import NotesSerializer,NoteDetailSerializer

from .models import Notes,Category
from rest_framework.permissions import IsAuthenticated
from .mypagination import MyPageNumberPagination

from rest_framework.filters import SearchFilter
# Create your views here.


class NoteListView(generics.ListAPIView ):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    pagination_class = MyPageNumberPagination
    permission_classes = [IsAuthenticated]
   
    # filter_backends =[SearchFilter]
    # search_fields = ['title']




# class NoteCreateView(generics.CreateAPIView):
#     serializer_class = NotesSerializer
#     # permission_classes = [IsAuthenticated]


class NotesUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='notes_id'




class NoteCreateView(generics.CreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            note=serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DetailNoteAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Notes.objects.all()
    lookup_field = "slug"
    serializer_class = NoteDetailSerializer
    permission_classes = [IsAuthenticated]
