![image](https://user-images.githubusercontent.com/97190263/224012280-5eb628ed-98a1-45e1-83ef-e5367c1c4383.png)



## Overview ##

This tool creates an executable file that establishes a reverse shell connection to a specified IP address and port. The builder.py script takes three arguments from the command line: the IP address, port number, and the filename for the output executable. It then obfuscate the modified file using <b>@acheong08</b> tool called py-obfuscate [compress.py] before creating an executable file that fits the current used system. The generated executable file is built using PyInstaller.

The generated executable file connects to a hardcoded IP address and port number and awaits commands from the attacker. The RevShell.py file is the code that will be executed on the victim's machine once the attacker has successfully established a connection. The code within RevShell.py is an obfuscated reverse shell that allows the attacker to execute commands on the victim's machine.

## Usage ##

<b>#Important!#</b>
* Use the builder script at the same system as the target machine , build on linux for linux targets, build on windows for windows targets

* Clone the repository or download the code.
* Navigate to the directory that contains the builder.py script.
* pip install -r requirements.txt
* pip install pyinstaller [make sure it is in your path after it has been installed]

* Run the following command [If you want the script to generate a bat file using your preferred input payload in the startup directory, you have the option of renaming RevShellWithStartup.py to RevShell.py.]:
<b>python3 builder.py IP PORT OutputFileName</b> 
Once the script has finished executing, the generated executable file will be located at dist in the same directory as the builder.py script.

* On the attacker's machine, establish a netcat listener on the specified port: nc -lvp <port number>.
* Transfer the generated executable file to the victim's machine.
* Run the executable file on the victim's machine.

The victim's machine will connect to the attacker's machine, and the attacker will be able to execute commands on the victim's machine through the netcat listener.
Note that the IP address and port number used in the builder.py script and the RevShell.py file are hardcoded and should be modified to match the IP address and port number that the attacker will use.

## Tools & Dependencies ##

# Tools #

* Python 3
* PyInstaller 

# Dependencies #

* socket
* cryptography
* pystyle
* subprocess
* os
* base64


# The dependencies listed above are standard Python libraries and should be included with any Python distribution #

Before running the builder.py script, make sure that all required tools and dependencies are installed and accessible from the command line.
<b>And Again use the builder script at the same system as the target machine , build on linux for linux targets, build on windows for windows targets [you can try using wine to compile exe on linux].</b>

## Disclaimer ##
This tool is provided for educational purposes only. Misuse of this tool to gain unauthorized access to computer systems is strictly prohibited. The author assumes no liability for any damages caused by the use or misuse of this tool.
