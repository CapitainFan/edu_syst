from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Form, Teacher

@receiver(post_save, sender=Form)
def update_teacher_form(sender, instance, created, **kwargs):
    if created:
        teacher = instance.class_teacher
        teacher.form = instance
        teacher.save()
