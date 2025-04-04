# Ansible-nettverksautomatisering: OSPF, HSRP, DHCP og EtherChannel
---

##  Innhold

- Konfigurasjon av to rutere (RR1 og RR2)
- Dynamisk ruting med OSPF (Area 0)
- HSRP for gateway-redundans (RR1 som aktiv) det er lagt til for to nettverk som er da sør og nor for ruterene 
- DHCP-server på RR1 med backup i RR2
- VLAN-konfigurasjon på switcher
- EtherChannel-trunk mellom SR3 og SG3
- Bruk av Ansible for helautomatisert oppsett

---

## 🗂️ Mappestruktur

```
.
├── rr1.yml                # Playbook for RR1
├── rr2.yml                # Playbook for RR2
├── switch_playbook.yml   # Playbook for SR3 og SG3 EtherChannel
├── ruter_vars.yml        # Variabler for rutere
├── switch_vars.yml       # Variabler for switcher (bare brukt for EtherChannel)
├── hosts.yml             # Ansible inventory 
├── site.yml              # Kjøres for å kjøre hele oppsettet (veldig buggy run at your own risk)
```

---

## Forutsetninger

- Enheter har konfiguert IP,porter,SSH og Vlan (noe du kan enkelt gjøre med pythonskriptet fra oppgave 1)
- Tilkobling til SSH minst 1 gang på forhånd, fordi viss du ikke har gjort det minst 1 gang pr enhet så får du en error
- WSL (Ubuntu) og Ansible er installert på lokal maskin. kan prøve andre distroer men ubuntu var det som fungerte for meg
- Brukernavn og passord på alle enheter er `cisco` siden det er det er lab reglene. (du kan endre dette i hosts.yml)
- For meg fungerte ikke ansible-pylibssh så det gikk altid over til paramiko, denne prosessen er automatisk så om du får en feilmelding om dette kan du ignorere.

---

## Bruk

**først så må du gå til mappen der du har lagra ansible filene** 
I mitt tilfelle var det cd /mnt/c/users/"username"/desktop/ak4ansible$

**Kjør ruter konfigurasjon (RR1.yml):**
dette vil sette opp RR1, RR2 filen er hardcoded fordi det skal være fleksibelt nok for folk å bare å bruke RR1 og vars for rutere. jeg hadde bare ett test oppsett så å bare skirve det rett inn var enklere for meg. 

```bash
ansible-playbook -i hosts.yml rr1.yml
```
på bilde under ser du hvordan vars filen min såg ut for rutere. du kan endre på det som passer ditt ønsket oppsett
![image](https://github.com/user-attachments/assets/1cf4d97b-edca-41a3-a5ce-988baaa734d6)

**Kjør switch-konfigurasjon (EtherChannel mellom SR3 og SG3):**

```bash
ansible-playbook -i hosts.yml switch_playbook.yml 
```

---

## 🌐 Nettverksoppsett (eksempel for det jeg brukte for å teste, dette er kort oppsumering for fult oppsett sjekk nettverkskartet som du kan åpne i nettsiden draw.io)

- **RR1:** `192.168.0.1` og `192.168.1.2`
- **RR2:** `192.168.0.2` og `192.168.1.3`
- **HSRP VIP:** `192.168.1.1` (RR1 aktiv, RR2 standby)
- **HSRP2 VIP:** '192.168.0.4' (RR1 er aktiv, RR2 er Standby)
- **DHCP pools:**
  - VLAN 10: `192.168.0.60-100`
  - VLAN 5: `192.168.1.60-100`
- **SR1 og SR2:** VLAN-konfig med trunk/access porter
- **SR3 og SG3:** EtherChannel trunk via `Gig1/0/1` og `Gig1/0/2`

---
Dissclosure: det kommer errorer når du kjører switchskriptet fordi den prøver å gjøre endringer på SR1 og SR2 men jeg har ikke noen endringer å kjøre så du får noen skummle errorer men bare å ignorere.

Tips: noen av ruterene på labben bruker en gammel versjon av SSH. her er SSH kommandoer jeg måtte bruke:
**SR2**
ssh -o KexAlgorithms=diffie-hellman-group14-sha1 -o HostKeyAlgorithms=ssh-rsa -o Ciphers=aes128-cbc -o MACs=hmac-sha1 cisco@192.168.1.10

**SR3**
ssh -o KexAlgorithms=diffie-hellman-group14-sha1 -o HostKeyAlgorithms=ssh-rsa -o Ciphers=aes128-ctr -o MACs=hmac-sha1 cisco@192.168.1.11

**SG3**
ssh -o KexAlgorithms=diffie-hellman-group14-sha1 -o HostKeyAlgorithms=ssh-rsa -o Ciphers=aes128-ctr -o MACs=hmac-sha1 cisco@192.168.1.12



