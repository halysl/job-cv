from django.db import models
from jianli.fields import ListField,StringListField
# Create your models here.


# class Test(models.Model):
#     test = ListField()
#     slf = StringListField()

# class Edu(models.Model):
#     e_id = models.IntegerField(primary_key=True,default=0)
#     time = models.CharField(max_length=20)
#     name = models.CharField(max_length=50)
#     href = models.CharField(max_length=10)
#     honors = models.CharField(max_length=200)

# class PE(models.Model):
#     p_id = models.IntegerField()
#     name = models.CharField(max_length=50)
#     duty = models.CharField(max_length=20)
#     content = models.CharField(max_length=200)
#     git_link = models.CharField(max_length=100)
#     blog_link = models.CharField(max_length=100)
#     full_content = models.CharField(max_length=1000)

# class Skill(models.Model):
#     s_id = models.IntegerField()
#     name = models.CharField(max_length=50)
#     score = models.CharField(max_length=10)

class Cv(models.Model):
    c_id = models.IntegerField(primary_key=True,default=0)
    base_dir = models.CharField(max_length=100)
    avatar_dir = models.CharField(max_length=100)
    one_sentence_introduction = models.CharField(max_length=50)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=100)
    about_me = models.CharField(max_length=300)
    edu = models.CharField(max_length=1000)
    project_experience = models.CharField(max_length=2000)
    skill = models.CharField(max_length=2000)