#gerekli kütüphaneleri ekledik
from selenium import webdriver#pip install selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import webbrowser#pip install webbrowser
import time
import random
import sys
#bu kodlar tarayıcıyı normal bir şekilde açıyor arka planda çalıştırmayı daha başaramadım.
#kodlar çalışırken tarayıcı ve uygulama küçük olmasın kasıyor ve hata verebiliyor.
#çalışırken ikiside ön planda olsun üstüne program ya da uygulama açmayın hata verebiliyor.
driver_path = "C:/Users/hakan/OneDrive/Masaüstü/kodlar/yapayzeka1.3/driver/chromedriver.exe"#selenium kullanmak için gerekli olan driver'ın konumunu belirtiyoruz
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/hakan/AppData/Local/Google/Chrome/User Data/Default")#açılacak sayfanın kullanıcı bilgileri ile açılmasını saglıyoruz amacı ise mikrofona erişmek için her seferinde izin istemesin
buyukAlfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
br = webdriver.Chrome(driver_path, options=options)#tarayıcıyı açıyoruz
br.set_window_size(800, 500)#tarayıcının boyutunu belirtiyoruz
br.get("https://translate.google.com/?sl=auto&tl=tr&op=translate")#tarayıcının google translate gitmesini saglıyoruz. Proje translate ile dinleme saglayacak
time.sleep(6)#sayfanın yüklenmesi için zaman tanıyoruz
if br.title == "Google Çeviri":#sayfanın başlığının google çeviri olup olmadıgını kontrol ediyoruz
    try:
        br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/div/div[2]/div/div/span/button[1]""").click()#dil algıla bölümüne tıklıyoruz
        dil = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[3]/c-wiz/div[1]/div/div[2]/input""").send_keys("türkçe",Keys.ENTER)#tıkladıkdan sonra oraya türkçe yazıp enter yaparak dili seçiyoruz
        time.sleep(1)#yüklenmesini bekliyoruz
        print("Sistem hazır")#ekrana sistem hazır mesajı yolluyoruz
    except:
        print("bir hata oluşdu kod 0001")#eger dil algıla bölümü hata verirse sistem kapanacak
        br.close()#tarayıcıyı kapatıyor
        exit()#uygulamayı sonlandırıyor
else: 
    print("bir hata oluşdu")#başlık google çeviri olmazsa hata verip kapanıyor
    br.close()#tarayıcıyı kapatıyor
    print("Sistem kapanıyor")#ekrana bilgi mesajı yolluyor
    time.sleep(2)
    exit()#uygulamayı kapatıyor
    
def lower(kelimeilk:str):#kendi harf küçültme fonksyonumuzu tanımliyoruz
    yenikelime = str()
    kelime = kelimeilk.replace(".","")#noktaları siliyoruz
    kelime = kelime.replace("?","")#soru işaretini siliyoruz
    kelime = kelime.replace(",","")#virgülleri siliyoruz
    kelime = kelime.strip()#başındaki ve sonundaki boşlukları siliyoruz
    for i in kelime:
        if i in kelime:
            if i in buyukAlfabe:
                index = buyukAlfabe.index(i)
                yenikelime += kucukAlfabe[index]
            else:
                yenikelime += i
    return yenikelime#dönüşmüş halini geri döndürüyoruz

def havali(parametre, time_sleep = 0.04):#sistem ekrana yazı yazarken güzel yazması için bir fonksiyon 
    soz=[]
    for i in parametre+"\n":
        soz.append(i)
        time.sleep(time_sleep)
        sys.stdout.write(str(soz[0]))
        sys.stdout.flush()
        soz.remove(i) 
        
def konuş(bilgi):#sistemin konuşmasını saglayan fonksiyonu yazıyoruz
    bekle = len(bilgi)/10+0.6#kelimenin/cümlenin uzunluğuna göre bir zaman belirliyoruz
    havali("Algılanıyor...")
    try:
        br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[2]/div/div/span/button""").click()#çevirideki yazı yazınca oluşan sol üsteki çarpı tuşuna basıyor
    except:
        havali("Algılanamadı")#tuş bulunamazsa bilgi veriyor
    try:
        yaz = br.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea""")#çevirideki yazı yerini algılıyor
        yaz.send_keys(bilgi)#oraya bizim döndürdüğümüz cevabı yazıyor
        yaz.send_keys(Keys.ENTER)#çıkan önermelerden kurtulmak için enter'a basıyor
        br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[5]/div[1]/div/div[2]/div/span/button""").click()#seslendirme butonuna tıklıyor
    except:
        havali("hata kodu 0002")#hata oluşursa sistemi kapatıyor
        br.close()
        exit()
    bilgison = str
    bilgison = "Asistan:" + bilgi#ekrana yazılacak yazıyı ayarlıyoruz ve cevabı ona ekliyoruz
    havali(bilgison)#ekrana yazdırıyoruz
    time.sleep(bekle)#ilk başda tanımladığımız kadar bekliyoruz
    
def sesAlgıla(kelime=None):#ses algılama fonksiyonunu yazıyoruz
    bölüm=str
    bilgi = str
    secondtüm = int
    exbilgi = str
    try:
        mic = br.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[5]/c-wiz/span[2]/div/div[1]/span/button""")#microfonun xpathini tanımlıyoruz
        mic.click()#microfon tuşuna basıp dinlemeyi başlatıyoruz
    except:
        havali("bir hata oluşdu hata kodu 0003")#hata oldugunda sistemi kapatıyoruz
        br.close()
        exit()
    time.sleep(1)#mikrofon hemen aktif olmadığından 1 saniye bekliyoruz
    if kelime == "uyku":#eger sesalgıla fonksiyonuna uyku kelimesi ile çagrıldıysa uyku modu aktif mesajını yazıyoruz
        havali("uyku modu açıldı")
    else:
        havali("ses dinleniyor")#mikrofonun aktif oldugunu kullanıcıya belirtiyoruz
    time.sleep(1)
    secondilk1 = int(time.strftime("%S"))#mikrofon ilk açıldıgında saniyeyi kaydediyoruz
    secondtüm1 = int
    if kelime != "uyku":#eger kelime uyku değilse normal dinlemeye geçiyoruz
        while True:
            try:
                bilgi  = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span""").text#çeviri bölümün sag tarafındaki çıkdı bölümüne erişiyoruz
            except:
                secondson1 = int(time.strftime("%S"))#erişmezse bir çıkdı olmadığı belli oluyor bu yüzden saniyeyi çekiyoruz
                if secondilk1 <= secondson1:#eger secondilk1 secondson1 den küçük ya da eşit ise çıkartıyoruz ve secondtüm1'e eşitliyoruz
                    secondtüm1 = secondson1-secondilk1
                else:#eger tam tersi ise yani secondilk1 secondson1 den büyük ise 60 ekleyip çıkartıyoruz bu işlem şuna yarıyor eger ilk saniye 59 son saniye 4 ise burada çıkarırken hata veririr bu yüzden 4+60 - 59 diyerek dogru zamanı buluyoruz
                    secondtüm1 = 60+secondson1-secondilk1
                if secondtüm1 >10:#eğer 10 saniyedir her hangi bir bilgi oluşmadıysa döngü sonlanarak dinlemeyi bitirecek
                    break
                else:#10 saniye değil ise başa dönerek tekrardan deniyecek burada her hangi bilgi oluşmadığından başa sarıyor yoksa program hata verir
                    continue
            if exbilgi != bilgi:#bilginin değişip değişmediğini sorguluyor
                exbilgi = bilgi#değişdi ise kaydediyoruz
                bilgi1 = lower(bilgi)#küçük harfe dönüştürüyoruz
                newbilgi = bilgi1+" "
                print(newbilgi+"12")
                if len(newbilgi) >=5 and " ara " in newbilgi:#listin içinde ' ara' kelimesi var mı diye bakıyoruz
                    bölüm = "ara"#bölümü ara diye değiştiriyoruz
                    break#döngüden çıkıyoruz
                if len(newbilgi) >=4 and " aç " in newbilgi:#üsteki gibi ' aç'var mı diye bakıyoruz
                    bölüm = "aç"#bölümü a. diye değiştiriyoruz
                    break#döngüden çıkıyoruz
                secondilk = int(time.strftime("%S"))#secondilk güncelliyoruz
            else:#eger bilgide bir değişiklik olmazsa 
                secondson = int(time.strftime("%S"))#secondson'u çekiyoruz
                if secondilk <= secondson:#yukarıdaki işlemler
                    secondtüm = secondson-secondilk
                else:
                    secondtüm = 60+secondson-secondilk
                if secondtüm >1:#1 saniyeden fazla süredir yeni bilgi gelmediyse döngüden çıkıyor ama. bir şey söyledikden sonra susma süresi 1 saniyeden fazla ise dinlemeyi kapatıyor
                    break                
        if kelime == "uyku":#kelime uyku ise 
            havali("uyku modundan çıkıldı")#uyku modundan çıkıldı yazıyor
        else:#değil işe
            havali("ses dinlemesi bitti")#ses dinlemesi bitti diyor
        try:
            mic.click()#mokrofon tuşuna basıyor
        except:
            havali("bir hata oluşdu hata kodu 0004")#mikrofon tuşunu bulamazsa hata verip sistemi kapatıyor
            br.close()
            exit()
        try:
            bilgison = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span""").text#en son olarak çevirinin sağ tarafından yazıyı alıyor 
        except:
            bilgison = ""#alamaz ise iki ihtimal var biri hiç bir şey söylemediysek orası bulunamıyor ikincisi ise internet kötü ise çeviriyor diyor ve bulunamıyor iki ihtimalde de bilgisonu boş bırakıyoruz 
        if bölüm =="ara":#eger bölüm ara ise yani üstte belirmişdik(120. satır)
            bilgison = lower(bilgison)#küçük harfe dönüşüyor
            bilgisons = "siz: "+bilgison#ekrana yazılması için bir yazı ayarlanıyor
            havali(bilgisons)#yazı ekrana yazılıyor
            bilgison=bilgison[:len(bilgison)-4]#bilginin son 4 hanesi silinip kaydediliyor
            gog_src(bilgison)#arama bölümüne bilgi gönderiliyor
            return "%20"#çıkdı ayarlanıyor
        elif bölüm == "aç":#eger bölüm aç ise yani üstte belirtmişdik(123. satır)
            bilgison = lower(bilgison)#küçük harfe dönüşüyor
            bilgisons = "siz: "+bilgison#ekrana yazılması için bir yazı ayarlanıyor
            havali(bilgisons)#yazı ekrana yazılıyor
            bilgison=bilgison[:len(bilgison)-3]#bilginin son 3 hanesi silinip kaydediliyor
            return bilgison#burada üstekinden farklı olarak bilgiyi direk çıkdı olarak ayarlıyoruz 
        else:#eger bölüm ikiside değil ise
            bilgison = lower(bilgison)#küçük harfe dönüşüyor
            bilgisons = "siz: "+bilgison#ekrana yazılması için bir yazı ayarlanıyor
            havali(bilgisons)#yazı ekrana yazılıyor
            return bilgison#ve son olarak çıkdı ayarlanıyor
    elif kelime == "uyku":#eger kelime uyku ise bunu üst tarafda daha microfonu tanımlamadan önce belirmişdik
        while True:
            try:
                bilgi  = br.find_element_by_xpath("""/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span""").text#üstteki gibi mikrofonun xpathini tanımlıyoruz
            except:#üstteki işlemler oldugundan burada sadece üstte olmayan yerleri belirtecem
                continue
            if exbilgi != bilgi:
                exbilgi = bilgi
                bilgi1 = lower(exbilgi)
                if "dinle beni" in bilgi1:#burada farklı olarak dinle beni var bu eger dinle beni denirse 
                    bilgison = "dinle beni"
                    break
        havali("uyku modu kapandı")
        try:
            mic.click()
        except:
            havali("bir hata oluşdu hata kodu 0005")
        bilgisons = "siz: "+bilgison
        havali(bilgisons)
        return bilgison

def algılama(bilgi):#algılama fonksyonunu ayarlıyoruz
    #komutlar diye sözlük oluşturup komutları bunun içine yazıyor ve karşılarınada hangi fonksiyona gidecekse onu yazıyoruz
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

        "":sy_anla
        
    }
    func = komutlar.get(bilgi, lambda: konuş("üzgünüm komut listemde buna karşı cevap yok"))#söylediğimiz şeyi içine atıp karşılık gelen fonksyonu func atıyoruz eger herhangi bir karşılık yok ise lambda: yazısının karşısına yazıyoruz
    func()#burada ise çıkan fonksyonun sonuna parantez koyarak çagırıyoruz
def sy_slm():#merhaba ve benzeri kelimelere karşı cevaplar
    slm = ["merhaba","merhabalar","selam","selamlar"]
    konuş(random.choice(slm))#yukarıdaki cevaplardan birini rasgele bir şekilde konuş fonksyonuna gönderiyor
    
def sy_iyi():#nasılsın ve benzeri kelimelere karşı cevaplar
    iyi = ["iyiyim","iyidir","iyi","fena değil","şuanlık iyi","çok iyiyim","sesini duydum daha iyi oldum"]
    konuş(random.choice(iyi))#yukarıdaki cevaplardan birini rasgele bir şekilde konuş fonksyonuna gönderiyor
    
def sy_kod():#kimsin ve benzeri kelimelere karşı cevaplar
    konuş("Beni Arif Hakan Çankı diye biri kodlayarak geliştirdi.Ama cevap veremeyeceğim sorular var")#cevabı konuşa gönderiyoruz
    
def sy_re():#teşekkür ve benzeri kelimelere karşı cevaplar
    re = ["önemli değil","rica ederim","sağol","benim işim bu","yardım edebildiysem ne mutlu bana"]
    konuş(random.choice(re))#yukarıdaki cevaplardan birini rasgele bir şekilde konuş fonksyonuna gönderiyor
    
def sy_anla():#eger sesalgıla bölümünde bir cevap alamazsak bu fonksyon çalışır
    konuş("dediğini anlamadım tekrar deneyin")#cevabı konuşa gönderiyoruz
    
def sy_saat():#saati sordugumuzda çalışacak fonksiyon
    saat = "saat: "+str(time.strftime("%H"))+":"+str(time.strftime("%M"))#saati time kütüphanesinden çekiyoruz
    konuş(saat)#cevabı konuşa gönderiyoruz
    
def sy_gün(bilgi=None):#ayın kaçındayız ve benzeri kelimelere karşı cevaplar
    gün = str(time.strftime("%d"))#time kütüphanesinden günü çekiyoruz
    günson = "ayın "+gün+"."+" günü"#cevabı ayarlıyoruz
    if bilgi == "tam":#eger fonksyon tam bilgisi ile çağrılmışsa 
        return gün#gün'ü çıkdı olarak ayarlıyoruz
    else:
        konuş(günson)#cevabı konuşa gönderiyoruz
        
def sy_hf(bilgi=None):#haftanın hangi günündeyiz ve benzeri gibi kelimelere karşı cevaplar
    günin = str(time.strftime("%A"))#haftanın gününü time kütüphanesinden çekiyoruz ama ingilizce olarak çekiliyor
    #günler diye sözlük oluşturup ingilizceyi türkçeye çeviriyoruz
    günler = {
        "Monday": "pazartesi",
        "Tuesday": "salı",
        "Wednesday": "çarşamba",
        "Thursday": "perşembe",
        "Friday": "cuma",
        "Saturday": "cumartesi",
        "Sunday": "pazar"
    }
    güntr = günler.get(günin)#günlerin içine ingilizce olan bilgiyi atıp güntr yani günler türkçe olan değeri alıyoruz
    if bilgi == "tam":#eger fonksyon tam ile çagrıldıysa
        return güntr#güntr'yi çıkdı olarak gönderiyoruz
    else:
        günk = "bu gün günlerden "+güntr#cevabi ayarlıyoruz
        konuş(günk)#cevabı konuşa gönderiyoruz
        
def sy_ayk():#kaçıncı aydayız ve benzeri kelimelere karşı cevaplar
    ay1 = " "+str(time.strftime("%m"))#hangi aydayız onu time kütüphanesinden çekiyoruz
    if " 0" in ay1:#eğer önünde 0 var ise onu siliyoruz (kütüphaneden bilgi 01,02,03 tarzında çekildiği için 0 ı siliyoruz ama 10'da da sıfır oldugundan önüne boşluk koyup ' 0' değeri varsa silme işlemini gerçekleştiriyoruz)
        ay = ay1[1:]
    ayk = "yılın "+ay+"."+" ayı"#cevabı hazırlıyoruz
    konuş(ayk)#cevabı konuşa gönderiyoruz
    
def sy_ayh(bilgi=None):#hangi aydayız ve benzeri kelimelere karşı cevaplar
    ay = str(time.strftime("%m"))#time kütüphanesinden sayı olarak değeri alıyoruz
    #aldığımız değeri ayların isimlerine çevirmek için sözlük oluşturuyoruz
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
    ayh = aylar.get(ay)#sözlüge sayı olan değeri atıp ayın ismini alıyoruz
    if bilgi == "tam":#eger fonksyon tam ile çagrıldıysa
        return ayh#ayın ismini çıkdı olarka gönderiyoruz
    else:
        ayhk = ayh+" ayındayız"#cevabı ayarlıyoruz
        konuş(ayhk)#cevabı konuşa gönderiyoruz
        
def sy_ylj(bilgi=None):#hangi yıldayız ve benzeri kelimelere karşı cevaplar
    yıl = str(time.strftime("%Y"))#time kütüphanesinden yıl değerini alıyoruz
    yılk = yıl+" yılındayız"#cevabı ayarlıyoruz
    if bilgi == "tam":#fonksyon tam ile çagrıldıysa
        return yıl# yılı çıkdı olarak gönderiyoruz
    else:
        konuş(yılk)#cevabı konuşa gönderiyoruz
        
def sy_yıl():#bana tarihi tam olarak söyle ve benzeri kelimelere karşı cevaplar
    yıl = str(sy_ylj("tam"))#yılı yukardaki fonksyondan tam göndererek çekiyoruz
    ay = str(sy_ayh("tam"))#ayı yukardaki fonksyondan tam göndererek çekiyoruz
    gün = str(sy_gün("tam"))#günü yukardaki fonksyondan tam göndererek çekiyoruz
    hafta = str(sy_hf("tam"))#hafta gününü yukardaki fonksyondan tam göndererek çekiyoruz
    tarih1 = (hafta+" "+gün+" "+ay+" "+yıl)#cevabı ayarlıyoruz
    konuş(tarih1)#cevabı konuşa gönderiyoruz
    
def sy_idn():#eger %20 verisi olursa bu çagrılacak. %20 sadece arada çagrılıyor
    print("")
    
def gog_src(aramak=None):#bir şey aramak istiyorum ve benzeri kelimelere karşı cevaplar 
    if aramak == None:#eger fonksyon bir kelime ile çagrılmadıysa
        konuş("aramak istediğiniz şeyi söyleyin")#konuşa cevap gönderiyoruz
        ara = sesAlgıla("ara")#sesalgılayı ara ile çagrıyoruz gelen cevabı ise ara'ya atıyoruz
        ara = ara[:len(ara)-3].strip()#son 3 karakterini silip kaydediyoruz çünkü sonunda ara yazıyor
    else:
        ara = aramak#ara'yı çağrılan kelimeye eşitliyoruz
    konuş(ara+" aranıyor")#cevabı konuşa gönderiyoruz
    Url = "https://www.google.com/search?client=opera&q="+ara#aramayı gerçekleştiriyoruz buradaki URL opera için opera kullanmıyorsanız çalışmaya bilir
    webbrowser.open_new_tab(Url)#URL yi çalıştırıyoruz
    uyku_on("ara")#uyku'yu aktif ederek aramadan sonra dinlemeyi kapatıyoruz ta ki uykudan çıkıncaya kadar 
    
def op_ig():#instagramı aç ve benzeri kelimelere karşı cevaplar
    konuş("instagram açılıyor")#cevabı konuşa gönderiyoruz
    webbrowser.open_new_tab("https://www.instagram.com")#instagramı açıyoruz
    uyku_on("aç")#uyku'yu aktif ederek açdan sonra dinlemeyi kapatıyoruz ta ki uykudan çıkıncaya kadar 
    
def op_yt():#youtube aç ve benzeri kelimelere karşı cevaplar
    konuş("youtube açılıyor")#cevabı konuşa gönderiyoruz
    webbrowser.open_new_tab("https://www.youtube.com")#youtube'u açıyoruz
    uyku_on("aç")#uyku'yu aktif ederek açdan sonra dinlemeyi kapatıyoruz ta ki uykudan çıkıncaya kadar 
    
def op_twt():#twitter'ı aç ve benzeri kelimelere karşı cevaplar
    konuş("twitter açılıyor")#cevabı konuşa gönderiyoruz
    webbrowser.open_new_tab("https://www.twitter.com")#twitter açılıyor
    uyku_on("aç")#uyku'yu aktif ederek açdan sonra dinlemeyi kapatıyoruz ta ki uykudan çıkıncaya kadar 
    
def op_trd():#trendyol'u aç ve benzeri kelimelere karşı cevaplar
    konuş("trendyol açılıyor")#cevabı konuşa gönderiyoruz
    webbrowser.open_new_tab("https://www.trendyol.com")#trendyol açılıyor
    uyku_on("aç")#uyku'yu aktif ederek açdan sonra dinlemeyi kapatıyoruz ta ki uykudan çıkıncaya kadar 
    
def uyku_on(koşul=None):#uyku moduna geç ve benzeri kelimelere karşı cevaplar
    if koşul == None:#fonksyon bir kelime ile çagrılmadıysa
        konuş("uyku modu aktif")#cevabı konuşa gönderiyoruz
    bilgi = sesAlgıla("uyku")#sesalgılayı uyku ile çağrıyoruz ve gelen bilgiyi kaydediyoruz
    algılama(bilgi)#algılama'ya kaydetdiğimiz bilgiyi gönderiyoruz
    
def uyku_off():#dinle beni ve benzeri kelimelere karşı cevaplar genel olarak uyku modunu kapatırken kullanılır
    konuş("dinliyorum")#cevabı konuşa gönderiyoruz
    
def sys_exit():#sistemi kapat ve benzeri kelimelere karşı cevaplar
    konuş("sistem kapanıyor son 5 saniye")#cevabı konuşa gönderiyoruz
    time.sleep(5)#5 saniye bekliyor
    br.close()#tarayıcıyı kapatıyor
    exit()#uygulamayı kapatıyor
    
    
while True:#döngü ile dinleme'yi devamlı halle getiriyoruz
    bilgi = sesAlgıla()#sesalgıla fonksyonunu çagrıyor ve gelen bilgiyi kaydediyor
    algılama(bilgi)#algılamaya kaydedilen bilgiyi gönderiyor
