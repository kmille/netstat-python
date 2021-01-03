# simple netstat in python

![my first Github action example](https://github.com/kmille/netstat-python/workflows/First%20example/badge.svg) ![playing with pytest](https://github.com/kmille/netstat-python/workflows/Run%20python%20tests/badge.svg) ![latest tag](https://img.shields.io/github/v/tag/kmille/netstat-python?sort=semver) ![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)

## install

```bash
python3 -m venv venv
source venv/bin/activate
pip install arrow
pip install psutil
sudo python netstat.py
```

## run it

```bash
(venv) kmille@linbox pnetstat master % sudo python netstat.py
IP           PORT   USER             STARTED         PARENT          CWD                            CMDLINE
::           22     root             a week ago      systemd         /                              sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups
0.0.0.0      22     root             a week ago      systemd         /                              sshd: /usr/bin/sshd -D [listener] 0 of 10-100 startups
127.0.0.53   53     systemd-resolve  a week ago      systemd         /                              /usr/lib/systemd/systemd-resolved
127.0.0.1    631    root             a week ago      systemd         /                              /usr/bin/cupsd -l
::1          631    root             a week ago      systemd         /                              /usr/bin/cupsd -l
127.0.0.1    2222   kmille           2 hours ago     VBoxSVC         /home/kmille/.config/i3        /usr/lib/virtualbox/VirtualBoxVM --comment hackthebox --startvm cf13e0dd-103c-426f-9d58-d6fee9bb8a49 --no-startvm-errormsgbox
127.0.0.1    8081   kmille           2 hours ago     VBoxSVC         /home/kmille/.config/i3        /usr/lib/virtualbox/VirtualBoxVM --comment hackthebox --startvm cf13e0dd-103c-426f-9d58-d6fee9bb8a49 --no-startvm-errormsgbox

```

