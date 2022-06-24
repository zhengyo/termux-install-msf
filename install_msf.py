# Start Python import os 
import os
# Upgrade 
os.system('pkg up -y')
# Delete the original directory 
os.system("rm -rf $HOME/metasploit-framework/;rm -rf $PREFIX/lib/metasploit-framework/")
# Uninstall the old Ruby 
os.system("apt remove ruby -y && rm -rf $PREFIX/lib/ruby")
# Install Ruby 
os.system("pkg install ruby -y")
# Install the required components 
os.system("pkg install python libiconv zlib autoconf bison clang coreutils curl findutils git apr apr-util libffi libgmp libpcap postgresql readline libsqlite openssl libtool libxml2 libxslt ncurses pkg-config wget make libgrpc termux-tools ncurses-utils ncurses unzip zip tar termux-elf-cleaner -y")
print("[-] In order to ensure the success of the download, we will execute the download command 4 times, if there are 3 errors, please ignore. ")
# Download msf 
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
# Delete the original soft connection 
os.system('rm $PREFIX/bin/msfconsole')
os.system('rm $PREFIX/bin/msfd')
os.system('rm $PREFIX/bin/msfdb')
os.system('rm $PREFIX/bin/msfrpc')
os.system('rm $PREFIX/bin/msfupdate')
os.system('rm $PREFIX/bin/msfvenom')
# Install the necessary components again 
os.system("pip install --upgrade pip")
os.system("pip install requests")
# Start the add-on program 
os.system("bash $HOME/termux-install-msf/core/gem.sh")
os.system("bash $HOME/termux-install-msf/core/sed.sh")
print("Starting metasploit framework console...")
print("")
print("")
print("")
os.system("sleep 1")
os.system("msfconsole")
os.system("rm -rf $HOME/termux-install-msf/")
