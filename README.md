# **ArpSpoof**  
**A Python-based ARP Spoofing tool for network security testing**  

![ArpSpoof Banner](https://raw.githubusercontent.com/Zer0Secur8ty/ArpSpoof/main/assets/banner.png) *(Replace with actual image if available)*  

##  About 
ArpSpoof is a simple yet powerful tool for conducting **ARP Spoofing** attacks, allowing penetration testers and cybersecurity professionals to intercept and manipulate network traffic. This tool is intended for **educational and security research purposes only**.  

##  Disclaimer  
This tool is for **ethical hacking and educational purposes only**. Unauthorized use on networks without permission is illegal. The author is not responsible for any misuse of this tool.  

##  Features  
- Spoofs ARP tables to redirect network traffic  
- Intercepts packets between victim and router  
- Works on Linux and Windows  
- Supports Python 3  

##  Installation 
###  Prerequisites 
Ensure you have **Python 3** and the required dependencies installed:  
```bash
pip install scapy
```

###  Clone the repository
```bash
git clone https://github.com/Zer0Secur8ty/ArpSpoof.git
cd ArpSpoof
```

##  Usage  
Run the tool with **root privileges**:  
```bash
python arp_spoof.py -t <Target-IP> -g <Gateway-IP>
```

### Example  
```bash
python arp_spoof.py -t 192.168.1.100 -g 192.168.1.1
```
This will spoof the ARP cache of the target **192.168.1.100**, making it believe that our machine is the gateway (**192.168.1.1**).  

##  Options  
| Flag | Description |
|------|------------|
| `-t, --target` | Target IP address |
| `-g, --gateway` | Gateway (router) IP address |
| `-i, --interface` | Network interface (default: eth0) |
| `-h, --help` | Show usage information |

##  Protection Against ARP Spoofing  
To protect yourself from ARP spoofing attacks:  
- Use **static ARP tables** on critical devices  
- Enable **ARP Spoofing detection tools**  
- Use **VPNs** or encrypted protocols  

##  License 
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

##  Contributing 
Contributions are welcome! Feel free to **open an issue** or **submit a pull request**.  
