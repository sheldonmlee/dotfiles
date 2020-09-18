#!/bin/bash

#screenshots using scrot
scrot_dir=$HOME/screenshots/
date_format='%Y-%m-%d_%H-%M-%S'
s_scrot() {
	name=$(date +${date_format}_sel.png)
	path="${scrot_dir}${name}"
	scrot -s $path
}

f_scrot() {
	name=$(date +${date_format}_full.png)
	path="${scrot_dir}${name}"
	scrot $path
}

#cd into config dir
cfdir()
{
	cd $HOME/.config/$1
}
