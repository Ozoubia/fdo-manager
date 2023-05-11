from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
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



# # FDO ---------------------------------------------------------------------
# @api_view(['GET'])
# def getFDO(request):
#     FDOs = FDO.objects.all()
#     serializer = fdoSerializer(FDOs, many=True)
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def addFDO(request):
#     serializer = fdoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# # profiles ---------------------------------------------------------------
# @api_view(['GET'])
# def getProfiles(request):
#     pfs = profiles.objects.all()
#     serializer = profileSerializer(pfs, many=True)
#
#     return Response(serializer.data)
#
#
# # get one profile with id
# @api_view(['GET'])
# def getProfile(request, id):
#     try:
#         pf = pf = profiles.objects.get(id=id)
#
#     except profiles.DoesNotExist:
#         msg = {'msg': "not found error"}
#         return Response(msg)
#
#     serializer = profileSerializer(pf)
#     return Response(serializer.data)
#
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def addProfiles(request):
#     serializer = profileSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['PATCH'])
# def updateProfiles(request, id):
#     try:
#         pf = profiles.objects.get(id=id)
#     except profiles.DoesNotExist:
#         msg = {'msg': "not found error"}
#         return Response(msg)
#
#     serializer = profileSerializer(pf, data=request.data, partial=True)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
#
#
# @api_view(['DELETE'])
# def deleteProfile(request, id):
#     try:
#         pf = profiles.objects.get(id=id)
#     except profiles.DoesNotExist:
#         msg = {'msg': "not found error"}
#         return Response(msg)
#     pf.delete()
#
#     return Response(status=status.HTTP_204_NO_CONTENT)
#
# # records ----------------------------------------------------------------------------
# @api_view(['GET'])
# def getRecords(request):
#     recs = PID_records.objects.all()
#     serializer = recordsSerializer(recs, many=True)
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def addRecords(request):
#     serializer = recordsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# # metadata -------------------------------------------------------------------------------
# @api_view(['GET'])
# def getMetaData(request):
#     metad = PID_metadata.objects.all()
#     serializer = metadataSerializer(metad, many=True)
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def addMetaData(request):
#     serializer = metadataSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# # artifact properties -------------------------------------------------------------------------
# @api_view(['GET'])
# def getArtprop(request):
#     artprop = artifact_prop.objects.all()
#     serializer = artPropertiesSerializer(artprop, many=True)
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def addArtprop(request):
#     serializer = artPropertiesSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)