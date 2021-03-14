import os
import eyed3


def get_music_metadata(music_file_paths):
    music_metadata = []
    for song in music_file_paths:
        try:
            audiofile = eyed3.load(song)                          
            if audiofile:                                                        
                music_metadata.append({                        
                    'artist': audiofile.tag.artist,      
                    'title': audiofile.tag.title,        
                    'album': audiofile.tag.album,            
                    'track_number': audiofile.tag.track_num,
                    'file_path': song
                })
        except Exception as e:
            print(e)
            pass
    
    return music_metadata


def sort_music_by_metadata(music_metadata):
    for track in music_metadata:
        try:
            if track['artist'] != None and track['album'] != None:
                if not os.path.exists(track['artist']):    
                    os.mkdir(f"{track['artist']}/")  
                    print(f"Creating {track['artist']}/")

                if not os.path.exists(f"{track['artist']}/{track['album']}"):    
                    os.mkdir(f"{track['artist']}/{track['album']}")
                    print(f"Creating {track['artist']}/{track['album']}/")
    
                print(f"Moving {track['file_path']} to {track['artist']}/{track['album']}")
                os.rename(track['file_path'], f"{track['artist']}/{track['album']}/{track['file_path']}")

            if track['artist'] != None and track['album'] == None:
                if not os.path.exists(track['artist']):    
                    os.mkdir(f"{track['artist']}/")  
                    print(f"Creating {track['artist']}/")
         
                print(f"Moving {track['file_path']} to {track['artist']}/")
                os.rename(track['file_path'], f"{track['artist']}/{track['file_path']}")
  
        except Exception as e:
            print(e)
            pass


def sort_music_in_cwd():
    files = os.listdir()
    music_files = [file for file in files if file.endswith('.mp3')]
    music_metadata = get_music_metadata(music_files)

    return sort_music_by_metadata(music_metadata)


if __name__ == '__main__':
    sort_music_in_cwd()
