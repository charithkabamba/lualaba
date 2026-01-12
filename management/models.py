from django.db import models

# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
    verbose_name = 'Carousel'
    verbose_name_plural = 'Carousels'
    
class CatService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    verbose_name = 'Category Service'
    verbose_name_plural = 'Category Services'

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(CatService, on_delete=models.CASCADE, related_name='services')
    icon = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
    verbose_name = 'Service'
    verbose_name_plural = 'Services'

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} - {self.subject}'
    
    class Meta:
        ordering = ['-created_at']
    verbose_name = 'Message'
    verbose_name_plural = 'Messages'