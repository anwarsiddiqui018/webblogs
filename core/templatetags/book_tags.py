from django import template
from ..models import Book
from django.db.models import Count


register = template.Library()

@register.simple_tag
def total_book():
    return Book.objects.count()

@register.inclusion_tag('core/latest_books.html')
def show_latest_books(count=5):
    latest_books = Book.objects.order_by('-published_date')[:count]
    return {'latest_books': latest_books}


@register.simple_tag
def get_most_commented_posts(count=2):
    post_objects_comment =  Book.objects.annotate(total_comments = Count('comments'))
# to find the number of comments we use annotate .annotate(var_name = Count('comments')
    return post_objects_comment.order_by('-total_comments')[:count]
