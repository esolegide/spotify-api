from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__} - {self.pk}: ({self.created_at}, {self.updated_at})"

    class Meta:
        abstract = True


class Singer(BaseModel):
    name=models.CharField(max_length=225, help_text='singer name')
    description = models.TextField(blank=True, null=True, help_text='About singer')

    def __str__(self):
       return f"singer - {self.name} ({self.pk})"

    class Meta:
        ordering = ["name"]

class Album(BaseModel):
    title = models.CharField(max_length=255, help_text="singer Ablum title")
    release_date = models.DateField(help_text="singer Ablum Release Date")
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, help_text="singer that owns the Album")

    class Meta:
        ordering =["title"]