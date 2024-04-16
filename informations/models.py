from django.db import models


class ProfessionnalProfile(models.Model):
    description = models.TextField()
    email = models.EmailField()
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    linkedin = models.URLField()
    linkedin_pseudo = models.CharField(max_length=50)
    github = models.URLField()
    github_pseudo = models.CharField(max_length=50)
    

class Experience(models.Model):
    title = models.CharField(max_length=50)
    enterprise = models.CharField(max_length=50)
    date_begin = models.DateField()
    date_end = models.DateField()
    
    def __str__(self):
        return f"{self.title} / {self.enterprise}"
    
        
    def date(self):
        return f'{self.date_begin.strftime("%B %Y")}' + ('' if not self.date_end else f' - {self.date_end.strftime("%B %Y")}')

class ExperienceDetail(models.Model):
    category = models.ForeignKey(Experience, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.content}"

class CertificatCategory(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.title}"

class Certificat(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    category = models.ForeignKey(CertificatCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"
 
class TechnicalSkillCategory(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.title}"

class TechnicalSkill(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(TechnicalSkillCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"

class SoftSkill(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.title}"

class Project(models.Model):
    title = models.CharField(max_length=50)
    # short_description = models.CharField(max_length=200)
    detail = models.TextField()
    # url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.title}"

class Education(models.Model):
    title = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    date_begin = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def date(self):
        return f'{self.date_begin.strftime("%Y")}' + ('' if not self.date_end else f' - {self.date_end.strftime("%Y")}')
    