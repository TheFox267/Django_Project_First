from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='user_avatar/%Y/%m/%d/', default='user_avatar/avatar.png', blank=True)
    birth_date = models.DateField(null=True, blank=True)

    MALE = 'M'
    FEMALE = 'W'
    ANOTHER = 'ANOTHER'
    NONE = None

    gender = [
        (MALE, 'мужской'),
        (FEMALE, 'женский'),
        (ANOTHER, 'другой'),
        (NONE, 'не выбран'),
    ]
    gender_choice = models.CharField(max_length=7, choices=gender, blank=True)

    def get_avatar(self):
        if not self.avatar:
            return '/media/user_avatar/avatar.png'
        return self.avatar.url

    def avatar_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_avatar())

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('avatar_tag', 'user')  # В качестве поля указываем метод, который вернёт тег картинки в списке пользовательских профилей
    readonly_fields = ['avatar_tag']  # обязательно read only режим
    fields = ('avatar_tag', 'user')  # Указываем поля, которые нужно отобразить в административной форме
