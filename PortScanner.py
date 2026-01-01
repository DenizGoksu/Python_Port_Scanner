import socket
import argparse
import threading
from datetime import datetime
from colorama import Fore, Style # Terminali renklendirmek için

def port_scanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            try:
                # Servis bilgisini almaya çalış (Banner Grabbing)
                banner = s.recv(1024).decode().strip()
                print(f"{Fore.GREEN}[+] Port {port} AÇIK! {Fore.YELLOW} -> {banner}{Style.RESET_ALL}")
            except:
                print(f"{Fore.GREEN}[+] Port {port} AÇIK!{Style.RESET_ALL}")
        s.close()
    except:
        pass

def main():
    # Komut satırı argümanları
    parser = argparse.ArgumentParser(description="Aşko-Scan v2.0 | Profesyonel Port Tarayıcı")
    parser.add_argument("-t", "--target", help="Hedef IP Adresi", required=True)
    parser.add_argument("-p", "--ports", help="Port Aralığı (Örn: 1-1000)", default="1-1024")
    args = parser.parse_args()

    target_ip = socket.gethostbyname(args.target)
    start_port, end_port = map(int, args.ports.split("-"))

    print(f"{Fore.CYAN}Tarama Başlatıldı: {target_ip} ({datetime.now()}){Style.RESET_ALL}")
    
    # Threading ile hızlandırma
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=port_scanner, args=(target_ip, port))
        threads.append(t)
        t.start()

if __name__ == "__main__":
    main()