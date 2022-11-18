from django.db import models

class Userdata(models.Model):
    name=models.CharField(max_length=20,primary_key=True)
    password=models.IntegerField()
    mobile=models.CharField(max_length=10)

    def __str__(self):
        return("{},{},{}".format(self.name,self.password,self.mobile))



