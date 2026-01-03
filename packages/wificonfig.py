import ubinascii
import os
import sys
import gc

def mkdir_p(path):
    parts = path.split("/")
    cur = ""
    for p in parts:
        if not p:
            continue
        cur += "/" + p
        try:
            uos.stat(cur)
        except OSError:
            try:
                uos.mkdir(cur)
            except OSError:
                pass

def write_b64_chunks_to_file(path, b64_chunks, gc_every=32):
    parent = path.rsplit("/", 1)[0]
    if parent:
        mkdir_p(parent)

    tmp = path + ".tmp"
    try:
        uos.remove(tmp)
    except OSError:
        pass

    with open(tmp, "wb") as f:
        for i, ch in enumerate(b64_chunks, 1):
            if isinstance(ch, str):
                ch = ch.encode()
            f.write(ubinascii.a2b_base64(ch))
            if i % gc_every == 0:
                gc.collect()

    try:
        uos.remove(path)
    except OSError:
        pass
    uos.rename(tmp, path)
    gc.collect()

def decode_b64_to_text(b64_chunks):
    if isinstance(b64_chunks, (tuple, list)):
        b64 = "".join(b64_chunks)
    else:
        b64 = b64_chunks
    raw = ubinascii.a2b_base64(b64.encode() if isinstance(b64, str) else b64)
    return raw.decode("utf-8")

def write_text_file(path, text):
    parent = path.rsplit("/", 1)[0]
    if parent:
        mkdir_p(parent)

    tmp = path + ".tmp"
    try:
        uos.remove(tmp)
    except OSError:
        pass
    with open(tmp, "w") as f:
        f.write(text)
    try:
        uos.remove(path)
    except OSError:
        pass
    uos.rename(tmp, path)
    gc.collect()     

def append_to_file(fname, data):
    with open(fname, "a") as f:
     f.write(data)
     f.close()



def main(argv):
 DHCPB64 = (
    "aW1wb3J0IG5ldHdvcmsKIyBOT1RFIEVkaXQgdGhpcyBmaWxlIGFuZCBjaGFuZ2UgaXQgdG8gY2hhbmdlIG5ldHdvcmsgY29ubmVjdGlvbgpzc2lkID0gIlNTSURfVkFSIgp3a2V5ID0gIldLRVlfVkFSIgoKd2xhbiA9IG5ldHdvcmsuV0xBTihuZXR3b3JrLlNUQV9JRikKd2xhbi5hY3RpdmUoVHJ1ZSkKc2Nhbm5lZCA9IHdsYW4uc2NhbigpCndsYW4uY29ubmVjdChzc2l
)
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




