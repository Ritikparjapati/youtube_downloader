from pytube import YouTube
link="https://www.youtube.com/watch?v=JsvVTu0X9Nc"
youtube_1=YouTube(link)

print(youtube_1.title)                            #for download the title
print(youtube_1.thumbnail_url)                    #for download the thumbnail
 
videos= youtube_1.streams.all() 
vid=list(enumerate(videos))

for i in vid:
     print(i)
print()
strm=int(input("enter : "))
videos[strm].download()
print("succesfully")
