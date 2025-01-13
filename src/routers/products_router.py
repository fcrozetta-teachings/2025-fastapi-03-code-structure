from fastapi import APIRouter


app = APIRouter(tags=["Products"], prefix="/products")


@app.get("/")
def list_products():
    """
    This endpoint should return all products
    """
    return products


@app.get("/{product_id}")
def get_product(product_id: int):
    """
    this endpoint has to return the product details for a given product id
    """
    return list(filter(lambda x: x["product_id"] == product_id, products))


@app.post("/")
def create_product(payload: dict):
    name = payload["name"]
    for p in products:
        if p["name"] == name:
            return False
    last_product = products[-1]
    last_id = last_product["product_id"]
    products.append({"product_id": last_id + 1, "name": name, "price": 0})
    return last_id + 1
