import os
os.system("rm -rf $HOME/metasploit-framework/;rm -rf $PREFIX/lib/metasploit-framework/")
os.system("apt remove ruby && rm -rf $PREFIX/lib/ruby")
os.system("pkg install ruby -y")
os.system("pkg install python libiconv zlib autoconf bison clang coreutils curl findutils git apr apr-util libffi libgmp libpcap postgresql readline libsqlite openssl libtool libxml2 libxslt ncurses pkg-config wget make libgrpc termux-tools ncurses-utils ncurses unzip zip tar termux-elf-cleaner -y")
print("[-] In order to ensure the success of the download, we will execute the download command 4 times, if there are 3 errors, please ignore. ")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib metasploit-framework; sed -i '13,15 {s/^/#/}' /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/encryption_algorithm/functionable.rb; sed -i '14 {s/^/#/}' /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp256.rb; sed -i '14 {s/^/#/}' /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp384.rb; sed -i '14 {s/^/#/}' /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp521.rb;")
os.system('ln -s $PREFIX/lib/metasploit-framework/msfconsole $PREFIX/bin/msfconsole')
os.system('ln -s $PREFIX/lib/metasploit-framework/msfd $PREFIX/bin/msfd')
os.system('ln -s $PREFIX/lib/metasploit-framework/msfdb $PREFIX/bin/msfdb')
os.system('ln -s $PREFIX/lib/metasploit-framework/msfrpc $PREFIX/bin/msfrpc')
os.system('ln -s $PREFIX/lib/metasploit-framework/msfupdate $PREFIX/bin/msfupdate')
os.system('ln -s $PREFIX/lib/metasploit-framework/msfvenom $PREFIX/bin/msfvenom')
os.system("clear")
os.system('bash initialization.sh')
print("start metasploit......")
os.system('msfconsole')
os.system('rm -rf $HOME/termux-install-msf')
exit()
