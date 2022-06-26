# Made With ❤️ Kucing0yen
# Powered By ExecutedTeam

import os,sys,time,requests,json,random
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
bg="\033[1;0m\033[1;41mText\033[1;0m"

def printtik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)

# Logo By Kucing0yen
def banner():
    print(f"""
{ungu}╔╦╗{W}┌─┐┌─┐┌─┐  {biru}╔═╗{W}┌┬┐┌─┐
{ungu}║║║{W}├─┤└─┐└─┐  {biru}╚═╗{W}│││└─┐
{ungu}╩ ╩{W}┴ ┴└─┘└─┘  {biru}╚═╝{W}┴ ┴└─┘""")

# Tambah Api Web Sama Massive Sendiri
def banner2():
    banner()
    print (f"""
{W}┬───{R}⟨{W}Menu{R}⟩{W}────────────────
{W}├─{ungu}⟩ {W}1{R}.{W}Spam Sms {W}({Y}Massive{W})
{W}├─{ungu}⟩ {W}2{R}.{W}Setting Target {R}({W}Atur Target{R})
{W}├─{ungu}⟩ {W}3{R}.{W}Remove Target {R}({W}Hapus Target{R})
{W}├─{ungu}⟩ {W}4{R}.{W}Join Komunitas {R}({G}WhatsApp{R})
{W}├─{ungu}⟩ {R}0{R}.{W}Exit {R}({W}Keluar{R})
{W}└─────────────────────────
""")
    mr_input=input(f"{W}Pilih {B}»{R}⟩ ")
    if mr_input=="1":
        start()
        tanya()
    if mr_input=="2":
        settings()
    if mr_input=="3":
        printik(f"{W}[{Y}•••{W}] Removed Target{abu}...")
        os.system("rm list1.txt list2.txt target.txt")
        time.sleep(5)
        printik(f"{W}[{G}✓{W}] Success Removed Target")
        tanya()
    if mr_input=="4":
        os.system("xdg-open https://chat.whatsapp.com/GRZoMoLPNJA22TR7WINpMY")
        tanya()
    if mr_input=="0":
        time.sleep(5)
        sys.exit(f"{W}[{R}!{W}] Exited With Program{abu}.....")

banner2()
