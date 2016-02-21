instructions = [
    {
        "description": "Update",
        "command": "sudo apt-get update\nsudo apt-get upgrade",
        "linenums": False
    },
    {
        "description": "Create install_cec.sh",
        "command": '''#!/bin/bash

# by EMJB Thu Jul 30, 2015
# https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=117019
# This script is intended to install the latest version of libcec on a Pi running Raspbian
# It has been tested on Pi1 & Pi2 using the latest Raspbian as of 26/7/2015 and CEC version 3.0.1
# To run this file "bash /xxxx/TRANSCEND/libcecinstall.sh" where xxxx is the directory where this file is held
# or "rm /tmp/libcecinstall.log -f && bash /xxxx/TRANSCEND/libcecinstall.sh  |& tee /tmp/libcecinstall.log" if you want a log file
# Thanks to Alexander P, Sam Nazarko, nlrb & gkreidl for the inputs that enabled me to get this working

COLOUR='\033[0;31m' # Red
NC='\033[0m' # No Color
echo
echo -e ${COLOUR}"Running libcec installation script${NC}"
echo
echo "Installing the prerequisites for building libcec:"
sudo apt-get install git cmake g++-4.8 checkinstall liblockdev1-dev libudev-dev libxrandr-dev python-dev swig
sudo apt-get install libraspberrypi-dev
echo
echo -e ${COLOUR}"Cloning the Pulse-Eight libcec repository:"${NC}
echo
mkdir /home/pi/libcecworkarea
cd /home/pi/libcecworkarea
git clone --recursive https://github.com/Pulse-Eight/libcec.git
echo
echo -e ${COLOUR}"Creating the cec platform library:"${NC}
echo
cd /home/pi/libcecworkarea/libcec/src/platform
mkdir build
cd build
cmake -DRPI_INCLUDE_DIR=/opt/vc/include -DRPI_LIB_DIR=/opt/vc/lib -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=1 -DCMAKE_CXX_COMPILER=g++-4.8 ..
make
sudo make install
echo
echo -e ${COLOUR}"Building libcec:"${NC}
echo
cd /home/pi/libcecworkarea/libcec
mkdir build
cd build
export LIBRARY_PATH=/opt/vc/lib
cmake -DRPI_INCLUDE_DIR=/opt/vc/include -DRPI_LIB_DIR=/opt/vc/lib -DCMAKE_CXX_COMPILER=g++-4.8 -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=1 ..
make
sudo -E bash -c 'make install'
echo
echo -e ${COLOUR}"libcec installation script completed\\n"${NC}
echo''',
        "linenums": True
    },
    {
        "description": "Go Home",
        "command": "cd",
        "linenums": False
    },
    {
        "description": "Install pip",
        "command": "sudo apt-get install python-pip",
        "linenums": False
    },
    {
        "description": "Install Flask",
        "command": "sudo pip install flask",
        "linenums": False
    },
    {
        "description": "Clone the PiPyMote repo",
        "command": "git clone https://github.com/daftscience/PiPyMote.git",
        "linenums": False
    },
    {
        "description": "Test it out",
        "command": "cd pipymote\npython pipymote",
        "linenums": False}
]

advanced_instructions = [

    {
        "description": "install gunicorn",
        "command": "sudo apt-get install gunicorn",
        "linenums": False
    },
    {
        "description": "Install Supervisorctl",
        "command": "sudo apt-get install supervisor",
        "linenums": False
    },
    {
        "description": "Configure Supervisorctl",
        "command": "sudo nano /etc/supervisor/conf.d/pipymote.conf",
        "linenums": False
    },
    {
        "description": "Add the following",
        "command": '''[program:pipymote]
command = gunicorn pipymote:app -b 0.0.0.0:5000
directory = /home/pi/pipymote
user = pi''',
        "linenums": True
    },
    {
        "description": "Start supervisor",
        "command": '''sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start flask_project
''',
        "linenums": False
    }

]
