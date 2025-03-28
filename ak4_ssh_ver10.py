import serial
import time

def send_command(ser, command, sleep=1): #sende en command med comporten og venter på svar (+ den printer kommandoen sendt i konsolen for enklere feilsøking)
    ser.write(command.encode() + b'\n')
    print(command)
    time.sleep(sleep)
    output = ser.read(ser.inWaiting()).decode()
    print(output)

def get_input(prompt): #får bruker input
    value = input(prompt + " (eller skriv 'skip' for å hoppe over): ").strip() #la til dette for å kunne hoppe over input felt som ikke er relevant
    return None if value.lower() == "skip" else value

def configure_ssh(ser, hostname, username, password): #setter opp SSH
    send_command(ser, "enable")
    send_command(ser, "configure terminal")
    send_command(ser, f"hostname {hostname}")
    send_command(ser, "ip domain-name AK4.local")
    time.sleep(4)
    send_command(ser, "crypto key generate rsa")
    send_command(ser, "1024")
    send_command(ser, "ip ssh version 2")
    if username and password:
        send_command(ser, f"username {username} privilege 15 secret {password}")
    send_command(ser, "line vty 0 4")
    send_command(ser, "transport input ssh")
    send_command(ser, "login local")
    send_command(ser, "exit")
    send_command(ser, "exit")
    send_command(ser, "exit")
    print("SSH-konfigurasjon fullført!")

def configure_port(ser): #her kan man konfiguere port
    port = get_input("Skriv inn portnavn du vil konfigurere (f.eks. gigX/X.XX)") #skriv inn interface her
    if not port:
        print("Ingen port valgt. Hopper over konfigurasjon.")
        return
    
    port_type = get_input("Vil du konfigurere denne porten som ruterport eller switchport? (ruter/switch)")
    send_command(ser, "enable")
    send_command(ser, "configure terminal")
    send_command(ser, f"int {port}") #veit at på ruterdenlen så gå in inn og ut av sån 3 interfaces men den her må være her for at switchport skal funke

    if port_type == "ruter": 
        ip = get_input("Skriv inn IP-adresse")
        mask = get_input("Skriv inn subnet-maske")
        vlan_id = get_input("Skriv VLAN-ID")
        none_subint = get_input("navnet på porten som skal skrues på (ikke ha med subint)") #den her må være her slik at det kan kjøres no shutdown på porten hvis det er valgt subinterface
        if ip and mask and vlan_id: 
            send_command(ser, "exit")
            send_command(ser, "exit")
            send_command(ser, "vlan database") #legger til vlan i database
            send_command(ser, f"vlan {vlan_id}")
            send_command(ser, "exit")
            send_command(ser, "conf t")
            send_command(ser, f"int {none_subint}")
            send_command(ser, "no shutdown")
            send_command(ser, "exit")
            send_command(ser, f"int {port}")
            send_command(ser, f"encapsulation dot1Q {vlan_id}")
            send_command(ser, f"ip address {ip} {mask}")
            send_command(ser, "no shutdown")
            print(f"Port {port} konfigurert som ruterport med IP {ip}/{mask}")
            send_command(ser, "exit")
            send_command(ser, "exit")
    elif port_type == "switch":
        vlan_id = get_input("Skriv inn VLAN ID for som skal være allowed (hopp over for vanlig trunk)")
        send_command(ser, "switchport mode trunk")
        if vlan_id: 
            send_command(ser, f"switchport trunk allowed vlan {vlan_id}")
        print(f"Port {port} satt i trunk mode.")
    
    send_command(ser, "exit")
    print("Portkonfigurasjon fullført!")

def configure_vlan(ser): #her kan du legge til vlan :D
    vlan_id = get_input("Skriv inn VLAN-ID du vil konfigurere")
    if not vlan_id:
        print("Ingen VLAN-ID valgt. Hopper over konfigurasjon.")
        return
    
    ip_address = get_input("Skriv inn IP-adresse for VLAN")
    subnet_mask = get_input("Skriv inn subnet-mask")
    default_gateway = get_input("Skriv inn default gateway")
    
    send_command(ser, "enable")
    send_command(ser, "configure terminal")
    send_command(ser, f"vlan {vlan_id}")
    send_command(ser, f"name VLAN_{vlan_id}")
    send_command(ser, "exit")
    send_command(ser, f"interface vlan {vlan_id}") 
    send_command(ser, f"ip address {ip_address} {subnet_mask}") #her får vlanet ip
    send_command(ser, "no shutdown") # denne er viktig eller så blir ikke vlan aktivert
    send_command(ser, "exit")
    
    if default_gateway: #insane måte å sette opp default gateway
        send_command(ser, f"ip default-gateway {default_gateway}")
        print(f"Default gateway satt til {default_gateway}")
    print(f"VLAN {vlan_id} konfigurert med IP {ip_address}/{subnet_mask}.")

def main(): #her er main :D
    com_port = input("Skriv inn COM-port du ønsker å bruke (f.eks. COM6): ").strip() #her blir bruker spurt om hvliken com port som skal brukes
    ser = serial.Serial(com_port, baudrate=9600, timeout=1) # åpner com komblingen
    time.sleep(2)
    
    setup_ssh = input("Vil du sette opp SSH? (ja/nei): ").strip().lower()
    if setup_ssh == "ja":
        hostname = get_input("Skriv inn ønsket hostname")
        username = get_input("Skriv inn brukernavn")
        password = get_input("Skriv inn passord")
        configure_ssh(ser, hostname, username, password)
    
    while True:
        config_choice = input("Vil du konfigurere en port eller VLAN? (port/vlan/skip): ").strip().lower()
        if config_choice == "port":
            configure_port(ser)
        elif config_choice == "vlan":
            configure_vlan(ser)
        elif config_choice == "skip":
            break
    
    ser.close() #her slutter den kontakten over com koblingen
    print("Konfigurasjon fullført!") #yay

if __name__ == "__main__":
    main()
