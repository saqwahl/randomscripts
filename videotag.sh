#!/bin/bash

IFS=$'\n'
allvids=$(find ~/Downloads -name '*.mp4' -or -name '*.wav' -or -name '*.mkv' -or -name '*.avi' -or -name '*.flv')
tmsu --verbose tag --tags "media video" -- $allvids

