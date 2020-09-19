#!/bin/bash

function run()
{
	if ! pgrep -f $1; then
		$1&
	fi
}

run firefox
run discord
run alacritty
