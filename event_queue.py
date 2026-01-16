from collections import deque

event_queue = deque()
dead_letter_queue = deque()

def publish_event(event):
    event_queue.append(event)

def get_event():
    if event_queue:
        return event_queue.popleft()
    return None

def send_to_dead_letter(event):
    dead_letter_queue.append(event)
