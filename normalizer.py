import datetime

def normalize(indicator_value, ioc_type, source):
    return {
        "value": indicator_value.strip().lower(),
        "type": ioc_type,
        "source": source,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
