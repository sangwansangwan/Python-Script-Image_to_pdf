#!/bin/bash

 
read -p "Enter the URL:" url


youtube-dl -F $url


read -p "Enter the Number:" num

youtube-dl -f 'num[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 $url

