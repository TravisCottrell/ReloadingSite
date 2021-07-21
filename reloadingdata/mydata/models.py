from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Gun(models.Model):
    gun = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.gun

    def get_absolute_url(self):
        return reverse("guns")
    

class Bullet(models.Model):
    """Specific bullet related to a gun."""
    gun = models.ForeignKey(Gun, on_delete=models.CASCADE, related_name="bullets")
    bullet = models.CharField(max_length=50)
    powder = models.CharField(max_length=50)
    primer = models.CharField(max_length=50, null=True, blank=True)
    coal = models.FloatField(null=True,blank=True)
    landTotal = models.FloatField(null=True,blank=True)
    landOffset = models.FloatField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        """Return a string representation of the model."""
        return self.bullet + '/' + self.powder

class TestResult(models.Model):
    """result from a bullet.""" 
    bullet = models.ForeignKey(Bullet, on_delete=models.CASCADE, related_name="results")
    charge = models.FloatField(null=True,blank=True)
    moa = models.FloatField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    class Meta:
        ordering = ['charge']

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.bullet)  + '/' + str(self.charge)

class Velocity(models.Model):
    """velocity from a result.""" 
    result = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name="velocity")
    shotnumber= models.IntegerField(null=True,blank=True)
    velocity = models.FloatField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.result.charge) + '/' + str(self.velocity)