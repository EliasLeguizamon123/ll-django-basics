from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import get_object_or_404
from .models import Notes
# Create your views here.
from .forms import NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    
class PopularNotesView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    
    def get_queryset(self):
        return Notes.objects.filter(likes__gte=1) # likes greater than or equal to 1 va con __ por que asi lo toma django
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'
    
    def get_object(self, queryset=None):
        return get_object_or_404(Notes, pk=self.kwargs.get('pk'))
    
class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'