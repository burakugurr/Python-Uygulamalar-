import webbrowser as wb
import time
import sqlite3 as sql
from InstagramAPI import InstagramAPI
import tweepy
def veritabani():
    vt = sql.connect('tv.sqlite')
    imlec = vt.cursor()
    imlec.execute("CREATE TABLE IF NOT EXISTS program(TVad,Tvadres,Radyoad,Radyoadres,fbid,fbpas,instaid,instapas,twid,twpas)")
#func is here
def TV():
    global kanal_sec
    kanal_sec=int(input("Bir Kanal seçiniz... \n[1] TRT\n[2] SHOW\n[3] KANAL D\n[4] STAR\n[5] HABERTÜRK\n[6] TLC\n[7] CNN\n[8] NTV\n[9]Geri"))
    if(kanal_sec==1):
        wb.open_new("https://www.youtube.com/watch?v=DVOgoBnGAs0")
    elif(kanal_sec==2):
        wb.open_new("https://www.showtv.com.tr/canli-yayin")
    elif(kanal_sec==3):
        wb.open_new("https://www.kanald.com.tr/canli-yayin")
    elif(kanal_sec==4):
        wb.open_new("https://www.startv.com.tr/canli-yayin")
    elif(kanal_sec==5):
        wb.open_new("https://www.youtube.com/watch?v=s-KKgm4ysjk")
    elif(kanal_sec==6):
        wb.open_new("https://www.youtube.com/watch?v=IMy6RvwMJLs")
    elif(kanal_sec==7):
        wb.open_new("https://www.youtube.com/watch?v=I6ISnq4qyY0")
    elif(kanal_sec==8):
        wb.open_new("https://www.youtube.com/watch?v=XEJM4Hcgd3M")
    elif(kanal_sec==9):
        return 1
    else:
        print("HATALI İŞLEM")
        return 0
def Twitter():
    consumer_key = " "
    consumer_secret = " "
    access_token = " "
    access_token_secret = " "

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print("""
    -------------------------
    
    1-Tweet At
    2-Profil Görüntüle
    
    -------------------------
    """)
    secim=int(input("\nBir İşlem Seçin..."))
    if(secim==1):

        tweet=input("Tweet yazın:")
        api.update_status(tweet)
        print("Tweet Gönderildi")
    elif(secim==2):
        u_name=input("Kulllanıcı Adı Girin:")
        data=api.get_user(u_name)
        print(data)
    else:
        print("Hatalı işlem...")

def Instagramm(username,password):


    ig=InstagramAPI(username,password)
    ig.login()
    islemler=int(input("""
    1-Kullanıcı yayın akışı görüntüle
    2-Canlı Yayın Başlat
    """))
    if(islemler==1):
        ig.getTimeline()
    elif(islemler==2):
        import subprocess
        FILE_PATH = '/path/to/video/file'
        PUBLISH_TO_LIVE_FEED = False
        SEND_NOTIFICATIONS = False

        api = InstagramAPI(username,password, debug=False)
        assert api.login()

        # first you have to create a broadcast - you will receive a broadcast id and an upload url here
        assert api.createBroadcast()
        broadcast_id = api.LastJson['broadcast_id']
        upload_url = api.LastJson['upload_url']

        # we now start a boradcast - it will now appear in the live-feed of users
        assert api.startBroadcast(broadcast_id, sendNotification=SEND_NOTIFICATIONS)

        ffmpeg_cmd = "ffmpeg -rtbufsize 256M -re -i '{file}' -acodec libmp3lame -ar 44100 -b:a 128k -pix_fmt yuv420p -profile:v baseline -s 720x1280 -bufsize 6000k -vb 400k -maxrate 1500k -deinterlace -vcodec libx264 -preset veryfast -g 30 -r 30 -f flv '{stream_url}'".format(
            file=FILE_PATH,
            stream_url=upload_url.replace(':4343', ':80', ).replace('rtmps://', 'rtmp://'),
        )

        print(" Ctrl+C yaparak yayını sonlandırabilirsiniz")
        try:
            subprocess.call(ffmpeg_cmd, shell=True)
        except KeyboardInterrupt:
            print('Stop Broadcasting')

        assert api.stopBroadcast(broadcast_id)

        print('Yayın sona erdi')

        if PUBLISH_TO_LIVE_FEED:
            api.addBroadcastToLive(broadcast_id)
            print('Added Broadcast to LiveFeed')

def Interaktif():
    global secim
    secim=int(input("Uygulama Seçiniz: \n[1]FaceBook\n[2]İnstagram\n[3]Twitter\n[4]Youtube\n[5]Whatsapp\n[9]Geri"))
    if(secim==1):
        wb.open_new("https://www.facebook.com/")
    elif(secim==2):
        username = input("Kullanıcı adı giriniz:")
        password = input("Şifre giriniz:")
        Instagramm(username,password)
    elif(secim==3):
        Twitter()
        #wb.open_new("https://twitter.com/login?lang=tr")
    elif(secim==4):
        wb.open_new("https://www.youtube.com/")
    elif(secim==5):
        wb.open_new("https://web.whatsapp.com/")
    elif(secim==9):
        return 1
    else:
        print("HATALI İŞLEM YAPTINIZ..")
        return 0

def Radyo():
    global secim
    kanallar=["Fenomen","JoyTürk","PowerTürk","45likler"]
    adresler=["https://www.youtube.com/watch?v=KSe7H96-rS8","https://www.youtube.com/watch?v=VlNIxWdT_Yw","https://www.youtube.com/watch?v=qWmZKP2TzGc","https://www.youtube.com/watch?v=rtTDYzG9vXM"]

    def Radyoekle():
        kanalismi=input("Eklemek istediğiniz kanal ismi:")
        kanal=input("Kanal Adresi:")
        kanallar.append(kanalismi)
        adresler.append(kanal)

    for i in kanallar:
        print("[{}]\n".format(i))
    secim = int(input("Uygulama Seçiniz: \n[9]Geri\n[10]Radyo Kanalı Ekle\n"))

    if(secim==1):
        wb.open_new("https://www.youtube.com/watch?v=KSe7H96-rS8")
    elif(secim==2):
        wb.open_new("https://www.youtube.com/watch?v=VlNIxWdT_Yw")
    elif(secim==3):
        wb.open_new("https://www.youtube.com/watch?v=qWmZKP2TzGc")
    elif(secim==4):
        wb.open_new("https://www.youtube.com/watch?v=rtTDYzG9vXM")
    elif(secim==9):
        return 1
    elif(secim==10):
        Radyoekle()
        Radyo()
    else:
        print("HATALI İŞLEM..")
        return 0


"""
Main Loop
"""
# main loop
while True:
    print("----------- TV ------------\n")
    secimy=int(input("Merhaba bir işlem seçin\n\t1-TV 2-Radyo 3-İnteraktif 4-Kapat"))
    if(secimy==1):
        TV()
        print("---------------------------")
        if(TV()==0):
            continue
        elif(TV()==1):
            continue

    elif(secimy==2):
        Radyo()
        print("---------------------------")
        if(Radyo()==0):
            continue
        elif(Radyo()==1):
            continue
    elif(secimy==3):
        Interaktif()
        print("---------------------------")
        if(Interaktif()==0):
            continue
        elif(Interaktif()==1):
            continue
    elif(secimy==4):
        print("Sistem Kapatlıyor..")
        time.sleep(2)
        print(" : Hoşçakal : ")
        break
    else:
        print("HATALI İŞLEM YAPILDI\n")
        continue
print("----------------------")