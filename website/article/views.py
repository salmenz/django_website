from django.http import HttpResponse
from .models import Article
from django.template import loader


def index(request):
    articles = Article.objects.all()
    template = loader.get_template("article/index.html")
    context = {'articles':articles,}
    return HttpResponse(template.render(context, request))

 
def detail(request, article_id):
    return HttpResponse("<h2>Details for article id : " + str(article_id) + "<h2>")