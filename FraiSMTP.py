import socket,argparse
import colorama
from colorama import Fore, Style

description=""
Texto=''

parser=argparse.ArgumentParser(description='SMTP Anonymouse - By Fraile 2023.', epilog=description)
parser.add_argument("-ip", dest="IpServer", help="Introduzca Ip Servidor SMTP: 192.168.168.80", required=True)
parser.add_argument("-p", dest="Port", help="Introduzca el Puerto: 25.", required=True)
parser.add_argument("-d", dest="Dominio", help="Introduzca nombre de dominio a suplantar: Fraile.com.", required=True)
parser.add_argument("-mf", dest="MailFrom", help="Introduzca el email a suplantar: info@example.com", required=True)
parser.add_argument("-rt", dest="Rcpt", help="Introduzca el email del receptor: info@example.com", required=True)
parser.add_argument("-df", dest="DMailFrom", help="Introduzca el email a sumplantar que aparecera en el contexto del mensaje: Fraile <info@example.com>", required=True)
parser.add_argument("-dt", dest="DMailTo", help="Introduzca el email del receptor que aparecera en el contexto del mensaje: Fraile <info@example.com>", required=True)
parser.add_argument("-ds", dest="DMailSubject", help="Introduzca el asunto que aparecera en el contexto del mensaje: Hacienda somos todos.", required=True)
parser.add_argument("-t", dest="DMailTexto", help="Introduzca el mensaje que aparecera en el contexto del mensaje: xxxxxxx.", required=True)


params=parser.parse_args()
IpServer=params.IpServer
Port=params.Port
Dominio=params.Dominio
MailFrom=params.MailFrom
Rcpt=params.Rcpt
DMailFrom=params.DMailFrom
DMailTo=params.DMailTo
DMailSubject=params.DMailSubject
DMailTexto=params.DMailTexto



colorama.init(autoreset=True)

print ('',end="\n\n")
print ('*****************************************')
print (f"{Fore.GREEN}SMTP Anonymouse - By Fraile 2023{Style.RESET_ALL}")
print ('*****************************************',end="\n\n")

sock=socket


with sock.create_connection((IpServer,Port)) as Smtp:
    
    # Conexion.
    Texto=Smtp.recv(256)
    print (f"{Fore.GREEN}{Texto.decode('utf-8')}{Style.RESET_ALL}",)

    # Saludo al servidor.
    Smtp.sendall(b'EHLO ' + Dominio.encode('utf-8') + b'\r\n')
    Texto=Smtp.recv(256)
    print (f"{Fore.GREEN}{Texto.decode('utf-8')}{Style.RESET_ALL}")

    # Inroducimos email a suplantar.

    Smtp.sendall(b'mail from: ' + MailFrom.encode('utf-8') + b'\r\n')
    Texto=Smtp.recv(256)
    print (f"{Fore.GREEN}{Texto.decode('utf-8')}{Style.RESET_ALL}")

    # Introducimos email objetivo.

    Smtp.sendall(b'rcpt to: ' + Rcpt.encode('utf-8') + b'\r\n')
    Texto=Smtp.recv(256)
    print (f"{Fore.GREEN}{Texto.decode('utf-8')}{Style.RESET_ALL}")

    # Abrimos DATA, para la redaccion del email.
    Smtp.sendall(b'Data\r\n')
    Texto=Smtp.recv(256)
    print (f"{Fore.GREEN}{Texto.decode('utf-8')}{Style.RESET_ALL}")

    Smtp.sendall(b'From:' + DMailFrom.encode('utf-8') + b'\r\n')

    Smtp.sendall(b'To:' + DMailTo.encode('utf-8') + b'\r\n')

    Smtp.sendall(b'Subject:' + DMailSubject.encode('utf-8') + b'\r\n')

    # Mensaje.

    Smtp.sendall(b'' + DMailTexto.encode('utf-8') + b'\r\n')

    Smtp.sendall(b'.\r\n')
    Texto=Smtp.recv(256)
    print (f"{Fore.GREEN}{Texto.decode('utf-8')}{Style.RESET_ALL}")


    Smtp.close





