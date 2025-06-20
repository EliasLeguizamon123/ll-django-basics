from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.name"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    path('notes/<int:pk>/like', views.NotesLikeView.as_view(), name="notes.like"),
    path('notes/<int:pk>/change_visibility', views.NotesChangeVisibilityView.as_view(), name="notes.change_visibility"),
]