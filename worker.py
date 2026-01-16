import time
import random
from event_queue import get_event, publish_event, send_to_dead_letter

MAX_RETRIES = 3


def start_worker():
    print("Worker started. Waiting for events...")

    while True:
        event = get_event()

        if event:
            print("Processing event:", event)
            handle_event(event)
        else:
            time.sleep(1)


def handle_event(event):
    retries = event.get("retries", 0)

    try:
        if event["type"] == "OrderPlaced":
            process_payment(event)
            update_inventory(event)
            send_notification(event)

    except Exception as e:
        print("Error:", e)

        if retries < MAX_RETRIES:
            event["retries"] = retries + 1
            print(f"Retrying event ({event['retries']})")
            publish_event(event)
        else:
            print("Sending event to dead letter queue")
            send_to_dead_letter(event)


def process_payment(event):
    print(f"Processing payment for order {event['order_id']}")
    time.sleep(1)

    if random.choice([True, False]):
        raise Exception("Payment gateway failure")

    print("Payment successful")


def update_inventory(event):
    print(f"Updating inventory for {event['item']}")
    time.sleep(1)
    print("Inventory updated")


def send_notification(event):
    print(f"Sending notification for order {event['order_id']}")
    time.sleep(1)
    print("Notification sent")


if __name__ == "__main__":
    start_worker()

