from django.db import models
from django.contrib.auth import get_user_model


class Message(models.Model):
    message_from = models.ForeignKey('auth.User',
                                    related_name='message_from_set',on_delete=models.CASCADE)
    message_to = models.ForeignKey('auth.User',
                                related_name='message_to_set',
                                on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'Message from {self.message_from} to {self.message_to}'
    


user_model = get_user_model()
user_model.add_to_class('message',
                        models.ManyToManyField('self',
                                                through=Message,
                                                related_name='message_to'))