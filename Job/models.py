
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

JOB_TYPE=(
    ('full type','full type'),
    ('part type','part type'),
)
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name

    


class job(models.Model):
    owner=models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title =models.CharField(max_length=50)   
    description=models.TextField(max_length=1000)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    publish_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=image_upload)
    slug=models.SlugField(blank=True,null=True)


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Apply(models.Model):
    Job=models.ForeignKey(job,related_name='apply_job',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    website=models.URLField()
    CV=models.FileField(upload_to='apply/')
    cover_letter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name