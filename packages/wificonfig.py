import sys

def main(argv):
 print("This command installs persistent networking by saving your")
 print("Wifi preferences in a file called dhcp.py and then also ")
 print("adding a boot parameter in boot.py to call dhcp.py")
 installNetwork = input("Do you want to proceed with the setup of wireless networking? (y|n)")
 if installNetwork == "y":
     ssid = input("Enter the SSID>")
     wkey = input("Enter the password")
     print ("Creating dhcp.py")
     dhtxt = decode_b64_to_text(DHCPB64)
     dhtxt = dhtxt.replace("SSID_VAR", ssid).replace("WKEY_VAR", wkey)
     write_text_file("/dhcp.py", dhtxt)
     print ("Appending import dhcp in boot.py")
     append_to_file("/boot.py", "\n" + "import dhcp" + "\n")
 else:
     print("Skipping network setup.. ")

 print("Network config complete.. Please reboot your microcontroller now..")




