#!/usr/bin/bash
mkdir -p ~/youtube_data/youtube_data
while read p; do
	python3 download_youtube_data.py $p >~/youtube_data/$p
done <video_ids.txt
