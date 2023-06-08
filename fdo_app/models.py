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




