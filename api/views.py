from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import fdoSerializer
# from fdo_app.models import test_t
from fdo_app.models import FDO

@api_view(['GET'])
def getData(request):
    FDOs = FDO.objects.all()
    serializer = fdoSerializer(FDOs, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = fdoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)