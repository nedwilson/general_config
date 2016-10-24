# general_config

This repository contains the general configuration files for the In-House pipeline. This has been tested on MacOS 10.11.5 (El Capitan) and CentOS Linux 7.2. In theory it should also work on Windows systems, but it has not been tested.

# WARNING

Setting up this pipeline will make configuration changes to system files, and could end in absolute disaster. Do not run any of this stuff unless you are aware of what it does, and more importantly, you know how to put the system back into a pristine state. This also assumes that you have a VANILLA install of Nuke that you have not customized in any way. If you have customized your Nuke installation, take care when copying the various init.py files. 

# GENERAL SETUP - ALL PLATFORMS

~~~~
git clone https://github.com/nedwilson/general_config.git
cd general_config
~~~~

# SETUP - MACOS

Open etc-environment in the text editor of your choice, enter the correct show code, config file path, and show root path, and then run the following commands in the Terminal:

~~~~
sudo cp ./Library-LaunchAgents-environment.user.plist /Library/LaunchAgents/environment.user.plist
sudo chmod 600 /Library/LaunchAgents/environment.user.plist
sudo cp ./Library-LaunchDaemons-environment.plist /Library/LaunchDaemons/environment.plist
sudo chmod 600 /Library/LaunchDaemons/environment.plist
sudo cp ./etc-environment /etc/environment
sudo chmod 755 /etc/environment
cp Users-ned-dotnuke-init.py $HOME/.nuke/init.py
mkdir -p $HOME/.nuke/Python/Startup/
cp ./Users-ned-dotnuke-Python-Startup-init.py $HOME/.nuke/Python/Startup/
sudo reboot
~~~~

# SETUP - CENTOS LINUX 7

Open etc-profile.d-environment.sh in the text editor of your choice, enter the correct show code, config file path, and show root path, and then run the following commands in the Terminal:

~~~~
sudo cp ./etc-environment /etc/profile.d/environment.sh
sudo chmod 755 /etc/profile.d/environment.sh
cp Users-ned-dotnuke-init.py $HOME/.nuke/init.py
mkdir -p $HOME/.nuke/Python/Startup/
cp ./Users-ned-dotnuke-Python-Startup-init.py $HOME/.nuke/Python/Startup/
sudo reboot
~~~~

# SETUP - WINDOWS 10 - NOT TESTED

Add the following System environment variables:

~~~~
IH_SHOW_CODE
IH_SHOW_ROOT
IH_SHOW_CFG_PATH
~~~~

There is a decent write-up on how to do this here:

http://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10

In the command shell, assuming you have cloned the git repository and have changed directory into it, try the following:

~~~~
COPY .\Users-ned-dotnuke-init.py %USERHOME%\.nuke\init.py
MKDIR %USERHOME%\.nuke\Python\Startup\
COPY .\Users-ned-dotnuke-Python-Startup-init.py %USERHOME%\.nuke\Python\Startup\
~~~~

After that, reboot, and let me know if it works!

