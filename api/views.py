from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# from .serializers import fdoSerializer, profileSerializer, recordsSerializer, metadataSerializer, artPropertiesSerializer
# from fdo_app.models import FDO, profiles, PID_records, PID_metadata, artifact_prop

from fdo_app.models import Thing, Organisation, CreativeWork, Service, WebAPI, SoftwareApplication, Person
from .serializers import thingSerializer, organizationSerializer, creativeWorkSerializer, serviceSerializer, webapiSerializer, softwareapplicationSerializer, personSerializer


# Person -------------------------------------------------------------------
@api_view(['GET'])
def getPerson(request):
    persons = Person.objects.all()
    serializer = personSerializer(persons, many=True)

    if not persons:
        message = 'No Person found'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_404_NOT_FOUND)
    else:
        message = 'Retrieved all persons successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getPersonByID(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
        serializer = personSerializer(person)
        message = 'Retrieved the person successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    except Person.DoesNotExist:
        message = 'Person not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addPerson(request):
    serializer = personSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Person added successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_201_CREATED)
    else:
        message = 'Person addition failed'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatePerson(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        message = 'Person not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = personSerializer(person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Person updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def patchPerson(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        message = 'Person not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = personSerializer(person, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = 'person partially updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletePerson(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        message = 'Person not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    person.delete()
    message = 'Person deleted successfully'
    return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)


# organisation -------------------------------------------------------------
@api_view(['GET'])
def getOrganization(request):
    orgs = Organisation.objects.all()
    serializer = organizationSerializer(orgs, many=True)

    if not orgs:
        message = 'No organization found'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_404_NOT_FOUND)
    else:
        message = 'Retrieved all Organizations successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getOrgByID(request, organisation_id):
    try:
        org = Organisation.objects.get(id=organisation_id)
        serializer = organizationSerializer(org)
        message = 'Retrieved the Organisation successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    except Organisation.DoesNotExist:
        message = 'Organisation not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addOrganization(request):
    serializer = organizationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Organization added successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_201_CREATED)
    else:
        message = 'Organization addition failed'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateOrganisation(request, organisation_id):
    try:
        org = Organisation.objects.get(id=organisation_id)
    except Organisation.DoesNotExist:
        message = 'Organisation not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = organizationSerializer(org, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Organisation updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def patchOrganisation(request, organisation_id):
    try:
        org = Organisation.objects.get(id=organisation_id)
    except Organisation.DoesNotExist:
        message = 'Organisation not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = organizationSerializer(org, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = 'Organisation partially updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteOrganisation(request, organisation_id):
    try:
        org = Organisation.objects.get(id=organisation_id)
    except Organisation.DoesNotExist:
        message = 'Organisation not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    org.delete()
    message = 'Organisation deleted successfully'
    return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)


# service ------------------------------------------------------------------
@api_view(['GET'])
def getService(request):
    services = Service.objects.all()
    serializer = serviceSerializer(services, many=True)

    if not services:
        message = 'No service found'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_404_NOT_FOUND)
    else:
        message = 'Retrieved all services successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getServiceByID(request, service_id):
    try:
        serv = Service.objects.get(id=service_id)
        serializer = serviceSerializer(serv)
        message = 'Retrieved the Service successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    except Service.DoesNotExist:
        message = 'Service not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addService(request):
    # check if the 'type' field is present in the request data
    # if 'provider_type' not in request.data:
    #     message = 'provider_type field is required.'
    #     return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
    #
    # # check if the specified type is valid
    # valid_types = ('person', 'organisation')
    # if request.data['provider_type'] not in valid_types:
    #     message = f"Invalid provider_type '{request.data['provider_type']}'. Must be one of {valid_types}."
    #     return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
    #
    # # check that the specified person or organization field is present based on the type
    # if request.data['provider_type'] == 'person':
    #     required_field = 'person'
    # else:
    #     required_field = 'organisation'

    # if required_field not in request.data:
    #     message = f"{required_field.capitalize()} field is required for provider_type '{request.data['provider_type']}'."
    #     return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

    serializer = serviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Service added successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_201_CREATED)
    else:
        message = 'Organisation addition failed'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateService(request, service_id):
    try:
        ser = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        message = 'Service not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = serviceSerializer(ser, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Service updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patchService(request, service_id):
    try:
        serv = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        message = 'Service not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = serviceSerializer(serv, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = 'Service partially updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteService(request, service_id):
    try:
        serv = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        message = 'Service not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serv.delete()
    message = 'Service deleted successfully'
    return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)


# creative work --------------------------------------------------------------
@api_view(['GET'])
def getCreativeWork(request):
    CW = CreativeWork.objects.all()
    serializer = creativeWorkSerializer(CW, many=True)

    if not CW:
        message = 'No creative work found'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_404_NOT_FOUND)
    else:
        message = 'Retrieved all creative works successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getCreativeworkByID(request, creativework_id):
    try:
        cw = CreativeWork.objects.get(id=creativework_id)
        serializer = creativeWorkSerializer(cw)
        message = 'Retrieved the Creative work successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    except CreativeWork.DoesNotExist:
        message = 'Creative work not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addCreativeWork(request):

    serializer = creativeWorkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Creative work added successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_201_CREATED)
    else:
        message = 'Creative work addition failed'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateCreativeWork(request, creativework_id):
    try:
        cw = CreativeWork.objects.get(id=creativework_id)
    except CreativeWork.DoesNotExist:
        message = 'Creative work not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = creativeWorkSerializer(cw, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Creative work updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def patchCreativeWork(request, creativework_id):
    try:
        cw = CreativeWork.objects.get(id=creativework_id)
    except CreativeWork.DoesNotExist:
        message = 'Creative work not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = creativeWorkSerializer(cw, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = 'Creative work partially updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteCreativeWork(request, creativework_id):
    try:
        cw = CreativeWork.objects.get(id=creativework_id)
    except CreativeWork.DoesNotExist:
        message = 'Creative work not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    cw.delete()
    message = 'Creative work deleted successfully'
    return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)



# Web api -------------------------------------------------------------------
@api_view(['GET'])
def getWebAPI(request):
    webapis = WebAPI.objects.all()
    serializer = webapiSerializer(webapis, many=True)

    if not webapis:
        message = 'No Web API work found'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_404_NOT_FOUND)
    else:
        message = 'Retrieved all Web APIs successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getWebAPIByID(request, webapi_id):
    try:
        webapi = WebAPI.objects.get(id=webapi_id)
        serializer = webapiSerializer(webapi)
        message = 'Retrieved the web API successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    except WebAPI.DoesNotExist:
        message = 'Web API not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addWebAPI(request):

    serializer = webapiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Web API added successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_201_CREATED)
    else:
        message = 'Web API addition failed'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateWebAPI(request, webapi_id):
    try:
        webapi = WebAPI.objects.get(id=webapi_id)
    except WebAPI.DoesNotExist:
        message = 'Web API not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = webapiSerializer(webapi, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Web API updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def patchWebAPI(request, webapi_id):
    try:
        webapi = WebAPI.objects.get(id=webapi_id)
    except WebAPI.DoesNotExist:
        message = 'Web API not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = webapiSerializer(webapi, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = 'Web API partially updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteWebAPI(request, webapi_id):
    try:
        webapi = WebAPI.objects.get(id=webapi_id)
    except WebAPI.DoesNotExist:
        message = 'Web API not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    webapi.delete()
    message = 'Web API deleted successfully'
    return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)


# software application -------------------------------------------------------
@api_view(['GET'])
def getSoftwareApp(request):
    softwareApps = SoftwareApplication.objects.all()
    serializer = softwareapplicationSerializer(softwareApps, many=True)

    if not softwareApps:
        message = 'No Software Application work found'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_404_NOT_FOUND)
    else:
        message = 'Retrieved all Software Applications successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getSoftwareAppByID(request, softwareapp_id):
    try:
        softapp = SoftwareApplication.objects.get(id=softwareapp_id)
        serializer = softwareapplicationSerializer(softapp)
        message = 'Retrieved the software application successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    except SoftwareApplication.DoesNotExist:
        message = 'Software Application not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def addSoftwareApp(request):

    serializer = softwareapplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Software application added successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_201_CREATED)
    else:
        message = 'Software application addition failed'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateSoftwareApp(request, softwareapp_id):
    try:
        soft = SoftwareApplication.objects.get(id=softwareapp_id)
    except SoftwareApplication.DoesNotExist:
        message = 'Software app not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = softwareapplicationSerializer(soft, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = 'Software app updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def patchSoftwareApp(request, softwareapp_id):
    try:
        soft = SoftwareApplication.objects.get(id=softwareapp_id)
    except SoftwareApplication.DoesNotExist:
        message = 'Software app not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    serializer = softwareapplicationSerializer(soft, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = 'Software app partially updated successfully'
        return Response({'data': serializer.data, 'message': message}, status=status.HTTP_200_OK)
    else:
        message = 'Invalid data'
        return Response({'message': message, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteSoftwareApp(request, softwareapp_id):
    try:
        soft = SoftwareApplication.objects.get(id=softwareapp_id)
    except SoftwareApplication.DoesNotExist:
        message = 'Software App not found'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    soft.delete()
    message = 'Software App deleted successfully'
    return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)


