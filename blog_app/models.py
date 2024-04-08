from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='title', unique=True)
    body = models.TextField(verbose_name='text')
    image = models.ImageField(verbose_name='blog image', upload_to='Blog',
                              help_text='The size of the images should be 470x570 pixels')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='grouping', related_name='blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='writer')
    tag = models.ManyToManyField('Tag', verbose_name='tags', related_name='tag')
    situation = models.BooleanField(verbose_name='publication status', default=False)
    created_at = models.DateField(verbose_name='creation date', auto_now_add=True)
    update = models.DateTimeField(verbose_name='Update history', auto_now=True)
    slug = models.SlugField(blank=True, verbose_name='aslag',
                            help_text='this field is filled automatically')

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Blog, self).save()

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='Category title', unique=True)
    slug = models.SlugField(blank=True, verbose_name='Aslag',
                            help_text='This field is filled automatically')
    date = models.DateTimeField(verbose_name='creation date', auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()
    class Meta:
        verbose_name = 'Grouping'
        verbose_name_plural = 'categories'



class Tag(models.Model):
    title = models.CharField(max_length=25, verbose_name='Title tag', unique=True)
    slug = models.SlugField(blank=True, unique=True, verbose_name='Aslag',
                            help_text='This field is filled automatically')
    date = models.DateTimeField(verbose_name='creation date', auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Tag, self).save()

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'Tags'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name='Article',
                             help_text='What article is the intended comment for?')
    name = models.CharField(max_length=20, verbose_name='first name and last name')
    email = models.EmailField(verbose_name='email', null=True)
    text = models.TextField(verbose_name='Comment text')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies',
                               verbose_name='Reply to the comment',
                               help_text='If this comment is in response to another comment, it will be completed',
                               null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'Comments'
