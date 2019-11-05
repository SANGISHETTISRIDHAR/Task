from django.db import models

# Create your models here.
class File(models.Model):
    doc = models.FileField(upload_to='Doc/',default='Doc/None/No-doc.pdf')
class Data(models.Model):
    St_date=models.CharField(max_length=500)
    End_date=models.CharField(max_length=500)
    Task_Id=models.CharField(max_length=500)
    Task_desp=models.CharField(max_length=500)
    Wla_task_des=models.CharField(max_length=500)
    Resources=models.CharField(max_length=500)
    Quantity=models.CharField(max_length=500)
    Responsible_manager=models.CharField(max_length=500)
    Location=models.CharField(max_length=500)
    Chainage_from=models.CharField(max_length=500)
    Chainage_To=models.CharField(max_length=500)
    # exclude = ('id',)

    # def __str__(self):
    #     return self.St_date,self.End_date,self.Task_Id

