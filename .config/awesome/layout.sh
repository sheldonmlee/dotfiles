#!/bin/bash
# dmenu script to change Xorg layout
options="
1) US\n\
2) Colemak
"

# dmenu
#option=$(echo -e $options | dmenu -i)
# rofi emulation of dmenu
option=$(echo "1) US|2) Colemak" | rofi -dmenu -sep '|' -i)

echo $option

case $option in 
1*)
	setxkbmap us
	;;
2*)
	setxkbmap us -variant colemak
	;;
esac
