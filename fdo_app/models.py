from django.db import models

# Create your models here.

#
# class test_t(models.Model):
#     name = models.CharField(max_length=100,null=True)
#     last_name = models.CharField(max_length=100, null=True)
#
#

class FDO(models.Model):
    PID = models.IntegerField()
    metadata_ID = models.IntegerField()
    PID_bit_seq = models.CharField(max_length=200)
    PID_record_ID = models.IntegerField()


class PID_metadata(models.Model):
    licence = models.CharField(max_length=10)
    publisher = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)


class profiles(models.Model):
    attribute1 = models.CharField(max_length=50)
    attribute2 = models.CharField(max_length=50)


class PID_records(models.Model):
    metadata_ID = models.ForeignKey(PID_metadata, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(profiles, on_delete=models.CASCADE)

