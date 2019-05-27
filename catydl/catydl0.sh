#!/bin/zsh

catfile="$1"
catfiles="$*"

firstfilelength=$(wc -l "${catfile}")
echo $firstfilelength
# if [ -n "$1" ] && [ -z "$2" ]; then
#     echo "$1"
#     cat "$1" | xpanes -c "youtube-dl {}"
# elif [ -n "$2" ]; then
#     echo "Only 1 file allowed!!!"
#     exit
# fi

