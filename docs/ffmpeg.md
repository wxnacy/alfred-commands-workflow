## ffmpeg -i
**m3u8 转为 mp4**
```
ffmpeg -i <m3u8-file> -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 <mp4-file>
```
## ffmpeg -ss
**截取视频**
```
ffmpeg -ss <start> -t <end> -i <sourcefile> -vcodec copy -acodec copy <outputfile>
```
