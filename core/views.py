from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import *
from .models import *


# Create your views here.
def list_of_book_by_category(request, category_slug):
    categories = Book.objects.all()
    # print("Available books are {}".format(categories))
    post = Book.objects.filter()

    if category_slug:
        category_object = get_object_or_404(Category, slug=category_slug)
        post_category= post.filter(category_object)
        # print("Available books are {}".format(category_object))

    template = 'core/list_of_book_by_category.html'
    context = {'categories': categories,'post':post_category,'category': category_object}
    return render(request, template, context)


class Home(TemplateView):
    template_name = 'core/home_core.html'

@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
    return render(request, 'core/upload.html', context)

def book_detail(request, pk):
    books = get_object_or_404(Book, pk=pk)
    books.views = books.views + 1
    books.save()
    return render(request, 'core/book_detail.html', {'books': books})


def book_list(request):
    books = Book.objects.all()
    # template = 'core/book_list.html'
    template = 'core/book_list.html'
    # print ("Available books are {}".format(books))
    return render(request, template, {
        'books' : books
    })
@login_required
def book_list_genres(request,pk):
    books = Book.objects.filter(genres=pk)
    # print ("Available books are {}".format(books))
    return render(request, 'core/book_list_genres.html', {
        'books' : books
    })
@login_required
def add_comment_to_post(request, pk):
    books = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = books
            comment.save()
            return redirect('book_detail', pk=books.pk)
    else:
        form = CommentForm()
    return render(request, 'core/add_comment_to_post.html', {'form': form})

# def approved_comments(self):
#     return self.comments.filter(approved_comment=True)

def StockMarketBooks(request):
    posts = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'core/StockMarketBooks.html', {'posts': posts})

@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'core/upload_book.html', {
        'form' : form
    })
@login_required
def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'core/class_book_list.html'
    context_object_name = 'books'

class UploadBookView(CreateView):
    model = Book
    # form_class = BookForm
    fields = ('title', 'author', 'pdf', 'cover')
    success_url = reverse_lazy('class_book_list')
    template_name = 'core/upload_book.html'