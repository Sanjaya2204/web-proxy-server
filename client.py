import socket

def main():
    proxy_host = "172.16.7.164"  
    proxy_port = 5050 

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((proxy_host, proxy_port))

        request = "GET / HTTP/1.1\r\n Host: www.example.com\r\n\r\n"
        s.sendall(request.encode('utf-8'))

        
        response = s.recv(4096)
        print(response.decode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    main()