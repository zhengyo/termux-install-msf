# Upgrade 
pkg up -y
# Delete the original directory 
rm -rf $HOME/metasploit-framework/;rm -rf $PREFIX/lib/metasploit-framework/
# Uninstall the old Ruby 
apt remove ruby -y && rm -rf $PREFIX/lib/ruby
# Install Ruby 
pkg install ruby -y
# Install the required components 
pkg install python libiconv zlib autoconf bison clang coreutils curl findutils git apr apr-util libffi libgmp libpcap postgresql readline libsqlite openssl libtool libxml2 libxslt ncurses pkg-config wget make libgrpc termux-tools ncurses-utils ncurses unzip zip tar termux-elf-cleaner -y
# Download msf 
cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1
cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1
cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1
cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1
# Delete the original soft connection 
rm $PREFIX/bin/msfconsole msfd msfdb msfrpc msfupdate msfvenom
# Install the necessary components again 
pip install --upgrade pip
pip install requests
# Start the add-on program 
bash $HOME/termux-install-msf/core/gem.sh
bash $HOME/termux-install-msf/core/sed.sh
msfconsole
rm -rf $HOME/termux-install-msf/
