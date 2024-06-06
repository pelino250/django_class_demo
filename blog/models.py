from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.email


# president -- country : one-to-one
# author -- article: one-to-many
# movie -- actor: many-to-many

class Article(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='articles')  # author.articles

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
