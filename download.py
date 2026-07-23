import yt_dlp

def download_song():
    song_name = input("הכנס את שם השיר שתרצה להוריד: ")
    print(f"מוריד את השיר: '{song_name}', אנא המתן...")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'default_search': 'ytsearch1',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}}
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_name])
        print("ההורדה הסתיימה בהצלחה!")
    except Exception as e:
        print(f"שגיאה בהורדה: {e}")

if __name__ == "__main__":
    download_song()
