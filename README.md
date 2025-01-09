## AI Agents Demo

This Demo is linked to an Introduction to Autonomous Agent

## Credits
This demo is based on a template provided by Tyler Ai.

## Setup
```bash
pip install -r requirements.txt
```

### Dual Windows-Linux setup to use ollama local api from Windows.

It require WSL

From Windows
```bash
netsh innetsh advfirewall firewall delete rule name="Allow Port 11434"
netsh advfirewall firewall delete rule name="Allow ICMPv4-In"
interface portproxy delete v4tov4 listenaddress=172.31.32.1 listenport=11434
```

Check connection between WSL and Windows

From Windows
```bash
ipconfig | findstr "172."
```

From WSL
```
ip a
```
Let's pretend that
Windows has 172.31.32.1 (ipconfig).
WSL has 172.31.34.201 (ip on eth0).

```
netsh advfirewall firewall add rule name="Allow Port 11434" dir=in action=allow protocol=TCP localport=11434
```

Test
```
curl http://172.31.32.1:11434
```

## Authors

- [Noah Kohrs](https://github.com/noahkohrs)
- [Thibaut Haberer](https://github.com/ThibHab)