from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m/', null=True)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/%Y/%m', null=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject


# The Lesson class is a child of the BaseModel class. It has a subject, content, image, course, and
# tags
class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='lessons')
    
    def __str__(self):
        return self.subject


# The Tag class is a subclass of BaseModel, which is a subclass of models.Model.
# The Tag class has a name attribute, which is a CharField.
# The name attribute has a max_length of 50 and is unique. s
# The __str__ method returns the name attribute
class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
