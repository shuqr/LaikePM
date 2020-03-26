from django.db import models


# Create your models here.
class AppVersion(models.Model):
    appName = models.CharField(max_length=50)
    version = models.CharField(max_length=100)
    versionCode = models.CharField(max_length=10)
    branchName = models.CharField(max_length=100)
    downloadUrl = models.CharField(max_length=300)
    createTime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.version
