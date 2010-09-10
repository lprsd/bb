from django.db import models
from django.forms import ModelForm


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime = models.DateTimeField()

    class Meta():
        ordering = ('-datetime',)

    def __unicode__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField()
    
    def __unicode__(self):
        return self.text
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
