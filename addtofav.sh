#!/bin/bash

filepath="$1"

/usr/bin/tmsu tag "'${filepath}'" "favorites" ; show-text "Added to Favorites!" 3000
echo '{ "command": ["show-text", "Added to Favorites", 3000] }' | socat - /tmp/mpvsocket 
