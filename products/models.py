from django.db import models
from django.utils import timezone
from .validators import validate_blocked_words
# Create your models here.

class ProductManager(models.Manager):
    # def published(self):
    #     now = timezone.now()
    #     return self.get_queryset().filter(state=Product.PUBLISHED, publish_timestamp__lte=now)

    def get_queryset(self):
        now = timezone.now()
        return super().get_queryset().filter(state=Product.PUBLISHED, publish_timestamp__lte=now)

class Product(models.Model):
    DRAFT = 'DR'
    PUBLISHED = 'PB'

    STATE_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    state = models.CharField(max_length=2,choices=STATE_CHOICES,default=DRAFT)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    publish_timestamp = models.DateTimeField(auto_now_add=False,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    objects = models.Manager()
    published = ProductManager()

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        validate_blocked_words(self.title)
        if self.is_published and self.publish_timestamp is None:
            self.publish_timestamp = timezone.now()
        else:
            self.publish_timestamp = None
        super().save(*args,**kwargs)

    @property
    def is_published(self):
        return self.state == self.PUBLISHED

