from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BogieChecksheet, WheelSpec
from .serializers import BogieChecksheetSerializer, WheelSpecSerializer

@api_view(['POST'])
def submit_bogie_checksheet(request):
    serializer = BogieChecksheetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Bogie checksheet submitted successfully.",
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_wheel_specs(request):
    queryset = WheelSpec.objects.all()
    form_number = request.query_params.get('formNumber')
    submitted_by = request.query_params.get('submittedBy')
    submitted_date = request.query_params.get('submittedDate')

    if form_number:
        queryset = queryset.filter(form_number=form_number)
    if submitted_by:
        queryset = queryset.filter(submitted_by=submitted_by)
    if submitted_date:
        queryset = queryset.filter(submitted_date=submitted_date)

    serializer = WheelSpecSerializer(queryset, many=True)
    return Response({
        "message": "Filtered wheel specification forms fetched successfully.",
        "success": True,
        "data": serializer.data
    })
