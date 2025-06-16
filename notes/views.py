from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views import View
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = '/admin'
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
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
        note = get_object_or_404(Notes, pk=self.kwargs.get('pk'))
        user = self.request.user
        
        if note.public or (user.is_authenticated and note.user == user):
            return note
        
        raise Http404("This note is not available")
class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    
class NotesLikeView(View):
    def post(self, request, pk):
        if request.method == 'POST':
            note = get_object_or_404(Notes, pk=pk)
            note.likes += 1
            note.save()
            return HttpResponseRedirect(reverse('notes.name', args=(pk,)))
        raise Http404
    
class NotesChangeVisibilityView(View):
    def post(self, request, pk):
        if request.method == 'POST':
            note = get_object_or_404(Notes, pk=pk)
            note.public = not note.public
            note.save()
            return HttpResponseRedirect(reverse('notes.name', args=(pk,)))
        raise Http404