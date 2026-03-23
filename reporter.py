import json
import os

def save_outputs(correlated_data):
    os.makedirs("output", exist_ok=True)
    
    # 1. Save Full JSON Report
    with open("output/report.json", "w") as f:
        # Convert sets to lists for JSON serialization
        report_friendly = {k: {**v, "sources": list(v["sources"])} for k, v in correlated_data.items()}
        json.dump(report_friendly, f, indent=4)
    
    # 2. Save Blocklist (High & Medium Severity only)
    with open("output/blocklist.txt", "w") as f:
        for val, info in correlated_data.items():
            if info["severity"] in ["High", "Medium"]:
                f.write(f"{val}\n")
    
    print("[+] Files saved in 'output/' folder.")
