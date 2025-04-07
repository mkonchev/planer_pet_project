from django.db.models.signals import post_save
from pytils import translit

from apps.group.models import Group


def create_slug_signal(instance, created, *args, **kwargs):
    if created:
        instance.slug = translit.slugify(instance.name)
        instance.save()


post_save.connect(create_slug_signal, sender=Group)
