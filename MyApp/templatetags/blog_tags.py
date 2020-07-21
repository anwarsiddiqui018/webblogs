from django import template
from ..models import Post
from django.db.models import Count

register = 	template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_posts.html')

def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag

def get_most_commented_posts(count=2):
    post_objects_comment =  Post.objects.annotate(total_comments = Count('comments'))
# to find the number of comments we use annotate .annotate(var_name = Count('comments')
    return post_objects_comment.order_by('-total_comments')[:count]

