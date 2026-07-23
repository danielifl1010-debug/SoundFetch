import yt_dlp
import os
import shutil
import glob

def download_song():
    song_name = os.environ.get("SONG_NAME", "יונתן שינפלד דרך חדשה")
    print(f"מוריד את השיר: '{song_name}', אנא המתן...")
    
    # יצירת תיקיית יעד ברורה
    os.makedirs("downloads", exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'default_search': 'ytsearch1',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/song.%(ext)s',
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}}
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_name])
            
        # לוודא שקובץ ה-mp3 קיים בתיקייה ולהדפיס את תוכנה
        files = glob.glob('downloads/*')
        print(f"קבצים שנמצאו בתיקיית ההורדות: {files}")
        
        print("ההורדה הסתיימה בהצלחה!")
    except Exception as e:
        print(f"שגיאה בהורדה: {e}")

if __name__ == "__main__":
    download_song()
