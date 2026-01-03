# Network Security Tools - UniMI Project

Progetto didattico per il corso di Sicurezza delle Reti - Università degli Studi di Milano.

## Descrizione

Questa repository contiene due strumenti Python per l'analisi e il testing della sicurezza di rete:

1. **ARP Spoofing Tool** (`ARP_spoof.py`) - Strumento per eseguire attacchi Man-in-the-Middle mediante ARP spoofing
2. **Packet Sniffer** (`packet_sniffer.py`) - Sniffer di pacchetti HTTP per intercettare richieste e credenziali

## ⚠️ Disclaimer Legale

**ATTENZIONE**: Questi strumenti sono stati sviluppati esclusivamente per scopi educativi e di ricerca nell'ambito del corso di Sicurezza delle Reti.

- L'utilizzo di questi strumenti su reti o sistemi senza autorizzazione esplicita è **ILLEGALE**
- Utilizzare solo in ambienti di test controllati o su reti di cui si ha piena autorizzazione
- Gli autori non si assumono alcuna responsabilità per usi impropri o illegali di questi strumenti
- Rispettare sempre le leggi locali e nazionali sulla sicurezza informatica

## Requisiti

- Python 3.x
- Scapy
- scapy-http
- Privilegi di root/amministratore (necessari per la manipolazione dei pacchetti)

## Installazione

1. Clonare la repository:
```bash
git clone <url-repository>
cd "Progetto Sicurezza delle Reti UniMI"
```

2. Installare le dipendenze:
```bash
pip install -r requirements.txt
```

## Utilizzo

### ARP Spoofing Tool

Lo strumento esegue un attacco ARP spoofing posizionandosi come Man-in-the-Middle tra un target e il gateway.

```bash
sudo python3 ARP_spoof.py -t <IP_TARGET> -g <IP_GATEWAY>
```

**Parametri:**
- `-t, --target`: Indirizzo IP del dispositivo target
- `-g, --gateway`: Indirizzo IP del gateway/router

**Esempio:**
```bash
sudo python3 ARP_spoof.py -t 192.168.1.100 -g 192.168.1.1
```

**Funzionalità:**
- Abilita automaticamente l'IP forwarding
- Invia pacchetti ARP spoofed ogni 2 secondi
- Ripristina le ARP table originali alla terminazione (CTRL+C)

**Sito di test suggerito:** http://testphp.vulnweb.com/login.php

### Packet Sniffer

Intercetta e analizza pacchetti HTTP per rilevare richieste e potenziali credenziali.

```bash
sudo python3 packet_sniffer.py -i <INTERFACCIA>
```

**Parametri:**
- `-i, --interfaccia`: Interfaccia di rete da monitorare (es. eth0, wlan0)

**Esempio:**
```bash
sudo python3 packet_sniffer.py -i eth0
```

**Funzionalità:**
- Cattura richieste HTTP (Host + Path)
- Rileva potenziali credenziali cercando keyword: username, user, login, password, pass
- Visualizza in tempo reale i dati intercettati

## Ambiente di Test Consigliato

Per testare questi strumenti in modo sicuro e legale:

1. Creare una rete isolata virtuale (es. con VirtualBox/VMware)
2. Utilizzare macchine virtuali come target
3. Utilizzare siti di test vulnerabili come:
   - http://testphp.vulnweb.com/
   - DVWA (Damn Vulnerable Web Application)
   - WebGoat

## Documentazione di Riferimento

- [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)
- [scapy-http GitHub](https://github.com/invernizzi/scapy-http)
- [Python argparse](https://docs.python.org/3/library/argparse.html)
- [Python subprocess](https://docs.python.org/3/library/subprocess.html)

## Note Tecniche

### ARP Spoofing
L'ARP spoofing sfrutta la mancanza di autenticazione nel protocollo ARP, inviando risposte ARP falsificate per associare il MAC address dell'attaccante agli IP di target e gateway.

### HTTP Sniffing
Il packet sniffer funziona solo con traffico HTTP non cifrato. Il traffico HTTPS non può essere intercettato senza ulteriori attacchi (es. SSL stripping).

## Autore

Progetto realizzato per il corso di Sicurezza delle Reti - Università degli Studi di Milano

## Licenza

Questo progetto è distribuito solo per scopi educativi. Consultare il file LICENSE per maggiori dettagli.

## Contributi

Questo è un progetto didattico. Per suggerimenti o correzioni, aprire una issue.
