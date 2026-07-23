import yt_dlp
import os

def download_song():
    song_name = os.environ.get("SONG_NAME", "יונתן שינפלד דרך חדשה")
    print(f"מוריד את השיר: '{song_name}', אנא המתן...")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'default_search': 'ytsearch1',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'song.%(ext)s',
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}}
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(song_name, download=True)
            filename = ydl.prepare_filename(info)
            print(f"שם הקובץ המקורי: {filename}")
        print("ההורדה הסתיימה בהצלחה!")
    except Exception as e:
        print(f"שגיאה בהורדה: {e}")

if __name__ == "__main__":
    download_song()
