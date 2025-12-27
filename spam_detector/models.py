from django.db import models

class Email(models.Model):
    sender = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_spam = models.BooleanField(null=True)  # True=spam, False=ham, None=unknown
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.subject}"
