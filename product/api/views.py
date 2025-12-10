import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def products(request):
    if request.method == "GET":
        products = list(Product.objects.values())
        return JsonResponse(products, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        product = Product.objects.create(
            name=body["name"],
            price=body["price"],
            quantity=body["quantity"],
            description=body.get("description", "")
        )
        return JsonResponse({"message": "Product created", "id": product.product_id})

    elif request.method == "PUT":
        # Update an existing product
        body = json.loads(request.body.decode("utf-8"))
        try:
            product = Product.objects.get(product_id=body["id"])
            product.name = body.get("name", product.name)
            product.price = body.get("price", product.price)
            product.quantity = body.get("quantity", product.quantity)
            product.description = body.get("description", product.description)
            product.save()
            return JsonResponse({"message": "Product updated"})
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

    elif request.method == "DELETE":
        body = json.loads(request.body.decode("utf-8"))
        try:
            product = Product.objects.get(product_id=body["id"])
            product.delete()
            return JsonResponse({"message": "Product deleted"})
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)
