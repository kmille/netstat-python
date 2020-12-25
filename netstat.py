import arrow
import psutil
from psutil import Process


def main():
    connections = psutil.net_connections()
    listen = list(filter(lambda x: x.status == 'LISTEN', connections))
    listen_sorted = sorted(listen, key=lambda x: x.laddr.port)
    print(f"{'ip':<12} {'port':<6} {'user':<16} {'started':<15} {'parent':<15} {'cwd':<30} {'cmdline'}".upper())
    for l in listen_sorted:
        ip = l.laddr.ip
        port = l.laddr.port
        if not l.pid:
            cwd, user, cmdline, started = 4 * ["NOPERM"]
        else:
            p = Process(l.pid)
            parent = p.parent().name()
            cwd = p.cwd()
            user = p.username()
            cmdline = " ".join(p.cmdline())
            started = arrow.get(p.create_time()).humanize()
        print(f"{ip:<12} {port:<6} {user:<16} {started:<15} {parent:<15} {cwd:<30} {cmdline}")


if __name__ == '__main__':
    main()
