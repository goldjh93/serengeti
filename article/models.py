from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
  author = models.ForeignKey(
    'user.User',
    on_delete=models.CASCADE,
  )

  title = models.TextField()
  content = models.TextField()

  created_at = models.DateTimeField(
    auto_now_add=True,
  )
  
  updated_at = models.DateTimeField(
    auto_now=True,
  )

  image = models.ImageField(upload_to='article/', null=True)


  def __str__(self):
    return self.title
  
  def summary(self):
    return self.content[:100]
  

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='article_comments')
    author = models.ForeignKey('user.User',on_delete=models.CASCADE, null=True, related_name='author_comment')
    like_user_comment = models.ManyToManyField('user.User', related_name='like_comment')

    class Meta:
        db_table = 'comment'
    
    def __str__(self):
        return self.content + ' | ' + str(self.author)+'|' +str(self.like_user_comment)
    
class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    like_users = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table ='like'
        
    def __str__(self):
        return self.article.title + ' | ' + str(self.like_users) 