import ipaddress
#bu dosyada kullanıcıdan bilgi alma ve doğrulama işlemleri bulunmaktadır

def get_target():
    while True:
        target = input("IP adresini giriniz: ").strip()

        try:
            address = ipaddress.ip_address(target)

            if address.version != 4:
                print("[ERROR] Şimdilik yalnızca IPv4 destekleniyor.")
                continue

            return target

        except ValueError:
            print("[ERROR] Geçersiz IP adresi!")


def get_ports():
    while True:
        try:
            start, stop = map(
                int,
                input("Başlangıç ve bitiş portlarını giriniz: ").split()
            )

            if not (1 <= start <= stop <= 65535):
                print("[ERROR] Geçersiz port aralığı!")
                continue

            return start, stop

        except ValueError:
            print("[ERROR] İki geçerli port numarası giriniz!")