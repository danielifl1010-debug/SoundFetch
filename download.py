import yt_dlp
import os
import glob

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
        'outtmpl': 'output_song.%(ext)s',
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}}
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_name])
        print("ההורדה הסתיימה בהצלחה!")
        
        # הדפסת כל הקבצים בתיקייה ליתר בטחון
        print("קבצים בתיקייה:", glob.glob('*'))
        
    except Exception as e:
        print(f"שגיאה בהורדה: {e}")

if __name__ == "__main__":
    download_song()
