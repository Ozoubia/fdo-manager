from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Thing(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    class Meta:
        abstract = True


class Organisation(Thing):
    legalName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)


class Person(Thing):
    affiliation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=100)


class CreativeWork(Thing):
    # used for the type
    # tuple one used for django and one for the database
    creativeWorkChoices = [
        ('dataset', 'Dataset'),
        ('code', 'Code'),
        ('article', 'Article'),
    ]
    creativeWorkType = models.CharField(max_length=100, choices=creativeWorkChoices)

    creator_type_choices = (
        ('person', 'Person'),
        ('organisation', 'Organisation'),
    )

    creator_type = models.CharField(max_length=20, choices=creator_type_choices)
    creator_org = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)
    creator_person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


    # creator_id = models.PositiveIntegerField()
    #
    # def creator(self):
    #     if self.creator_type == 'person':
    #         return Person.objects.get(pk=self.creator_id)
    #     elif self.creator_type == 'organisation':
    #         return Organisation.objects.get(pk=self.creator_id)
    #     else:
    #         raise ValueError(f"Invalid creator type: {self.creator_type}")

    keywords = models.CharField(max_length=200)
    dateCreated = models.DateField()
    dateModified = models.DateField()
    licence = models.CharField(max_length=200)
    version = models.IntegerField()
    size = models.CharField(max_length=50)
    usage_info = models.CharField(max_length=200)
    # publisher = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    citation = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class Service(Thing):
    # provider_type_choices = (
    #     ('person', 'Person'),
    #     ('organisation', 'Organisation'),
    # )
    #
    # provider_type = models.CharField(max_length=20, choices=provider_type_choices)
    #
    # # Define provider_id as either a foreign key to Person or Organisation
    # if provider_type == 'person':
    #     provider = models.ForeignKey(Person, on_delete=models.CASCADE)
    # elif provider_type == 'organisation':
    #     provider = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    provider_type_choices = (
        ('person', 'Person'),
        ('organisation', 'Organisation'),
    )

    provider_type = models.CharField(max_length=20, choices=provider_type_choices)

    termsOfService = models.CharField(max_length=200)

    provider_org = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)
    provider_person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


class WebAPI(Service):
    documentation = models.CharField(max_length=200)


class SoftwareApplication(CreativeWork):
    releaseNotes = models.CharField(max_length=200)
    softwareRequirements = models.CharField(max_length=200)
    downloadUrl = models.CharField(max_length=200)
    memoryRequirements = models.CharField(max_length=50)
    operatingSystem = models.CharField(max_length=50)
    processorRequirements = models.CharField(max_length=50)




# class artifact_prop(models.Model):
#     name = models.CharField(max_length=30, default='DEFAULT VALUE')
#     url = models.CharField(max_length=200, default='DEFAULT VALUE')
#     description = models.CharField(max_length=300, default='DEFAULT VALUE')
#     creator = models.CharField(max_length=200, default='DEFAULT VALUE')
#     date_created = models.DateField()
#     date_modified = models.DateField()
#     keywords = models.CharField(max_length=200, default='DEFAULT VALUE')
#     licence = models.CharField(max_length=200, default='DEFAULT VALUE')
#     version = models.IntegerField(0)
#     size = models.CharField(max_length=50, default='DEFAULT VALUE')
#     usage_info = models.CharField(max_length=200, default='DEFAULT VALUE')
#     citation = models.CharField(max_length=200, default='DEFAULT VALUE')
#
#
# class PID_metadata(models.Model):
#     meta_class = models.CharField(max_length=20, default='default class')
#     type = models.CharField(max_length=100, default='default type')
#     description = models.CharField(max_length=200, default='default description')
#     url = models.CharField(max_length=200, default='default url')
#     properties = models.ForeignKey(artifact_prop, on_delete=models.CASCADE, null=True)
#
#
#
# class profiles(models.Model):
#     attribute1 = models.CharField(max_length=50)
#     attribute2 = models.CharField(max_length=50)
#
#
# class PID_records(models.Model):
#     metadata_ID = models.ForeignKey(PID_metadata, on_delete=models.CASCADE)
#     profile_id = models.ForeignKey(profiles, on_delete=models.CASCADE)
#
#
# class FDO(models.Model):
#     PID = models.IntegerField()
#     metadata_ID = models.ForeignKey(PID_metadata, on_delete=models.CASCADE)
#     PID_bit_seq = models.CharField(max_length=200)
#     PID_record_ID = models.ForeignKey(PID_records, on_delete=models.CASCADE)