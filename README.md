## Overview ##

This tool creates an executable file that establishes a reverse shell connection to a specified IP address and port. The builder.py script takes three arguments from the command line: the IP address, port number, and the filename for the output executable. It then obfuscate the modified file using @acheong08 tool called py-obfuscate [compress.py] before creating and executable file that fits the currentused system. The generated executable file is built using PyInstaller.

The generated executable file connects to a hardcoded IP address and port number and awaits commands from the attacker. The RevShell.py file is the code that will be executed on the victim's machine once the attacker has successfully established a connection. The code within RevShell.py is an obfuscated reverse shell that allows the attacker to execute commands on the victim's machine.

## Usage ##

<b>#Important!#</b1>
* Use the builder script at the same system as the target machine , build on linux for linux targets, build on windows for windows targets

* Clone the repository or download the code.
* Navigate to the directory that contains the builder.py script.

* Run the following command [filename must be different then RevShell.py]: <b>python builder.py IP-address port-number output-filename</b> 
Once the script has finished executing, the generated executable file will be located at dist in the same directory as the builder.py script.

* On the attacker's machine, establish a netcat listener on the specified port: nc -lvp <port number>.
* Transfer the generated executable file to the victim's machine.
* Run the executable file on the victim's machine.

The victim's machine will connect to the attacker's machine, and the attacker will be able to execute commands on the victim's machine through the netcat listener.
Note that the IP address and port number used in the builder.py script and the RevShell.py file are hardcoded and should be modified to match the IP address and port number that the attacker will use.

## Tools & Dependencies ##

# Tools #

Python 3
PyInstaller 

# Dependencies #

socket
subprocess
os
base64

## To install PyInstaller, run the following command ##

bash
Copy code
pip install pyinstaller

# The dependencies listed above are standard Python libraries and should be included with any Python distribution #

Before running the builder.py script, make sure that all required tools and dependencies are installed and accessible from the command line.
<b>And Again use the builder script at the same system as the target machine , build on linux for linux targets, build on windows for windows targets.</b>

## Disclaimer ##
This tool is provided for educational purposes only. Misuse of this tool to gain unauthorized access to computer systems is strictly prohibited. The author assumes no liability for any damages caused by the use or misuse of this tool.
