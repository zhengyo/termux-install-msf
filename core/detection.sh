if [ -e $HOME/metasploit-framework/msfconsole ];then
  exit
fi
  cd $HOME;git clone https://github.com/rapid7/metasploit-framework.git
