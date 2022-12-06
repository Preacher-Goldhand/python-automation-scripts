# Description:
# Youtube videos downloader with saving on a local machine

from pytube import YouTube              # Youtube downloader 

SAVE_TO = "D:/"                         # Path to save videos
links = open('yt_links.txt', 'r')       # Links of videos

for i in links:
    try:
        yt = YouTube(i)
    except:
        print("Something went wrong... Connection error")

    # Filter all .mp4 extensions    
    mp4_files = yt.filter('mp4') 

    # Getting videos with their resolution      
    dest_videos = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
    
    try:
        # Downloading the videos to the save path
        dest_videos.download(SAVE_TO)
    except:
        print("Something went wrong...")
print("Videos has been dowloaded successfully!")

