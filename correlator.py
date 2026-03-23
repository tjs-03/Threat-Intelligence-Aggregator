def correlate(all_data):
    stats = {}
    for entry in all_data:
        val = entry['value']
        if val not in stats:
            stats[val] = {"count": 0, "sources": set(), "type": entry['type']}
        stats[val]["count"] += 1
        stats[val]["sources"].add(entry['source'])

    # [span_7](start_span)Severity logic: High if appears in multiple sources[span_7](end_span)
    for val in stats:
        count = stats[val]["count"]
        if count >= 3: stats[val]["severity"] = "High"
        elif count == 2: stats[val]["severity"] = "Medium"
        else: stats[val]["severity"] = "Low"
    
    return stats
