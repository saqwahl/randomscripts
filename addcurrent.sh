#!/bin/bash

curfile=$(echo '{ "command": ["get_property", "path"] }' | socat - /tmp/mpvsocket | underscore select .data --outfmt text)

echo "$curfile" >> "$1.m3u"
