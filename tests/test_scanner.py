import socket
import ipaddress
import time

def get_target():
    while True:
        target(input("ip numarasını girin: ")).strip()
        
        try:
            ipaddress.ip_address(target)
            return target
        except ValueError:
            print("ERROR, geçersiz ip adresi!")


def get_ports():
    while True:
        try:
            start, stop=map(
                int,
                input("başlangıç ve bitiş portlarını giriniz:" \
                "").split()
            )
            if not (1 <= start <= stop <= 65535):
                print("[ERROR] Port aralığı geçersiz!")
                continue
        
            return start, stop
    
        except ValueError:
            print("ERROR, port numaraları yanlış girilmiş")

def scan_port(target, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
            # Bağlantıyı burada deneyeceksin.
            return sock.connect_ex((target, port)) == 0
        
        except OSError:
            return False

def main():

    target=get_target()
    start, stop= get_ports()

    start_time=time.time()
    open_ports=[]

    for ports in range(start ,stop+1):
        if scan_port(target, port):
            print(f"port {port} open")
            open_ports.append(port)

    elapsed=time.time() - start_time
    
    print("\n========== RESULTS ==========")
    print(f"Target: {target}")
    print(f"Open ports: {len(open_ports)}")
    print(f"Scan duration: {elapsed:.2f} seconds")
    print("=============================")


if __name__ == "__main__":
    main()