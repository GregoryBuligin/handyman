from django.db import models
from category.models import Category

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    discription = models.TextField()
    price = models.PositiveIntegerField()
    capture = models.ImageField(upload_to="service/%Y/%m/%d")
    category = models.ForeignKey(Category, related_name='services')

    def save(self, *args, **kwargs):
        try:
            this_record = Service.objects.get(id=self.id)
            if this_record.capture != self.capture:
                this_record.capture.delete(save=False)
        except:
            pass
        super(Service, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.capture.delete(save=False)
        super(Service, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Service"
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['title']
        unique_together = ('title', 'capture',)
