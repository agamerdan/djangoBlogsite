# Generated by Django 4.1.4 on 2023-01-14 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articles_article_image_alter_articles_autor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_autor', models.CharField(max_length=50, verbose_name='isim')),
                ('comment_content', models.CharField(max_length=200, verbose_name='yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.articles', verbose_name='Makale')),
            ],
        ),
    ]
