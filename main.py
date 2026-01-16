from fastapi import FastAPI
from event_queue import publish_event


app = FastAPI()

@app.post("/order")
def place_order(order_id: int, item: str, quantity: int):
    event = {
        "type": "OrderPlaced",
        "order_id": order_id,
        "item": item,
        "quantity": quantity
    }

    publish_event(event)

    return {
        "message": "Order placed successfully",
        "event": event
    }
