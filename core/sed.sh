$PREFIX/bin/find -type f -executable -exec termux-fix-shebang \{\} \;
rm ./modules/auxiliary/gather/http_pdf_authors.rb
termux-elf-cleaner /data/data/com.tsed -i '481, 483 {s/^/#/}' $PREFIX/bin/msfvenom
cd $PREFIX/lib/metasploit-framework/
sed -i '13,15 {s/^/#/}' /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/encryption_algorithm/functionable.rb; sed -i '14 {s/^/#/}' /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp256.rb; sed -i '14 {s/^/#/}' /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp384.rb; sed -i '14 {s/^/#/}' /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp521.rb
sed -Ei "s/(\^\\\c\s+)/(\^\\\C-\\\s)/" $PREFIX/lib/metasploit-framework/lib/msf/core/exploit/remote/vim_soap.rb
sed -i '86 {s/^/#/};96 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/concurrent-ruby-1.0.5/lib/concurrent/atomic/ruby_thread_local_var.rb
sed -i '442, 476 {s/^/#/};436, 438 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/logging-2.3.0/lib/logging/diagnostic_context.rb
ln -s $PREFIX/lib/metasploit-framework/msfconsole $PREFIX/bin/msfconsole
ln -s $PREFIX/lib/metasploit-framework/msfvenom $PREFIX/bin/msfvenom
