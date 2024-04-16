from django.shortcuts import render
from .models import ProfessionnalProfile, Experience, CertificatCategory, TechnicalSkillCategory, SoftSkill, Project, Education


def home(request):
    template = 'informations/index.html'
    profile = ProfessionnalProfile.objects.first()
    certificate_categories = CertificatCategory.objects.all()
    soft_skills = SoftSkill.objects.all()
    technical_skill_categories = TechnicalSkillCategory.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    context = {
        "profile":profile,
        "certificate_categories":certificate_categories,
        "soft_skills": soft_skills,
        "technical_skill_categories": technical_skill_categories,
        "educations": educations,
        "experiences": experiences,
        "projects": projects,
    }
    
    return render(request, template, context)
