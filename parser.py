import re

def extract_indicators(text):
    # Regex for IPv4
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    # Regex for Domains
    domain_pattern = r'\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b'
    
    found_ips = re.findall(ip_pattern, text)
    found_domains = re.findall(domain_pattern, text)
    
    return {"ips": found_ips, "domains": found_domains}
