import os
os.system('pkg up -y')
os.system("rm -rf $HOME/metasploit-framework/;rm -rf $PREFIX/lib/metasploit-framework/")
os.system("apt remove ruby && rm -rf $PREFIX/lib/ruby")
os.system("pkg install ruby -y")
os.system("pkg install python libiconv zlib autoconf bison clang coreutils curl findutils git apr apr-util libffi libgmp libpcap postgresql readline libsqlite openssl libtool libxml2 libxslt ncurses pkg-config wget make libgrpc termux-tools ncurses-utils ncurses unzip zip tar termux-elf-cleaner -y")
install.title() = input("Current country: ")
if install == 'China':
    print("[-] In order to ensure the success of the download, we will execute the download command 4 times, if there are 3 errors, please ignore. ")
    os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
    os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
    os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
else:
    os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")

os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system('rm $PREFIX/bin/msfconsole && ln -s $PREFIX/lib/metasploit-framework/msfconsole $PREFIX/bin/msfconsole')
os.system('rm $PREFIX/bin/msfd && ln -s $PREFIX/lib/metasploit-framework/msfd $PREFIX/bin/msfd')
os.system('rm $PREFIX/bin/msfdb && ln -s $PREFIX/lib/metasploit-framework/msfdb $PREFIX/bin/msfdb')
os.system('rm $PREFIX/bin/msfrpc && ln -s $PREFIX/lib/metasploit-framework/msfrpc $PREFIX/bin/msfrpc')
os.system('rm $PREFIX/bin/msfupdate && ln -s $PREFIX/lib/metasploit-framework/msfupdate $PREFIX/bin/msfupdate')
os.system('rm $PREFIX/bin/msfvenom && ln -s $PREFIX/lib/metasploit-framework/msfvenom $PREFIX/bin/msfvenom')
os.system("pip install --upgrade pip")
os.system("pip install requests")
os.system("bash $HOME/termux-install-msf/gem.sh")
os.system("bash $HOME/termux-install-msf/sed.sh")
print("Starting metasploit framework console...")
print("")
print("")
print("")
os.system("sleep 1")
os.system("msfconsole")
os.system("rm -rf $HOME/termux-install-msf/")
