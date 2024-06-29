import re
from collections import Counter

log_file_path = 'access.log'

def analyze_log():
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    # Regular expression to match HTTP status codes
    status_code_pattern = re.compile(r'"\s(\d{3})\s')
    status_codes = Counter(re.findall(status_code_pattern, ' '.join(logs)))

    # Regular expression to match requested pages
    page_pattern = re.compile(r'GET\s(\/\S*)\sHTTP')
    pages = Counter(re.findall(page_pattern, ' '.join(logs)))

    # Regular expression to match IP addresses
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ips = Counter(re.findall(ip_pattern, ' '.join(logs)))

    print(f"404 Errors: {status_codes['404']}")
    print(f"Most Requested Pages: {pages.most_common(5)}")
    print(f"Top 5 IPs: {ips.most_common(5)}")

if __name__ == '__main__':
    analyze_log()
