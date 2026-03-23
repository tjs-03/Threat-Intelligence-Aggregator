# Threat Intelligence Aggregator (Non-AI) 🛡️

## Project Overview
This project is a practical **Threat Intelligence (TI) Aggregator** designed to handle the challenges of modern cybersecurity operations. Organizations receive threat feeds in inconsistent formats (CSV, JSON, TXT), making analysis slow. [span_2](start_span)[span_3](start_span)[span_4](start_span)This tool automates the collection, normalization, and correlation of Indicators of Compromise (IOCs) to produce actionable intelligence.[span_2](end_span)[span_3](end_span)[span_4](end_span)

## Key Features
- **[span_5](start_span)IOC Parsing:** Extracts Malicious IPs and Domains using Regular Expressions (Regex).[span_5](end_span)
- **[span_6](start_span)[span_7](start_span)Normalization Engine:** Standardizes heterogeneous data into a unified structure with metadata (source, timestamp).[span_6](end_span)[span_7](end_span)
- **[span_8](start_span)[span_9](start_span)Correlation Engine:** Identifies repeated indicators across different feeds and assigns severity ratings (Low/Medium/High).[span_8](end_span)[span_9](end_span)
- **[span_10](start_span)[span_11](start_span)[span_12](start_span)Blocklist Generation:** Automatically creates ready-to-deploy blocklists for Firewalls and Web Filters.[span_10](end_span)[span_11](end_span)[span_12](end_span)
- **[span_13](start_span)[span_14](start_span)Reporting:** Generates comprehensive JSON reports and summary statistics.[span_13](end_span)[span_14](end_span)

## Project Architecture
The project follows a modular workflow:
1. **[span_15](start_span)Load Feeds:** Import IOC data from local files.[span_15](end_span)
2. **[span_16](start_span)Parse:** Extract raw indicators.[span_16](end_span)
3. **[span_17](start_span)Normalize:** Clean and add metadata.[span_17](end_span)
4. **[span_18](start_span)Correlate:** Cross-source matching to find high-priority threats.[span_18](end_span)
5. **[span_19](start_span)Export:** Generate final reports and blocklists.[span_19](end_span)

## Tech Stack
- **[span_20](start_span)Language:** Python 3[span_20](end_span)
- **[span_21](start_span)Environment:** Kali Linux (Recommended)[span_21](end_span)
- **[span_22](start_span)Libraries:** `re` (Regex), `json`, `os`, `datetime`[span_22](end_span)

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/tjs-03/Threat-Intelligence-Aggregator.git](https://github.com/tjs-03/Threat-Intelligence-Aggregator.git)
