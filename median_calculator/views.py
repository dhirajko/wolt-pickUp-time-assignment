from django.http import JsonResponse
from .utils import median_calculator


def PickupTimeCalculator(request):
    location_id = request.GET["location_id"]
    start_time = request.GET["start_time"]
    end_time = request.GET["end_time"]
    median = median_calculator(location_id, start_time, end_time)
    return JsonResponse({"median": int(median)})
