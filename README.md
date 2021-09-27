# libSSH-Authentication-Bypass
Spawn to shell without any credentials by using CVE-2018-10933

Exploit-DB : https://www.exploit-db.com/exploits/45638

Information about CVE-2018-10933 by libSSH : https://www.libssh.org/security/advisories/CVE-2018-10933.txt

Bugfix Release by libSSH : https://www.libssh.org/2018/10/16/libssh-0-8-4-and-0-7-6-security-and-bugfix-release/

### Usage
```
// If paramiko==2.0.8 doesn't works try : pip install paramiko==2.4.2

pip install -r requirements.txt
python libsshauthbypass.py --help

Example:
python libsshauthbypass.py --host 0.0.0.0 --port 22 --command "cat /etc/passwd" --logfile newlogfile.log
```

## Youtube videos that shows how to exploit libSSH by using this PoC (Proof Of Concept) 
[PoC_1](https://www.youtube.com/watch?v=2mBNS2vxSIU)

[PoC_2](https://www.youtube.com/watch?v=ZSWQjmfcn4g)


## Find the right server with these fingerprints:
https://gist.github.com/0x4D31/35ddb0322530414bbb4c3288292749cc

## Check the version of server that you trying to bypass with testversionofserver.py
If output is 0.7.5, 0.6.*, or lowest then the server is vulnerable.

If isn't then it's probably patched, truncated or not using libSSH.

## Shodan.io libSSH
( 22 Port is default, other ports like (2222, 3333, 4444) might be including libSSH )

![](https://i.imgur.com/SWEfcGR.png)
