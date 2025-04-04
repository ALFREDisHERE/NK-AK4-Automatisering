# 📡 Ansible-nettverksautomatisering: OSPF, HSRP, DHCP og EtherChannel

Dette prosjektet automatiserer oppsettet av rutere og switcher i et Cisco-basert nettverk ved hjelp av Ansible. Oppgaven er laget som en del av et skoleprosjekt, og dekker blant annet OSPF, HSRP, DHCP og EtherChannel-konfigurasjon.

---

## 🧠 Innhold

- Konfigurasjon av to rutere (RR1 og RR2)
- Dynamisk ruting med OSPF (Area 0)
- HSRP for gateway-redundans (RR1 som aktiv)
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
├── switch_vars.yml       # Variabler for switcher (EtherChannel)
├── hosts.yml             # Ansible inventory (YAML-basert)
├── site.yml              # Kjøres for å kjøre hele oppsettet
└── README.md             # Dokumentasjonen (denne filen)
```

---

## 🛠️ Forutsetninger

- Enheter har allerede grunnkonfigurasjon (IP, VLAN, SSH).
- Tilkobling til enhetene skjer via SSH.
- WSL (Debian) og Ansible er installert på lokal maskin.
- Brukernavn og passord på alle enheter er `cisco`.

---

## 🚀 Bruk

1. **Kjør hele oppsettet (RR1 og RR2):**

```bash
ansible-playbook site.yml -i hosts.yml
```

2. **Kjør kun en av ruterkonfigurasjonene:**

```bash
ansible-playbook rr1.yml -i hosts.yml
```

3. **Kjør switch-konfigurasjon (EtherChannel mellom SR3 og SG3):**

```bash
ansible-playbook switch_playbook.yml -i hosts.yml
```

---

## 🌐 Nettverksoppsett (kort)

- **RR1:** `192.168.0.1` og `192.168.1.2`
- **RR2:** `192.168.0.2` og `192.168.1.3`
- **HSRP VIP:** `192.168.1.1` (RR1 aktiv, RR2 standby)
- **DHCP pools:**
  - VLAN 10: `192.168.0.60-100`
  - VLAN 5: `192.168.1.60-100`
- **SR1 og SR2:** VLAN-konfig med trunk/access porter
- **SR3 og SG3:** EtherChannel trunk via `Gig1/0/1` og `Gig1/0/2`

---

## 👨‍💻 Forfatter

Prosjekt utført av [Ditt navn her] som en del av skoleprosjekt innen nettverksadministrasjon og automatisering.
