from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import fdoSerializer, profileSerializer, recordsSerializer, metadataSerializer
# from fdo_app.models import test_t
from fdo_app.models import FDO, profiles, PID_records, PID_metadata


# FDO
@api_view(['GET'])
def getFDO(request):
    FDOs = FDO.objects.all()
    serializer = fdoSerializer(FDOs, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addFDO(request):
    serializer = fdoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# profiles
@api_view(['GET'])
def getProfiles(request):
    pfs = profiles.objects.all()
    serializer = profileSerializer(pfs, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addProfiles(request):
    serializer = profileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# records
@api_view(['GET'])
def getRecords(request):
    recs = PID_records.objects.all()
    serializer = recordsSerializer(recs, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addRecords(request):
    serializer = recordsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# metadata
@api_view(['GET'])
def getMetaData(request):
    metad = PID_metadata.objects.all()
    serializer = metadataSerializer(metad, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addMetaData(request):
    serializer = metadataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)