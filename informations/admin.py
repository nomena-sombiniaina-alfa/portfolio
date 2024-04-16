from django.contrib import admin
from .models import ProfessionnalProfile, Experience, ExperienceDetail, CertificatCategory, Certificat, TechnicalSkill, TechnicalSkillCategory, SoftSkill, Project, Education

admin.site.register(ProfessionnalProfile)
admin.site.register(Experience)
admin.site.register(ExperienceDetail)
admin.site.register(Certificat)
admin.site.register(CertificatCategory)
admin.site.register(TechnicalSkill)
admin.site.register(SoftSkill)
admin.site.register(TechnicalSkillCategory)
admin.site.register(Project)
admin.site.register(Education)