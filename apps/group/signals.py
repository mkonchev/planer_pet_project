import secrets

from django.db.models.signals import pre_save
from pytils import translit

from apps.group.models import Group


def create_slug_signal(instance, sender, *args, **kwargs):
    slug = (translit.slugify(instance.name))
    while sender.objects.filter(slug=slug).exists():
        slug = f"{slug}-{secrets.token_urlsafe(8)}"
    instance.slug = slug


pre_save.connect(create_slug_signal, sender=Group)
