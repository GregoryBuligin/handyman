from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    discription = models.TextField()
    capture = models.ImageField(upload_to="category/%Y/%m/%d")

    def save(self, *args, **kwargs):
        try:
            this_record = Category.objects.get(id=self.id)
            if this_record.capture != self.capture:
                this_record.capture.delete(save=False)
        except:
            pass
        super(Category, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.capture.delete(save=False)
        super(Category, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']
        unique_together = ('title', 'capture',)
