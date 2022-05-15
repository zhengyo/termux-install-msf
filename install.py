import os
instal = input("Please return to your country, such as 'China' : ")
install = instal.title()
if install == 'China':
    os.system('bash core/change_sources.sh')
    print('Install the upgrade.')
    os.sysytem('apt update && apt upgrade -y'?
else:
    os.system('echo Install the upgrade. && pkg up')
os.system("rm -rf $HOME/metasploit-framework/;rm -rf $PREFIX/lib/metasploit-framework/")
os.system("apt remove ruby && rm -rf $PREFIX/lib/ruby")
os.system("pkg install ruby -y")
os.system("pkg install python libiconv zlib autoconf bison clang coreutils curl findutils git apr apr-util libffi libgmp libpcap postgresql readline libsqlite openssl libtool libxml2 libxslt ncurses pkg-config wget make libgrpc termux-tools ncurses-utils ncurses unzip zip tar termux-elf-cleaner -y")
print("[-] In order to ensure the success of the download, we will execute the download command 4 times, if there are 3 errors, please ignore. ")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system("cd $PREFIX/lib && git clone https://github.com/rapid7/metasploit-framework.git --depth=1")
os.system('rm $PREFIX/bin/msfconsole && ln -s $PREFIX/lib/metasploit-framework/msfconsole $PREFIX/bin/msfconsole')
os.system('rm $PREFIX/bin/msfd && ln -s $PREFIX/lib/metasploit-framework/msfd $PREFIX/bin/msfd')
os.system('rm $PREFIX/bin/msfdb && ln -s $PREFIX/lib/metasploit-framework/msfdb $PREFIX/bin/msfdb')
os.system('rm $PREFIX/bin/msfrpc && ln -s $PREFIX/lib/metasploit-framework/msfrpc $PREFIX/bin/msfrpc')
os.system('rm $PREFIX/bin/msfupdate && ln -s $PREFIX/lib/metasploit-framework/msfupdate $PREFIX/bin/msfupdate')
os.system('rm msfvenom && ln -s $PREFIX/lib/metasploit-framework/msfvenom $PREFIX/bin/msfvenom')
pip install --upgrade pip
pip install requests
cd $PREFIX/lib/metasploit-framework
gem install bundler
sed 's|nokogiri (1.*)|nokogiri (1.8.0)|g' -i Gemfile.lock
gem install nokogiri -v 1.8.0 -- --use-system-libraries
gem install actionpack
bundle update activesupport
bundle update --bundler
bundle install -j$(nproc --all)
$PREFIX/bin/find -type f -executable -exec termux-fix-shebang \{\} \;
rm ./modules/auxiliary/gather/http_pdf_authors.rb
termux-elf-cleaner /data/data/com.tsed -i '481, 483 {s/^/#/}' $PREFIX/bin/msfvenom
sed -Ei "s/(\^\\\c\s+)/(\^\\\C-\\\s)/" $PREFIX/opt/metasploit-framework/lib/msf/core/exploit/remote/vim_soap.rb
sed -i '86 {s/^/#/};96 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/concurrent-ruby-1.0.5/lib/concurrent/atomic/ruby_thread_local_var.rb
sed -i '442, 476 {s/^/#/};436, 438 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/logging-2.3.0/lib/logging/diagnostic_context.rb
