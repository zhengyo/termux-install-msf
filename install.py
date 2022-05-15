import os
instal = input("Please return to your country, such as'China' : ")
install = instal.title()
if install == 'China':
    os.system('bash core/change_sources.sh')
    os.system('echo Install the upgrade. && apt update && apt upgrade -y')
    print("安装准备工作完成")
    os.system('bash core/change_sources.sh')
    os.system('cd core/ && python start.py')
    print("Done.")
else:
    os.system('echo Install the upgrade. && pkg up')
    os.system('cd core/ && python start.py')
    print("Done.")
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

if [ -e $PREFIX/bin/msfconsole ];then

	rm $PREFIX/bin/msfconsoleif [ -e $PREFIX/bin/msfvenom ];then

	rm $PREFIX/bin/msfvenom

fi

termux-elf-cleaner /data/data/com.termux/files/usr/lib/ruby/gems/*/gems/pg-*/lib/pg_ext.so

sed -i '481, 483 {s/^/#/}' $PREFIX/bin/msfvenom

sed -Ei "s/(\^\\\c\s+)/(\^\\\C-\\\s)/" $PREFIX/opt/metasploit-framework/lib/msf/core/exploit/remote/vim_soap.rb

sed -i '86 {s/^/#/};96 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/concurrent-ruby-1.0.5/lib/concurrent/atomic/ruby_thread_local_var.rb

sed -i '442, 476 {s/^/#/};436, 438 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/logging-2.3.0/lib/logging/diagnostic_context.rb
