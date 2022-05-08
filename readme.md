# YaMusicToYtMusic - copy your Yandex music playlist to Youtube music

## How To

### YtMusic:
1. open youtube music in chrome and open developer console
2. press F5
3. go to Network
4. select request that looks like `browse?`
5. scroll to request headers and copy all from `accept: */*` to end
6. create `raw_headers.txt` file
7. paste headers to this file

### YaMusic
1. open your yamusic playlist in chrome and open developer console
2. press F5
3. go to Network
4. select request that looks like `playlist.jsx?`
5. copy request URL
6. create `playlist.txt` file
7. paste url to this file

### Finally
1. run `main.py` file 
2. answer `y` on question
3. don't use yt music to end of progress
* !!! some music may be not found on yt music