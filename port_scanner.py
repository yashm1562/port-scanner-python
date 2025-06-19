import socket

# Ask user for target
target = input("Enter IP or Website to scan: ")

# Common ports to check
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]

print(f"\nScanning {target}...\n")

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout for response
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} is OPEN")
    else:
        print(f"❌ Port {port} is CLOSED")
    sock.close()
