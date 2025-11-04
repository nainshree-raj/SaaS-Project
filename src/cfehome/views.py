from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir= pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args,  **kwargs):
    #queryset = PageVisit.objects.all()
    queryset = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title" : my_title,
        "page_visit_count" : queryset.count()
    }
    path = request.path
    print(path)
    html_template ="home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template,my_context)
    

def my_old_home_page_view (request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title" : my_title
    }
    html_ = """
    <!DOCTYPE html>
<html>
<body>
        <h1>
            {page_title} anything?
        </h1>
</body>
</html>
""".format(**my_context)
    return HttpResponse(html_)
