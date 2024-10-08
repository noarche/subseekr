# Disclaimer:
# This code/script/application/program is solely for educational and learning purposes.
# All information, datasets, images, code, and materials are presented in good faith and
# intended for instructive use. However, noarche make no representation or warranty, 
# express or implied, regarding the accuracy, adequacy, validity, reliability, availability,
# or completeness of any data or associated materials.
# Under no circumstance shall noarche have any liability to you for any loss, damage, or 
# misinterpretation arising due to the use of or reliance on the provided data. Your utilization
# of the code and your interpretations thereof are undertaken at your own discretion and risk.
#
# By executing script/code/application, the user acknowledges and agrees that they have read, 
# understood, and accepted the terms and conditions (or any other relevant documentation or 
#policy) as provided by noarche.
#
#Visit https://github.com/noarche for more information. 
#
#  _.··._.·°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°°·.·°·._.··._
# ███╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗██╗  ██╗███████╗
# ████╗  ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
# ██╔██╗ ██║██║   ██║███████║██████╔╝██║     ███████║█████╗  
# ██║╚██╗██║██║   ██║██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  
# ██║ ╚████║╚██████╔╝██║  ██║██║  ██║╚██████╗██║  ██║███████╗
# ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
# °°°·._.··._.·°°°·.°·..·°¯°··°¯°·.·°.·°°°°·.·°·._.··._.·°°°

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

def port_scan(ip, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def check_single_subdomain(sub, domain, ports, online_links):
    url = f"https://{sub}.{domain}"
    headers = {'User-Agent': ua.random}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            ip_address = socket.gethostbyname(f"{sub}.{domain}")
            open_ports = port_scan(ip_address, ports) if ports else []
            ports_str = f" | Open Ports: {open_ports}" if open_ports else ""
            output_line = f"\n{Fore.GREEN}[ONLINE]{Style.RESET_ALL} {Fore.YELLOW}{ip_address}{Style.RESET_ALL} | {Fore.RED}{url}{Style.RESET_ALL}{ports_str}"
            print(output_line)
            online_links.append(f"{ip_address},{url},{open_ports}")
    except requests.RequestException:
        pass

def check_subdomains(domain, threads, ports, online_links):
    with open("SubDomains.txt", "r", encoding="utf8") as file:
        subdomains = [line.strip() for line in file.readlines()]

    total_subdomains = len(subdomains)

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_subdomain = {executor.submit(check_single_subdomain, sub, domain, ports, online_links): sub for sub in subdomains}
        for index, future in enumerate(concurrent.futures.as_completed(future_to_subdomain), start=1):
            future.result() 
            print_progress_bar(index, total_subdomains)

    if online_links:
        print("{Fore.GREEN}Writing the following links to online_links.txt{Style.RESET_ALL}:", online_links)
        with open("online_links.txt", "a", encoding="utf8") as output_file:
            for link in online_links:
                output_file.write(link + "\n")
    else:
        print("{Fore.RED}No online links found.{Style.RESET_ALL}")

def main():
    thread_count = 20
    port_options = {
        '1': [],
        '2': [3389],  # RDP port
        '3': [3389, 21, 22],  # RDP, FTP, SSH ports
        '4': [21, 22, 587, 1194, 3389, 5900] # FTP, SSH, SMTP, VPN, RDP, VNC
    }

    while True:
        try:
            port_choice = input(f"{Fore.BLUE}Choose port scan option (1. No scan 2. Scan RDP port 3. Scan RDP+FTP+SSH ports 4. Scan FTP, SSH, SMTP, VPN, VNC, RDP ports): {Style.RESET_ALL}")
            ports = port_options.get(port_choice, [])

            thread_input = input(f"{Fore.BLUE}Enter the number of threads to use (1-250, default 100): {Style.RESET_ALL}")
            if thread_input:
                thread_count = max(1, min(250, int(thread_input)))

            user_input = input(f"{Fore.BLUE}Enter domain(s) (comma-separated, e.g., example.com,example2.com): {Style.RESET_ALL}")
            domains = [domain.strip() for domain in user_input.split(",")]

            for domain in domains:
                online_links = []
                check_subdomains(domain, thread_count, ports, online_links)

            repeat = input(f"{Fore.YELLOW}Do you want to check another domain? (y/n): {Style.RESET_ALL}")
            if repeat.lower() != 'y':
                break
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Exiting...{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()


# Disclaimer:
# This code/script/application/program is solely for educational and learning purposes.
# All information, datasets, images, code, and materials are presented in good faith and
# intended for instructive use. However, noarche make no representation or warranty, 
# express or implied, regarding the accuracy, adequacy, validity, reliability, availability,
# or completeness of any data or associated materials.
# Under no circumstance shall noarche have any liability to you for any loss, damage, or 
# misinterpretation arising due to the use of or reliance on the provided data. Your utilization
# of the code and your interpretations thereof are undertaken at your own discretion and risk.
#
# By executing script/code/application, the user acknowledges and agrees that they have read, 
# understood, and accepted the terms and conditions (or any other relevant documentation or 
#policy) as provided by noarche.
#
#Visit https://github.com/noarche for more information. 
#
#  _.··._.·°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°°·.·°·._.··._
# ███╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗██╗  ██╗███████╗
# ████╗  ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
# ██╔██╗ ██║██║   ██║███████║██████╔╝██║     ███████║█████╗  
# ██║╚██╗██║██║   ██║██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  
# ██║ ╚████║╚██████╔╝██║  ██║██║  ██║╚██████╗██║  ██║███████╗
# ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
# °°°·._.··._.·°°°·.°·..·°¯°··°¯°·.·°.·°°°°·.·°·._.··._.·°°°