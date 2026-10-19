import time

from netscope.scanner import scan_port
from netscope.utils import get_target, get_ports


def main():

    print("\n========== NETSCOPE v1.1 ==========\n")

    target = get_target()
    start, stop = get_ports()

    print(f"\n[*] Scanning {target}...\n")

    start_time = time.time()

    open_ports = []

    for port in range(start, stop + 1):

        if scan_port(target, port):
            print(f"[+] Port {port} OPEN")
            open_ports.append(port)

    elapsed = time.time() - start_time

    print("\n========== RESULTS ==========")
    print(f"Target: {target}")
    print(f"Open ports: {len(open_ports)}")
    print(f"Scan duration: {elapsed:.2f} seconds")
    print("=============================")


if __name__ == "__main__":
    main()