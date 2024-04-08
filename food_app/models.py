from django.db import models
from django.utils.text import slugify


class Food(models.Model):
    TYPES = [
        ('drinks', 'Beverages'),
        ('lunch', 'Lunch'),
        ('dinner', 'the evening'),
    ]

    food_type = models.CharField(max_length=20, choices=TYPES, verbose_name='type of food')

    name = models.CharField(max_length=20, verbose_name='food name')

    price = models.PositiveIntegerField(verbose_name='The price of food')

    descripion = models.TextField(verbose_name='Description of food')

    image = models.ImageField(upload_to='Foods', verbose_name='photo of food',
                              help_text='Images should be in 800x480 size')

    slug = models.SlugField(blank=True, unique=True, verbose_name='Aslag',
                            help_text='This field is filled automatically')

    update_at = models.DateTimeField(verbose_name='Update date', auto_now=True)
    date = models.DateTimeField(verbose_name='creation date', auto_now_add=True)

    situation = models.BooleanField(default=True, verbose_name='Availability of food')
    status = models.BooleanField(default=False, verbose_name='Condition', help_text='Publication status on the site')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Food, self).save()

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'foods'


class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='comments', verbose_name='Food',
                             help_text='Which food is the comment intended for?')

    name = models.CharField(max_length=20, verbose_name='first name and last name')

    email = models.EmailField(verbose_name='email', null=True)

    text = models.TextField(verbose_name='Comment text')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', verbose_name='Reply to the comment',
                               help_text='If this comment is in response to another comment, it will be completed', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'Comments'
