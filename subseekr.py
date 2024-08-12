import requests
from colorama import Fore, Style, init
import time
import sys
from fake_useragent import UserAgent
import socket
import concurrent.futures

init(autoreset=True)

APIKEY='''
 [91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m         [93m_[0m[92m_[0m     [96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m               [94m_[0m[95m_[0m         
[91m|[0m     [93m_[0m[92m_[0m[96m|[0m[94m.[0m[95m-[0m[91m-[0m[93m.[0m[92m-[0m[96m-[0m[94m.[0m[95m|[0m  [91m|[0m[93m-[0m[92m-[0m[96m.[0m[94m|[0m     [95m_[0m[91m_[0m[93m|[0m[92m.[0m[96m-[0m[94m-[0m[95m-[0m[91m-[0m[93m-[0m[92m.[0m[96m-[0m[94m-[0m[95m-[0m[91m-[0m[93m-[0m[92m.[0m[96m|[0m  [94m|[0m[95m-[0m[91m-[0m[93m.[0m[92m-[0m[96m-[0m[94m-[0m[95m-[0m[91m.[0m
[93m|[0m[92m_[0m[96m_[0m     [94m|[0m[95m|[0m  [91m|[0m  [93m|[0m[92m|[0m  [96m_[0m  [94m|[0m[95m|[0m[91m_[0m[93m_[0m     [92m|[0m[96m|[0m  [94m-[0m[95m_[0m[91m_[0m[93m|[0m  [92m-[0m[96m_[0m[94m_[0m[95m|[0m[91m|[0m    [93m<[0m[92m|[0m   [96m_[0m[94m|[0m
[95m|[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m|[0m[92m|[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m|[0m[96m|[0m[94m_[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m|[0m[94m|[0m[95m_[0m[91m_[0m[93m_[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m|[0m[93m|[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m|[0m[92m_[0m[96m_[0m[94m_[0m[95m_[0m[91m_[0m[93m|[0m[92m|[0m[96m_[0m[94m_[0m[95m|[0m[91m_[0m[93m_[0m[92m|[0m[96m_[0m[94m_[0m[95m|[0m  
[91mI[0m[93mn[0m[92ms[0m[96mp[0m[94mi[0m[95mr[0m[91me[0m[93md[0m [92mb[0m[96my[0m [94mD[0m[95mi[0m[91mr[0m[93mB[0m[92mu[0m[96ms[0m[94mt[0m[95me[0m[91mr[0m [93m|[0m [92mh[0m[96mt[0m[94mt[0m[95mp[0m[91ms[0m[93m:[0m[92m/[0m[96m/[0m[94mg[0m[95mi[0m[91mt[0m[93mh[0m[92mu[0m[96mb[0m[94m.[0m[95mc[0m[91mo[0m[93mm[0m[92m/[0m[96mn[0m[94mo[0m[95ma[0m[91mr[0m[93mc[0m[92mh[0m[96me[0m[94m/[0m[95ms[0m[91mu[0m[93mb[0m[92ms[0m[96me[0m[94me[0m[95mk[0m[91mr[0m
'''
print(APIKEY)



ua = UserAgent()

def print_progress_bar(current, total, bar_length=50):
    progress = current / total
    block = int(bar_length * progress)
    text = f"\r[91mT[0m[93me[0m[92ms[0m[96mt[0m[94mi[0m[95mn[0m[91mg[0m {current} of {total} [{'#' * block + '-' * (bar_length - block)}] {int(progress * 100)}%"
    sys.stdout.write(text)
    sys.stdout.flush()

def check_single_subdomain(sub, domain):
    url = f"https://{sub}.{domain}"
    headers = {'User-Agent': ua.random}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            ip_address = socket.gethostbyname(f"{sub}.{domain}")
            print(f"\n{Fore.GREEN}[ONLINE]{Style.RESET_ALL} {ip_address} | {url}")
            return url
    except requests.RequestException:
        pass
    return None

def check_subdomains(domain, threads):
    with open("SubDomains.txt", "r", encoding="utf8") as file:
        subdomains = [line.strip() for line in file.readlines()]

    total_subdomains = len(subdomains)
    online_links = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_subdomain = {executor.submit(check_single_subdomain, sub, domain): sub for sub in subdomains}
        for index, future in enumerate(concurrent.futures.as_completed(future_to_subdomain), start=1):
            result = future.result()
            if result:
                online_links.append(result)
            print_progress_bar(index, total_subdomains)

    if online_links:
        with open("online_links.txt", "a", encoding="utf8") as output_file:
            for link in online_links:
                output_file.write(link + "\n")

def main():
    thread_count = 100
    while True:
        try:
            thread_input = input(f"{Fore.BLUE}Enter the number of threads to use (1-250, default 100): {Style.RESET_ALL}")
            if thread_input:
                thread_count = max(1, min(250, int(thread_input)))

            user_input = input(f"{Fore.BLUE}Enter domain(s) (comma-separated, e.g., example.com,example2.com): {Style.RESET_ALL}")
            domains = [domain.strip() for domain in user_input.split(",")]

            for domain in domains:
                check_subdomains(domain, thread_count)

            repeat = input(f"{Fore.YELLOW}Do you want to check another domain? (y/n): {Style.RESET_ALL}")
            if repeat.lower() != 'y':
                break
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Exiting...{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
