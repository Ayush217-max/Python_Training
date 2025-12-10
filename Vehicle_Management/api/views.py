import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle

@csrf_exempt
def vehicles_management(request):
    if request.method == "GET":
        vehicles = list(Vehicle.objects.values())
        return JsonResponse(vehicles, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        vehicle = Vehicle.objects.create(
            number_plate=body["number_plate"],
            vehicle_type=body["vehicle_type"],
            manufacturer=body["manufacturer"],
            year=body["year"],
        )
        return JsonResponse({"message": "Vehicle created", "id": vehicle.vehicle_id})

    elif request.method == "PUT":
        # Update an existing product
        body = json.loads(request.body.decode("utf-8"))
        try:
            vehicle = Vehicle.objects.get(vehicle_id=body["vehicle_id"])
            vehicle.number_plate = body.get("number_plate", vehicle.number_plate)
            vehicle.vehicle_type = body.get("vehicle_type", vehicle.vehicle_type)
            vehicle.manufacturer = body.get("manufacturer", vehicle.manufacturer)
            vehicle.year = body.get("year",vehicle.year)
            vehicle.save()
            return JsonResponse({"message": "Vehicle updated"})
        except Vehicle.DoesNotExist:
            return JsonResponse({"error": "Vehicle not found"}, status=404)

    elif request.method == "DELETE":
        body = json.loads(request.body.decode("utf-8"))
        try:
            v = Vehicle.objects.get(vehicle_id=body["vehicle_id"])
            v.delete()
            return JsonResponse({"message": "Vehicle deleted"})
        except Vehicle.DoesNotExist:
            return JsonResponse({"error": "Vehicle not found"}, status=404)

    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)
