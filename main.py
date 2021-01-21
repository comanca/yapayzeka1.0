from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import webbrowser
import time
import random
import sys



dosya1 = open("kelimeler.txt","r")
kelime_list = dosya1.readlines()
dosya1.close()
driver_path = "C:/Users/hakan/OneDrive/Masaüstü/kodlar/yapayzeka1.3/driver/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/hakan/AppData/Local/Google/Chrome/User Data/Default")
buyukAlfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
br = webdriver.Chrome(driver_path, options=options)
br.set_window_size(800, 500)
br.get("https://translate.google.com/?sl=auto&tl=tr&op=translate")
time.sleep(6)
if br.title == "Google Çeviri":
    try:
        br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/div/div[2]/div/div/span/button[1]""").click()
        dil = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[1]/div/div[2]/input""").send_keys("türkçe",Keys.ENTER)
        time.sleep(1)
        print("Sistem hazır")
    except:
        print("bir hata oluşdu kod 0001")
        br.close()
        exit()
else: 
    print("bir hata oluşdu")
    br.close()
    print("Sistem kapanıyor")
    time.sleep(2)
    exit()
def lower(kelimeilk:str):
    yenikelime = str()
    kelime = kelimeilk.replace(".","")
    kelime = kelime.replace("?","")
    kelime = kelime.replace(",","")
    kelime = kelime.strip()
    for i in kelime:
        if i in kelime:
            if i in buyukAlfabe:
                index = buyukAlfabe.index(i)
                yenikelime += kucukAlfabe[index]
            else:
                yenikelime += i
    return yenikelime
def havali(parametre, time_sleep = 0.04):
    soz=[]
    for i in parametre+"\n":
        soz.append(i)
        time.sleep(time_sleep)
        sys.stdout.write(str(soz[0]))
        sys.stdout.flush()
        soz.remove(i) 
def konuş(bilgi):
    bekle = len(bilgi)/10+0.6
    havali("Algılanıyor...")
    try:
        br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[2]/div/div/span/button""").click()
    except:
        havali("Algılanamadı")
    try:
        yaz = br.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea""")
        yaz.send_keys(bilgi)
        yaz.send_keys(Keys.ENTER)
        br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[5]/div[1]/div/div[2]/div/span/button""").click()
    except:
        havali("hata kodu 0002")
        br.close()
        exit()
    bilgison = str
    bilgison = "Asistan:" + bilgi
    havali(bilgison)
    time.sleep(bekle)
def sesAlgıla(kelime=None):
    bölüm=str
    bilgi = str
    secondtüm = int
    exbilgi = str
    try:
        mic = br.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[5]/c-wiz/span[2]/div/div[1]/span/button""")#microfonun xpathini tanımlıyoruz
        mic.click()#microfon tuşuna basıp dinlemeyi başlatıyoruz
    except:
        havali("bir hata oluşdu hata kodu 0003")
        br.close()
        exit()
    time.sleep(1)#hemen aktif olmadığından 1 saniye bekliyoruz
    if kelime == "uyku":
        havali("uyku modu aktif")
    else:
        havali("ses dinleniyor")#mikrofonun aktif oldugunu kullanıcıya belirtiyoruz
    time.sleep(1)
    secondilk1 = int(time.strftime("%S"))
    secondtüm1 = int
    if kelime != "uyku":
        while True:
            try:
                bilgi  = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span""").text
            except:
                secondson1 = int(time.strftime("%S"))
                if secondilk1 <= secondson1:
                    secondtüm1 = secondson1-secondilk1
                else:
                    secondtüm1 = 60+secondson1-secondilk1
                if secondtüm1 >10:
                    break
                else:
                    continue
            if exbilgi != bilgi:
                exbilgi = bilgi
                bilgi1 = lower(bilgi)
                newbilgi = bilgi1.strip(" ")
                if len(newbilgi) >=5 and " ara" in newbilgi:
                    bölüm = "ara"
                    break
                if len(newbilgi) >=4 and " aç" in newbilgi:
                    bölüm = "aç"
                    break
                secondilk = int(time.strftime("%S"))
            else:
                secondson = int(time.strftime("%S"))
                if secondilk <= secondson:
                    secondtüm = secondson-secondilk
                else:
                    secondtüm = 60+secondson-secondilk
                if secondtüm >1:
                    break                
        if kelime == "uyku":
            havali("uyku modundan çıkıldı")
        else:
            havali("ses dinlemesi bitti")
        try:
            mic.click()
        except:
            havali("bir hata oluşdu hata kodu 0004")
            br.close()
            exit()
        try:
            bilgison = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span""").text
        except:
            bilgison = ""
        if bölüm =="ara":
            bilgison = lower(bilgison)
            kelime_list.append(bilgison)
            bilgisons = "siz: "+bilgison
            havali(bilgisons)
            bilgison=bilgison[:len(bilgison)-4]
            gog_src(bilgison)
            return "%20"
        elif bölüm == "aç":
            bilgison = lower(bilgison)
            kelime_list.append(bilgison)
            bilgisons = "siz: "+bilgison
            havali(bilgisons)
            bilgison=bilgison[:len(bilgison)-3]
            return bilgison
        else:
            bilgison = lower(bilgison)
            kelime_list.append(bilgison)
            bilgisons = "siz: "+bilgison
            havali(bilgisons)
            return bilgison
    elif kelime == "uyku":
        while True:
            try:
                bilgi  = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span""").text
            except:
                continue
            if exbilgi != bilgi:
                exbilgi = bilgi
                bilgi1 = lower(exbilgi)
                if "dinle beni" in bilgi1:
                    bilgison = "dinle beni"
                    break
    havali("ses dinlemesi bitti")
    try:
        mic.click()
    except:
        havali("bir hata oluşdu hata kodu 0005")

    if bilgison != "dinle beni":
        try:
            bilgison = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span""").text
        except:
            bilgison = ""
    bilgison = lower(bilgison)
    kelime_list.append(bilgison)
    bilgisons = "siz: "+bilgison
    havali(bilgisons)
    return bilgison

def algılama(bilgi):  
    komutlar = {
        "merhaba":sy_slm,
        "selam":sy_slm,
        "merhabalar":sy_slm,
        
        "nasılsın":sy_iyi,
        "nasıl gidiyor":sy_iyi,
        "naber":sy_iyi,
        "keyifler nasıl":sy_iyi,

        "teşekkürler":sy_re,
        "teşekürler":sy_re,
        "teşekür ederim":sy_re,
        "teşekkür ederim":sy_re,
        "çok sağol":sy_re,
        "sağol":sy_re,
        "harikasın":sy_re,
        
        "kimsin":sy_kod,
        "sen kimsin":sy_kod,
        "seni kim kodladı":sy_kod,
        "seni kim yazdı":sy_kod,
        
        "saat kaç":sy_saat,
        "şuan saat kaç":sy_saat,
        
        "ayın kaçıncı günündeyiz":sy_gün,
        "ayın kaçındayız":sy_gün,
        "bu gün ayın kaçı":sy_gün,
        
        "kaçıncı aydayız":sy_ayk,
        
        "hangi aydayız":sy_ayh,
        
        "hangi yıldayız":sy_ylj,
        "şuan hangi yıldayız":sy_ylj,

        "bana tam tarihi söyle":sy_yıl,

        "bugün hangi gün":sy_hf,
        "bugün günlerden ne":sy_hf,

        "bir şey aramak istiyorum":gog_src,
        "arama":gog_src,
        "araştır":gog_src,
        "arama yap":gog_src,

        "sistemi kapat":sys_exit,
        "kendini öldür":sys_exit,
        "kendini kapat":sys_exit,

        "uyu artık":uyku_on,
        "uyuma vakti":uyku_on,
        "uyku moduna geç":uyku_on,
        "uyku modunu aç":uyku_on,

        "dinle beni":uyku_off,

        "instagram":op_ig,
        "instagramı":op_ig,
        "insta":op_ig,
        "instayı":op_ig,
        "ınstagram":op_ig,
        "ınstagramı":op_ig,
        "ınsta":op_ig,
        "ınstayı":op_ig,

        "youtube":op_yt,
        "yutup":op_yt,
        "yutubu":op_yt,

        "twitır":op_twt,
        "twitter":op_twt,
        "tivitır":op_twt,

        "trendyol":op_trd,
        "trentyol":op_trd,
        "tirendyol":op_trd,
        "tirentyol":op_trd,


        "%20":sy_idn,
                
        #"sesi kıs":ses_kıs,
        #"sesi azalt":ses_kıs,
        #"ses seviyesini azalt":ses_kıs,

        #"sesi yükselt":ses_yükselt,
        #"sesi artır":ses_yükselt,
        #"ses seviyesini artır":ses_yükselt,

        #"sesi kapat":ses_kapat,
        
        #"sesi aç":ses_aç,

        "":sy_anla
        
    }
    func = komutlar.get(bilgi, lambda: konuş("üzgünüm komut listemde buna karşı cevap yok"))
    func()
def sy_slm():
    slm = ["merhaba","merhabalar","selam","selamlar"]
    konuş(random.choice(slm))
def sy_iyi():
    iyi = ["iyiyim","iyidir","iyi","fena değil","şuanlık iyi","çok iyiyim","sesini duydum daha iyi oldum"]
    konuş(random.choice(iyi))
def sy_kod():
    konuş("Beni Arif Hakan Çankı diye biri kodlayarak geliştirdi.Ama cevap veremeyeceğim sorular var")
def sy_re():
    re = ["önemli değil","rica ederim","sağol","benim işim bu","yardım edebildiysem ne mutlu bana"]
    konuş(random.choice(re))
def sy_anla():
    konuş("dediğini anlamadım tekrar deneyin")
def sy_saat():
    saat = "saat: "+str(time.strftime("%H"))+":"+str(time.strftime("%M"))
    konuş(saat)
def sy_gün(bilgi=None):
    gün = str(time.strftime("%d"))
    günson = "ayın "+gün+"."+" günü"
    if bilgi == "tam":
        return gün
    else:
        konuş(günson)
def sy_hf(bilgi=None):
    günin = str(time.strftime("%A"))
    günler = {
        "Monday": "pazartesi",
        "Tuesday": "salı",
        "Wednesday": "çarşamba",
        "Thursday": "perşembe",
        "Friday": "cuma",
        "Saturday": "cumartesi",
        "Sunday": "pazar"
    }
    güntr = günler.get(günin)
    if bilgi == "tam":
        return güntr
    else:
        günk = "bu gün günlerden "+güntr
        konuş(günk)
def sy_ayk():
    ay1 = " "+str(time.strftime("%m"))
    if " 0" in ay1:
        ay = ay1[1:]
    ayk = "yılın "+ay+"."+" ayı"
    konuş(ayk)
def sy_ayh(bilgi=None):
    ay = str(time.strftime("%m"))
    aylar={
        "01":"ocak",
        "02":"şubat",
        "03":"mart",
        "04":"nisan",
        "05":"mayıs",
        "06":"haziran",
        "07":"temmuz",
        "08":"ağustos",
        "09":"eylül",
        "10":"ekim",
        "11":"kasım",
        "12":"aralık"
    }
    ayh = aylar.get(ay)
    if bilgi == "tam":
        return ayh
    else:
        ayhk = ayh+" ayındayız"
        konuş(ayhk)
def sy_ylj(bilgi=None):
    yıl = str(time.strftime("%Y"))
    yılk = yıl+" yılındayız"
    if bilgi == "tam":
        return yıl
    else:
        konuş(yılk)
def sy_yıl():
    yıl = str(sy_ylj("tam"))
    ay = str(sy_ayh("tam"))
    gün = str(sy_gün("tam"))
    hafta = str(sy_hf("tam"))
    tarih1 = (hafta+" "+gün+" "+ay+" "+yıl)
    konuş(tarih1)
def sy_idn():
    print("")
def gog_src(aramak=None):
    if aramak == None: 
        konuş("aramak istediğiniz şeyi söyleyin")
        ara = sesAlgıla("ara")
        ara = ara[:len(ara)-3].strip()     
    else:
        ara = aramak    
    konuş(ara+" aranıyor")
    Url = "https://www.google.com/search?client=opera&q="+ara
    webbrowser.open_new_tab(Url)
    uyku_on("ara")
def op_ig():
    konuş("instagram açılıyor")
    webbrowser.open_new_tab("https://www.instagram.com")
    uyku_on("aç")
def op_yt():
    konuş("youtube açılıyor")
    webbrowser.open_new_tab("https://www.youtube.com")
    uyku_on("aç")
def op_twt():
    konuş("twitter açılıyor")
    webbrowser.open_new_tab("https://www.twitter.com")
    uyku_on("aç")
def op_trd():
    konuş("trendyol açılıyor")
    webbrowser.open_new_tab("https://www.trendyol.com")
    uyku_on("aç")
def uyku_on(koşul=None):
    if koşul == None:
        konuş("uyku modu aktif")
    bilgi = sesAlgıla("uyku")
    algılama(bilgi)
def uyku_off():
    konuş("dinliyorum")
def sys_exit():
    konuş("sistem kapanıyor son 5 saniye")
    time.sleep(5)
    br.close()
    dosya2= open("kelimeler.txt","w")
    dosya2.writelines(kelime_list)
    
    exit()
while True:
    ara = sesAlgıla()
    algılama(ara)
