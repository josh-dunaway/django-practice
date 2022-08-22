from django.db import models

# Create your models here.
class Topic(models.Model):
    """The title or topic of the blog post. 
    Multiple entires can share a topic."""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the topic"""
        return self.text

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    """Entries related to a topic"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    headline = models.CharField(max_length = 255)
    body_text = models.TextField()
    # change this later to be set when user actually publishes
    pub_date = models.DateTimeField(auto_now_add=True)
    # change this later to be set when user EDITS
    mod_date = models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = 'entries'