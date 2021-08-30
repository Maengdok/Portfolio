from django.db import models

# Project
class Project(models.Model):
    project_title = models.CharField(max_length = 200)
    project_description = models.TextField(null = True)
    project_link = models.URLField(max_length = 300, null = True)
    pub_date = models.DateTimeField('Date de création')

    # FK
    project_image = models.ForeignKey('Image', on_delete = models.CASCADE, null = True)
    project_techno = models.ManyToManyField('Techno')
    project_skill = models.ManyToManyField('Skill')

    def __str__(self):
        return self.project_title

# Work
class Work(models.Model):
    work_title = models.CharField(max_length = 200)
    work_description = models.TextField(null = True)
    work_city = models.CharField(max_length = 200)
    work_country = models.CharField(max_length = 100)
    work_start = models.DateTimeField('Date de début', null = True)
    work_end = models.DateTimeField('Date de fin')

    # FK
    work_image = models.ForeignKey('Image', on_delete = models.CASCADE, null = True)
    work_techno = models.ManyToManyField('Techno')
    work_skill = models.ManyToManyField('Skill')

    def __str__(self):
        return self.work_title


# Study
class Study(models.Model):
    study_title = models.CharField(max_length = 200)
    study_description = models.TextField(null = True)
    study_city = models.CharField(max_length = 200)
    study_country = models.CharField(max_length = 100)
    study_start = models.DateTimeField('Date de début')
    study_end = models.DateTimeField('Date de fin')

    # FK
    study_image = models.ForeignKey('Image', on_delete = models.CASCADE, null = True)
    study_techno = models.ManyToManyField('Techno')
    study_skill = models.ManyToManyField('Skill')

# Techno
class Techno(models.Model):
    techno_title = models.CharField(max_length = 100)

# Skill
class Skill(models.Model):
    skill_title = models.CharField(max_length = 200)
    skill_percent = models.IntegerField()
    skill_description = models.TextField(null = True)


# Image
class Image(models.Model):
    image_name = models.CharField(max_length = 200)
    image_file = models.FileField(upload_to = 'images/', null = True, verbose_name = "")
