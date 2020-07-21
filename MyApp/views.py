from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import PostForm, PostDeleteForm, CommentForm
from django.shortcuts import redirect
from taggit.models import Tag
from django.db.models import Count

# Add a new post
@login_required
def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



# Edit the post
@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# Delete the post
@login_required()
def post_remove(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostDeleteForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('/')
    else:
        form = PostDeleteForm(instance=post)
    return render(request, 'blog/delete.html', {'form': form,'post': post,})


# Detail of a post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views = post.views + 1
    post.save()
    # List fo similar posts
    post_tags_pks = post.tags.values_list('pk', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_pks).exclude(pk=post.pk)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('same_tags','-published_date')[:4]   # annotate is used to find the number of tags
    context = {
        'similar_posts': similar_posts,
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

#List of the post
def post_list(request, tag_slug=None):
    queryset_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag =get_object_or_404(Tag, pk=tag_slug)
        queryset_list = queryset_list.filter(tags__in=[tag])
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains = query) |
            Q(text__icontains = query) |
            # Q(tags__icontains = query)
            Q(author__first_name__icontains = query)
        ).distinct()
    paginator = Paginator(queryset_list, 5)
    ()
    page = request.GET.get('page', 1)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        queryset = paginator.page(paginator.num_pages)

    context = {
        "posts": queryset,
        "tag": tag,

    }
    return render(request, 'blog/post_list.html', context)



# User Post List
def user_post_list(request, pk):
    user = get_object_or_404(User, username=pk)
    post = Post.objects.filter(author=user)

    return render(request, 'blog/user_post_list.html', {'post': post})



def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()


#Add a comment to the post
@login_required()
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})








# def post_view(request, pk):
#     post = Post.objects.get(pk=pk)
#     post.views = F('views') + 1
#     post.save()
#     print(post.cleaned_data)
#
#     return render(request, 'post_detail.html', {'post': post})


