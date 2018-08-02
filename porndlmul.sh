#!/bin/bash

ytdldir="$HOME/Downloads/ytdl"



url=$*

for i in $url;do

    site=$(echo "$i" | awk -F'.' '{print $2}')
    spanksite=$(echo "$i" | awk -F'.' '{print $1}')

    if [ $site == "eporner" ]; then
        echo "SITE IS EPORNER!"
        cd "$ytdldir/eporner"
        echo "URL is: $i"
        youtube-dl "$i"

    elif [ $spanksite == "https://spankbang" ]; then
        echo "SITE IS SPANKBANG!"
        cd "$ytdldir/spankbang"
        echo "URL is: $i"
        youtube-dl "$i"

    elif [ $site == "pornhub" ]; then
        echo "SITE IS PORNHUB!"
        cd "$ytdldir/pornhub"
        echo "URL is: $i"
        youtube-dl "$i"

    else
        echo "SITE NOT RECOGNIZED!"
        cd "$ytdldir/misc"
        echo "URL is: $i"
        youtube-dl "$i"
    fi

done
