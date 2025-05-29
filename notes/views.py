from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer, RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()

    serializer_class = RegisterSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()

    serializer_class = NoteSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()

    serializer_class = NoteSerializer
    
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)