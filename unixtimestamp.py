import datetime

def unixConvert(timestamp, format):
    # Convert the timestamp to a datetime object
    dt = datetime.datetime.fromtimestamp(timestamp)
    if format == "date":
        formatted_date = dt.strftime("%Y-%m-%d")
        return f"{formatted_date}"
    elif format == "time":
        formatted_time = dt.strftime("%I:%M:%S%p")
        return f"{formatted_time}"    
    elif format == "both":
        formatted_date = dt.strftime("%Y-%m-%d")
        formatted_time = dt.strftime("%I:%M:%S%p")
        return f"{formatted_date}", f"{formatted_time}"
    else:
        return "Invalid format"    