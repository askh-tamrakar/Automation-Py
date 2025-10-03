# Question 7: Write a Python script to check if a port is open on a given host.





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
from Scripts import q5 as logger_util
import socket
import ipaddress

# For to check single port on Both IPv4 and IPv6
def check_port(host: str, port: int, ipv6: bool = False, timeout: float = 2.0, debug: bool = True) -> bool:
    """
    Check if a TCP port is open on host.
    Returns True if OPEN, False if CLOSED or unreachable.

    Parameters:
        host: hostname or IP string
        port: integer port
        ipv6: if True, prefer IPv6. Otherwise prefer IPv4 (but function will try both if needed).
        timeout: connect timeout in seconds
        debug: if True, prints/logs exception details
    """
    log_file = "port_scanner.log"

    if not (0 <= port <= 65535):
        raise ValueError("port must be in 0-65535")

    message_base = f"Port {port} on {host} is "
    sock = None

    family_preference = socket.AF_INET6 if ipv6 else socket.AF_INET
    try:
        addrs = socket.getaddrinfo(host, port, family_preference, socket.SOCK_STREAM)

    except socket.gaierror as e:
        logger_util.log(log_file, f"{message_base}UNRESOLVED - {e}", 'e')

        if debug:
            print("getaddrinfo error:", e)

        return False

    for family, socktype, proto, canonname, sockaddr in addrs:
        try:
            sock = socket.socket(family, socktype, proto)
            sock.settimeout(timeout)
            # For IPv6 sockaddr may be (host, port, flowinfo, scopeid)
            err = sock.connect_ex(sockaddr)  # returns 0 on success
            if err == 0:
                logger_util.log(log_file, message_base + "OPEN", 'i')
                sock.close()
                return True
            else:
                if debug:
                    logger_util.log(log_file, f"connect_ex to {sockaddr} returned err={err}", 'd')
            sock.close()

        except Exception as exc:
            if debug:
                logger_util.log(log_file, f"Exception while connecting to {sockaddr}: {exc}", 'd')
            if sock:
                try:
                    sock.close()
                except Exception:
                    pass

    # if we get here, none succeeded
    print(message_base + "CLOSED")
    return False


# For to check range of ports on Both IPv4 and IPv6
def scan_ports(host, start_port, end_port, ipv6=False):
    print(f"\nScanning {host} from port {start_port} to {end_port} ({'IPv6' if ipv6 else 'IPv4'})...\n")
    
    open_ports = []
    for port in range(start_port, end_port + 1):
        if check_port(host, port, ipv6):
            open_ports.append(port)
    
    print("\nScan complete.")
    if open_ports:
        print("Open ports:", ", ".join(map(str, open_ports)))
    else:
        print("No open ports found.")

#===================================================================================================================

# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        print("\nOnly open ports are going to be logged")
        print("\nFormat: host: start_port-end_port OR host: port, debug = False or True")
        address = input("\n~~~> Give IPv4 or IPv6 address: \n===> ").strip()

        if address == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
            continue

        try:
            host, port_range = address.split(":", 1)
            host = host.strip()
            port_range = port_range.strip()

            # Determine if IPv4 or IPv6
            try:
                ip_obj = ipaddress.ip_address(host)
                ipv6 = ip_obj.version == 6
            except ValueError:
                # Could be a hostname, assume IPv4
                ipv6 = False

            if "-" in port_range:
                start_port, end_port = map(lambda x: int(x.strip()), port_range.split("-", 1))
                scan_ports(host, start_port, end_port, ipv6)
            else:
                port = int(port_range)
                print(f"\nChecking the availability of Port: {port} on Host: {host} ... \n")
                check_port(host, port, ipv6)

        except ValueError:
            print("Invalid format! Use host:port or host:start_port-end_port, debug = False or True")
        except Exception as e:
            print(f"Error: {e}")

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
