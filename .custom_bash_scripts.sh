#!/bin/bash

#screenshots using scrot
scrot_dir=$HOME/screenshots/

s_scrot() {
	name=$(date +%Y-%m-%d_%H-%M_sel.png)
	path="${scrot_dir}${name}"
	scrot -s $path
}

f_scrot() {
	name=$(date +%Y-%m-%d_%H-%M_full.png)
	path="${scrot_dir}${name}"
	scrot $path
}
