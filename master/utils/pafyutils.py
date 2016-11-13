import pafy


sample_audio_url = "https://r6---sn-gwpa-w5pl.googlevideo.com/videoplayback?id=3d3dbf17ed5eb0f9&itag=251&source=youtube&requiressl=yes&gcr=in&initcwndbps=287500&pl=26&ms=au&mv=m&mn=sn-gwpa-w5pl&mm=31&ratebypass=yes&mime=audio/webm&gir=yes&clen=4405950&lmt=1469643231895394&dur=261.801&upn=7S--Gbp4CGk&key=dg_yt0&mt=1478960890&signature=09408C53D7E250D4D36806E2CECE60C9EC441247.3D55884EC8ADD65CC856AEFF8ECF2020806C5EEF&ip=47.9.234.249&ipbits=0&expire=1478982745&sparams=ip,ipbits,expire,id,itag,source,requiressl,gcr,initcwndbps,pl,ms,mv,mn,mm,ratebypass,mime,gir,clen,lmt,dur"

sample_video_url = "https://r6---sn-gwpa-w5pl.googlevideo.com/videoplayback?lmt=1478830965451507&mt=1478960890&mv=m&ms=au&mm=31&mn=sn-gwpa-w5pl&dur=261.851&id=o-ANfGrNr9i-zbcLA24EvqbVqw_fPVmzE29BYTQ-6ap94y&ei=_CcnWLO-FZa5ogOx-YyADA&upn=0B8emOpgRrU&gcr=in&key=yt6&ipbits=0&requiressl=yes&pl=26&ip=47.9.234.249&initcwndbps=287500&ratebypass=yes&itag=22&expire=1478982748&sparams=dur%2Cei%2Cgcr%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&source=youtube&mime=video%2Fmp4&signature=BBDD10934277F930EA5AD597918D53ADCCAA1296.C4D99F631BD0F3936339E704C6ECB912AD440DB1"

s = "http://redirector.googlevideo.com/videoplayback?itag=22&pl=24&gcr=us&mime=video%2Fmp4&nh=IgpwcjAzLmlhZDA3KgkxMjcuMC4wLjE&mn=sn-p5qlsnle&mm=31&hcs=yes&ratebypass=yes&shardbypass=yes&mv=m&mt=1478964111&ms=au&ei=YTQnWO32CcGRcaL1l6gM&lmt=1478830965451507&ip=159.253.144.86&key=yt6&expire=1478985921&dur=261.851&id=o-ANpEyOGZL82oeOxDX7jpki6PSV6yIo5ui81yuHS4PMrx&initcwndbps=3400000&source=youtube&sparams=dur%2Cei%2Cgcr%2Chcs%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Cshardbypass%2Csource%2Cupn%2Cexpire&ipbits=0&upn=xzMZ0alnl2I&signature=9B86EE7D77D7969C6FF2195906C365E40D3458DA.670F4641CA74F3495D8DE987F4F2AFE5A777B58E&title=The+Chainsmokers+-+Closer+%28Lyric%29+ft.+Halsey"



def pafy_audio_link():
    yt_url = "https://www.youtube.com/watch?v=PT2_F-1esPk"
    video = pafy.new(yt_url)

    # video_streams = video.streams
    audio_streams = video.audiostreams

    best_video_url = video.getbest(preftype="mp4").url
    best_audio_url = video.getbestaudio().url

    print "audio", best_audio_url
    print "video", best_video_url
