#!/bin/bash

walldir="$HOME/Pictures/Wallpapers"
interval=${1:-30}
directory=${2:-$walldir}

procfile="/tmp/autowall.proc"
touch $procfile

while [ -f "$procfile" ] ; do
    "$HOME/.local/bin/randwall"
    sleep $interval
done

