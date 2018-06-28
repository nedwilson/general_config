#!/bin/bash

# copies files into their respective system folders.
# only works with macOS.
# will not overwrite existing .nuke/init.py or system files. copy manually in this case.

if [ ! -e /etc/environment ]; then
	echo "Creating /etc/environment."
	sudo cp -v ./etc-environment /etc/environment
	sudo chmod 755 /etc/environment
else
	echo "Warning: /etc/environment exists."
fi

if [ ! -e /Library/LaunchAgents/environment.user.plist ]; then
	echo "Creating /Library/LaunchAgents/environment.user.plist."
	sudo cp -v ./Library-LaunchAgents-environment.user.plist /Library/LaunchAgents/environment.user.plist
	sudo chmod 644 /Library/LaunchAgents/environment.user.plist
else
	echo "Warning: /Library/LaunchAgents/environment.user.plist exists."
fi

if [ ! -e /Library/LaunchDaemons/environment.plist ]; then
	echo "Creating /Library/LaunchDaemons/environment.plist."
	sudo cp -v ./Library-LaunchDaemons-environment.plist /Library/LaunchDaemons/environment.plist
	sudo chmod 644 /Library/LaunchDaemons/environment.plist
else
	echo "Warning: /Library/LaunchDaemons/environment.plist exists."
fi

if [ ! -e $HOME/.nuke/init.py ]; then
	echo "Creating $HOME/.nuke/init.py."
	cp -v ./Users-ned-dotnuke-init.py $HOME/.nuke/init.py
	chmod 775 $HOME/.nuke/init.py
else
	echo "Warning: $HOME/.nuke/init.py exists."
fi

if [ ! -e $HOME/.bash_profile ]; then
    echo "Creating $HOME/.bash_profile."
    cp -v ./Users-ned-dotbash_profile $HOME/.bash_profile
    chmod 775 $HOME/.bash_profile
else
    echo "Warning: $HOME/.bash_profile exists."
fi

if [ ! -e $HOME/.nuke/Python/Startup/init.py ]; then
	echo "Creating $HOME/.nuke/Python/Startup/init.py."
	mkdir -p $HOME/.nuke/Python/Startup
	cp -v ./Users-ned-dotnuke-Python-Startup-init.py $HOME/.nuke/Python/Startup/init.py
	chmod 775 $HOME/.nuke/Python/Startup/init.py
else
	echo "Warning: $HOME/.nuke/Python/Startup/init.py exists."
fi
