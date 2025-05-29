from django.urls import path
from .views import RegisterView, NoteListCreateView, NoteDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('notes/', NoteListCreateView.as_view(), name='notes'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]