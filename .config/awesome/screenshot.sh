#!/bin/bash
#dmenu script for screenshots
CUSTOM_SCRIPTS_FILE=~/.custom_bash_scripts
if test -f $CUSTOM_SCRIPTS_FILE; then
	source $CUSTOM_SCRIPTS_FILE
else
	echo ".custom_bash_scripts.sh does not exist."
fi

options="
1) Fullscreen\n\
2) Selection
"
#echo -e $options

# -i case insensitive
# -l vertical lines
option=$(echo -e $options | dmenu -i)

#echo "\"$option\""
case $option in 
1*)
	sleep 0.5
	f_scrot
	;;
2*)
	s_scrot
	;;
esac

