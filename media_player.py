import pafy
import vlc
import urllib.request
import re


class Player:
    url=""
    control="play"
    
    
###youtube_search_module###

    def youtube_url(keywords):
        
        arr=[]
        word=""
        a=0
        for i in range (len(keywords)):
            if(keywords[i]==" "):
                arr.append(word)
                a=a+1
                word=""
            elif(keywords[i]!=" "):
                word=word+keywords[i]
        arr.append(word) 
        keywords=""
        for i in range (len(arr)):
            keywords=keywords+arr[i]+"+"
        url="https://www.youtube.com/results?search_query="+keywords
        html=urllib.request.urlopen(url)
        video_ids=re.findall(r"watch\?v=(\S{11})",html.read().decode())
        ##print(video_ids)
        vid_url="https://www.youtube.com/watch?v="+video_ids[0]
        return vid_url

    ###VIDEO_Downloader_player###

    def downloader(url):
        video=pafy.new(url)
        vid=video.getbest().url
        return vid
    
    ###LOCAL-VIDEO-PLAYER###

    def media_player(url):
        media=vlc.MediaPlayer(url)
        media.play()
        print("CONTROLS")
        print("1.Pause")
        print("2.play")
        print("3.Stop")
        while(1):
            c=input("Input control: ")
            if(c=="pause"):
                media.pause()
            elif(c=="play"):
                media.play()
            elif(c=="stop"):
                media.stop()
                break
            else:
                print("Wrong command")
        media.release()

        input("press enter to quit")


    def get_local_url(keywords):
        url=Player.youtube_url(keywords)
        vid_url=Player.downloader(url)
        return vid_url
    
    
    ###Youtube video player###

    def play_youtube_vid(name):
        url=Player.youtube_url(name)
        vid=Player.downloader(url)
        Player.media_player(vid)












