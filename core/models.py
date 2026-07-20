from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Singer(BaseModel):
    name=models.CharField(max_length=225, help_text='singer name')
    description = models.TextField(blank=True, null=True, help_text='About singer')

    class Meta:
        ordering = ["name"]

class Ablum(BaseModel):
    title = models.CharField(max_length=255, help_text="singer Ablum title")
    release_date = models.DateField(help_text="singer Ablum Release Date")
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, help_text="singer that owns the Album")

    class Meta:
        ordering =["title"]