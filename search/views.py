from django.shortcuts import render
from django.db.models import Q
from MyApp.models import Post

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(text__icontains=query)
            results= Post.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'search/view.html', context)
        else:
            return render(request, 'search/view.html',{})
    else:
        return render(request, 'search/view.html', {} )