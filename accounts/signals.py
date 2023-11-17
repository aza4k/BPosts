from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserDetail

@receiver(post_save, sender=User)
def create_user_detail(sender, instance, created, **kwargs):
    """Создать объект UserDetail при создании пользователя."""
    if created:
        UserDetail.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_detail(sender, instance, **kwargs):
    """Сохранить объект UserDetail при сохранении пользователя."""
    instance.userdetail.save()
