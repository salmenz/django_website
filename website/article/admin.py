from django.contrib import admin
from .models import Article, Marque, Article_images

admin.site.register(Article)
admin.site.register(Article_images)
admin.site.register(Marque)