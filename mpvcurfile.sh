#!/bin/bash

echo '{ "command": ["get_property", "path"] }' | socat - /tmp/mpvsocket
