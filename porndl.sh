#!/bin/bash

ytdldir="$HOME/Downloads/ytdl"
url=$1

site=$(echo "$url" | awk -F'.' '{print $2}')
spanksite=$(echo "$url" | awk -F'.' '{print $1}')

if [ $site == "eporner" ]; then
    echo "SITE IS EPORNER!"
    cd "$ytdldir/eporner"
    youtube-dl "$url"
elif [ $spanksite == "https://spankbang" ]; then
    echo "SITE IS SPANKBANG!"
    cd "$ytdldir/spankbang"
    youtube-dl "$url"
elif [ $site == "pornhub" ]; then
    echo "SITE IS PORNHUB!"
    cd "$ytdldir/pornhub"
    youtube-dl "$url"
else
    echo "SITE NOT RECOGNIZED!"
    cd "$ytdldir/misc"
    youtube-dl "$url"
fi
