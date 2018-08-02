#!/bin/bash
for i in $HOME/Downloads/firefox/*.torrent;do
    detox "$i"
done

for i in $HOME/Downloads/firefox/*.torrent;do
    mv "$i" "$HOME/Downloads/torfiles/$i"
done

