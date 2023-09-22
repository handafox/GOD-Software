import errno, os, _winreg
proc_arch = os.environ['PROCESSOR_ARCHITECTURE'].lower()
proc_arch64 = os.environ['PROCESSOR_ARCHITEW6432'].lower()

if proc_arch == 'x86' and not proc_arch64:
    arch_keys = {0}
elif proc_arch == 'x86' or proc_arch == 'amd64':
    arch_keys = {_winreg.KEY_WOW64_32KEY, _winreg.KEY_WOW64_64KEY}
else:
    raise Exception("Unhandled arch: %s" % proc_arch)

for arch_key in arch_keys:
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, _winreg.KEY_READ | arch_key)
    for i in xrange(0, _winreg.QueryInfoKey(key)[0]):
        skey_name = _winreg.EnumKey(key, i)
        skey = _winreg.OpenKey(key, skey_name)
        try:
            print _winreg.QueryValueEx(skey, 'DisplayName')[0]
        except OSError as e:
            if e.errno == errno.ENOENT:
                # DisplayName doesn't exist in this skey
                pass
        finally:
            skey.Close()