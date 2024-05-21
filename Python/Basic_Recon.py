import socket
import sys
import whois

def HTTPEnum():
    print('[-]creating socket[-]')
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(5)
    print('[+]socket created[+]')
    print("[+]connect with remote host[+]")
    target_host = input("[-]Enter Target IP[-]: ")
    print("[+]Target host is[+]: ", target_host)
    target_port = 80
    print("[+]Target Port[+]: ", target_port)
    s.connect((target_host,target_port))
    print('[+]Connection OK[+]')
    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
    s.send(request.encode())
    data=s.recv(4096).decode("utf-8")
    print("Data",(data))
    print("[+]Data Length[+]",len(data))
    print('[-]closing the connection[-]')
    s.close()

def version():
    try:
        s = socket.socket()
        s.settimeout(10)
        host = input("[-]Enter Target IP[-]: ")
        print("[+]Target host is[+]: ", host)
        port =int(input("[-]Enter Target port number[-]: "))
        print("[+]Target Port[+]: ", port)
        s.connect((host, port))
        service = socket.getservbyport(port)
        print('[+]Port: %s | => service: %s[+]'%(port, service))
        print("[+]\n",s.recv(1024).decode("utf-8"))
    except socket.error as e:
        print('[-]Process ',e, '[-]' )
        print("[-]Version Detection Process End[-]")
        main()


def domain_to_ip():
    try:
        domain = input("[-]Enter Domain to Resolve[-]")
        ip_address = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is: {ip_address}")
    except socket.gaierror as e:
        return f"Error: {e}"


def whois_query():
    try:
        domain = input("[-]Enter Domain name[-]")
        domain_info = whois.whois(domain)
        print(domain_info)
    except Exception as e:
        return f"Error: {e}"

        
def portcheck():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        host = input("[-]Enter IP Address[-]: ")
        print("[+]Target is[+]: ", host)
        port = int(input("[-]Enter Port number[-]: "))
        print("[+]Target Port is[+]: ", port)
        service = socket.getservbyport(port)
        if s.connect_ex((host, port)):
            print("[+]The port is closed[+]")
        else:
            print('[+]Port: %s | => service: %s[+]'%(port, service))
            print("[+]The port is open[+]")
    except s.error as e:
        print('[-]Process ',e, '[-]' )
        print("[-]Version Detection Process End[-]")
        main()

def main(): 
    choice = input("""\n[-]Enter Your Choice[-]
[1]HTTP Enumeraion
[2]Version Detection
[3]Port Checker
[4]Domain-to-IP
[5]Whois
[0]Exit\n""")
    print("[-]Processing[-]\n")
    if choice == '1':
        HTTPEnum()
        print("[-]HTTP Enumeration Process End[-]")
        main()
    elif choice == '2':
        version()
        main()
    elif choice == '3':
        portcheck()
        print("[-]Port Status Detection Process End[-]")
        main()
    elif choice == '4':
        domain_to_ip()
        print("[-]Domain name Resloving Done[-]")
        main()
    elif choice == '5':
        whois_query()
        print("[-]whois lookup process is Done[-]")
        main()
    elif choice == '0':
        sys.exit(1234)
    else:
        print("[-]You have wrong choice[-]")
        main()

main()
