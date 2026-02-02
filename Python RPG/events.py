### Event Processor##
def log_event(event_name, *tags, **details):
    print(f"Event: {event_name}")
    for tag in tags:
        print(f"Tag: {tag}")
    for key, value in details.items():
        print(f"{key} -> {value}")
    return len(tags) + len(details)