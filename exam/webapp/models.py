from django.db import models
status_choices = [('active', 'Active'), ('blocked', 'Blocked')]
# Create your models here.

class GuestBook(models.Model):
    user_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='User Name')
    user_email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='User Email')
    user_text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='User Text')
    date_start = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    date_edit = models.DateTimeField(auto_now=True, null=False, blank=False)
    status = models.TextField(null=False, default='active', choices=status_choices)


    class Meta:
        db_table = 'GuestBook'
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'

    def __str__(self):

        return f'{self.user_name} {self.user_email} {self.user_text}'