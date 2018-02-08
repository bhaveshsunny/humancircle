from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField(default=0000000)
    added = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='pics/',default='pics/profile-pictures.png')
    cv = models.FileField(upload_to='cv/%Y/%m/%d/',default='pics/profile-pictures.png')
    reg_date = models.DateTimeField('registration date',auto_now_add=True)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

class Photo(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

class Event(models.Model):
    event = models.CharField(max_length=200)
    cost = models.IntegerField(null=True,default=0)
    reg_start_date = models.DateField(null=True)
    reg_exp_date = models.DateField(null=True)
    event_question = models.CharField(max_length=200,default="")
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return str(self.event)



class Timeslot(models.Model):
    timeslot = models.TimeField(null=True)
    def __str__(self):
        return str(self.timeslot)

class Bookdate(models.Model):
    interview = models.DateField(null=True)
    timeslot = models.ForeignKey(Timeslot,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True)
    event_answer = models.CharField(max_length=500,default="")
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    waitlisted = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user) + '' + str(self.event)
