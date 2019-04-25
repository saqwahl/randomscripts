#!/bin/bash

echo '{ "command": ["get_property", "path"] }' | socat - /tmp/mpvsocket


ln -s $(echo '{ "command": ["get_property", "path"] }' \
    | socat - /tmp/mpvsocket \
    | awk -F'"' '{print $4}') \
    $HOME/.bestvids/

