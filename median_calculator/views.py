from django.http import JsonResponse
from .utils import median_calculator, is_date_valid, is_int_valid



def PickupTimeCalculator(request):
    location_id = request.GET.get("location_id")
    start_time = request.GET.get("start_time")
    end_time = request.GET.get("end_time")
    if (request.GET and location_id and start_time and end_time):
        if not (is_int_valid(location_id) and is_date_valid(start_time) and is_date_valid(end_time)):
            return JsonResponse(data={"message": "Invalid Input"}, status=400, safe=True)
        median = median_calculator(location_id, start_time, end_time)
        return JsonResponse(data={"median": int(median)}, status=200, safe=True)
    return JsonResponse(data={"message": "Invalid Qurery"}, status=400, safe=True)

