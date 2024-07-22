import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...\n")
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set timeout to 1 second
            sock.settimeout(1)
            
            # Attempt to connect to the target's port
            result = sock.connect_ex((target, port))
            
            # Check if the port is open
            if result == 0:
                print(f"Port {port}: Open")
                
            # Close the socket connection
            sock.close()
        
        except KeyboardInterrupt:
            print("\nExiting program...")
            break
        
        except socket.error:
            print("Couldn't connect to server.")
            break

# Define the target IP address or hostname
target = "localhost"

# Define the range of ports to scan
start_port = 1
end_port = 100

# Call the scan_ports function
scan_ports(target, start_port, end_port)