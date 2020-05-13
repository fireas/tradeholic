from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout
from .filers import BookFilter

from django.conf import settings
from django.http import Http404

from .models import Book
from.forms import AddForm

# Create your views here.
class FilteredListView(ListView):
    filterset_class = BookFilter

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context["filter"] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context

        
class HomeView(FilteredListView):
    model = Book
    paginate_by = 2
    template_name = "home.html"
    filterset_class = BookFilter
    


class BookDetailView(DetailView):
    model = Book
    template_name = "book.html"


def checkout_view(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request,'checkout.html',context)


def addBook_view(request):
    if not request.user.is_authenticated:
        raise Http404
    print(request.POST)
    if request.method == 'POST':
        print('aaaaaaaaaaaaaaaaaaaaaaaaa')
    form = AddForm(request.POST or None, request.FILES or None)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        print('*****************************************************************')
    context = {
        'form' : form
    }
    return render(request,'addbook.html',context)


def livre_view(request):
    if not request.user.is_authenticated:
        raise Http404
    print(request.POST,'**********')
    if request.method == 'POST':
        print('aaaaaaaaaaaaaaaaaaaaaaaaa')
    form = AddForm(request.POST or None, request.FILES or None)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        print('*****************************************************************')
        

    context = {
        'form' : form
    }
    return render(request,'l1.html',context)
