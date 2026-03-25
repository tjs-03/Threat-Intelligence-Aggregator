Threat Intelligence Aggregator 🛡️

Overview:
This project is a simple Python-based Threat Intelligence Aggregator that processes Indicators of Compromise (IOCs) like IP addresses and domains from different data sources.
It helps in cleaning, organizing, and identifying important or repeated threats for basic cybersecurity analysis.

Features:
Extracts IPs and domains from input data
Cleans and standardizes the data
Identifies repeated/high-risk indicators
Generates simple blocklists
Creates a basic report

How It Works:
Load IOC data (files like CSV/JSON/TXT)
Parse indicators (IP, domain, etc.)
Clean and normalize data
Find repeated indicators
Generate output (blocklist + report)

Tech Stack:
Python 3
Libraries: re, json, os, datetime

How to Run:
Bash
git clone https://github.com/tjs-03/Threat-Intelligence-Aggregator.git
cd Threat-Intelligence-Aggregator
python main.py

Purpose:
This project is built for learning how threat intelligence works and how security teams handle IOC data.

Author:
Tejas Dihora
