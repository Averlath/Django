from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    page_text = models.CharField(max_length=1000)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField('creation_date')
    image = models.ImageField(upload_to='images', null=True, blank=True)
    string = "images"

    def __str__(self):
        return self.title

    def has_image(self):
        return True if str(self.image).find(self.string) == 0 else False

    has_image.boolean = True