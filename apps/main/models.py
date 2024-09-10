from django.db import models
from requests import post
from django.conf import settings
from .validators import img_validator, custom_file_path
from pytz import timezone

class Carousel(models.Model):
    image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])

    def __str__(self):
        return self.image.name


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])
    profession = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name


class Advantage(models.Model):
    heading = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.heading


class About(models.Model):
    image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])
    text = models.TextField()

    def __str__(self):
        return self.image.name


class Certificate(models.Model):
    image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])

    def __str__(self):
        return self.image.name


class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_read:
            text = f"Ism: {self.name}\n"
            text += f"Telefon: {self.phone}\n"
            text += f"Javob berildi: ✅\n"
            text += f"Yuborilgan vaqt: {self.created_at.astimezone(tz=timezone('Asia/Tashkent')).strftime('%d.%m.%Y %H:%M')}"
            mes = self.message
            post(f"https://api.telegram.org/bot{settings.BOT_TOKEN}/editMessageText", json={
                "chat_id": settings.GROUP_ID,
                "message_id": mes.message_id,
                "text": text
            })
        super(Application, self).save(*args, **kwargs)


class BotMessage(models.Model):
    application = models.OneToOneField(Application, models.CASCADE, related_name='message')
    message_id = models.CharField(max_length=100)

    def __str__(self):
        return self.message_id
