
from django.urls import path
from notes.views import NoteListView, NoteCreateView, NotesUpdateView,DetailNoteAPIView

urlpatterns = [
    path('note/' ,NoteListView.as_view()),
    path('note-create/' , NoteCreateView.as_view()),
    path('note-update/<notes_id>/' ,NotesUpdateView.as_view()),
    path('note-detail/<str:slug>//' , DetailNoteAPIView.as_view()),
]
