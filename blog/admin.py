from django.contrib import admin

from blog.models import Article, Author

admin.site.register(Article)
admin.site.register(Author)
