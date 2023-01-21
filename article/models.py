from django.db import models

# Create your models here.

class Articles(models.Model):
    autor=models.ForeignKey("auth.user", on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık" )
    content= models.TextField(verbose_name="İçerik")
    created_date=models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_image=models.FileField(blank=True, null=True,verbose_name="Resim Ekle")
    
    def __str__(self):
        return self.title
    class Meta:
       ordering = ['-created_date']
    
class Comment(models.Model):
    article=models.ForeignKey(Articles,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_autor=models.CharField(max_length=50,verbose_name="isim")
    comment_content=models.CharField(max_length=200, verbose_name="yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
    
    
