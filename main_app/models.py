from django.db import models

class HomeSlider(models.Model):
    image = models.ImageField(upload_to='Slider', verbose_name='Slider Image',
                              help_text='Images should be 1920x1280 pixels in size')

    update_at = models.DateTimeField(verbose_name='Last Updated Date', auto_now=True)
    date = models.DateTimeField(verbose_name='Creation Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'

    def __str__(self):
        return 'Slider Image ' + str(self.id)

class Gallery(models.Model):
    image = models.ImageField(upload_to='Gallery', verbose_name='Gallery Image',
                              help_text='Images should be 1200x800 pixels in size')

    update_at = models.DateTimeField(verbose_name='Last Updated Date', auto_now=True)
    date = models.DateTimeField(verbose_name='Creation Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return 'Gallery Image ' + str(self.id)

class ContactUs(models.Model):
    name = models.CharField(max_length=30, verbose_name='Full Name')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=11, verbose_name='Phone Number')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(verbose_name='Creation Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
