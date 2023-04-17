from django.db import models

# Create your models here.
class Todo3(models.Model):
  id = models.IntegerField
  text = models.CharField(max_length=255)
  completed = models.IntegerField(default=0)
  def __str__(self):
    return self.text + str(self.completed)
  def has_completed(self):
    return self.completed == 1