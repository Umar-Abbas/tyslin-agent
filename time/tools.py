import datetime

def get_time(timezone: str = "UTC"):
    """Gets the current time in a given timezone."""
    # This is a placeholder for a real time API call
    now = datetime.datetime.now(datetime.timezone.utc)
    return f"The current time is {now}."
