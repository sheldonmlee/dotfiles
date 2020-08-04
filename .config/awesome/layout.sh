#!/bin/bash
# dmenu script to change Xorg layout
options="
1) US\n\
2) Colemak
"

option=$(echo -e $options | dmenu -i)

echo $option

case $option in 
1*)
	setxkbmap us
	;;
2*)
	setxkbmap us -variant colemak
	;;
esac
