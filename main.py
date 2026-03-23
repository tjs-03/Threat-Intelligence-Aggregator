import os
from parser import extract_indicators
from normalizer import normalize
from correlator import correlate
from reporter import save_outputs

def main():
    print("--- Threat Intelligence Aggregator ---")
    data_dir = "data"
    all_normalized_events = []

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"[-] '{data_dir}' folder banaya gaya hai. Isme files rakhein.")
        return

    # [span_10](start_span)STEP 1 & 2: Load and Parse[span_10](end_span)
    for filename in os.listdir(data_dir):
        path = os.path.join(data_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
            found = extract_indicators(content)
            
            # [span_11](start_span)STEP 3: Normalize[span_11](end_span)
            for ip in found['ips']:
                all_normalized_events.append(normalize(ip, "IP", filename))
            for dom in found['domains']:
                all_normalized_events.append(normalize(dom, "Domain", filename))

    # [span_12](start_span)STEP 4: Correlate[span_12](end_span)
    correlated_results = correlate(all_normalized_events)

    # [span_13](start_span)STEP 5 & 6: Blocklist & Final Report[span_13](end_span)
    save_outputs(correlated_results)
    print("[!] Project execution completed successfully.")

if __name__ == "__main__":
    main()
