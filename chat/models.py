from django.contrib.auth import get_user_model

from django.db import models
User=get_user_model()

# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='officer', on_delete=models.CASCADE)
    officer = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username
class Message(models.Model):
    author=models.ForeignKey(Contact, related_name='author_message', on_delete=models.CASCADE)
    content=models.TextField()
    timesent=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username 
    def last_12_messages(self):
        return Message.objects.order_by('-timesent').all()[: 12 ]  
class Chat(models.Model):
    members = models.ManyToManyField(
        Contact, related_name='chats', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return "{}".format(self.pk)