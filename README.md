# Termux_install_metasploit
This procedure refers to Gushmazko/metasploit_in_termux
# What can this program do? 
Installing metasploit in termux

# Effect map: 
![Screenshot_20220514-115023](https://user-images.githubusercontent.com/95407088/168409710-6d8dfe07-4af8-43e9-8f90-7763bf2850b8.jpg)

# How to install? 
### Auto:
```bash
pkg up && pkg install python git -y && git clone https://github.com/zhengyo/termux-install-msf.git && cd termux-install-msf && python install_msf.py
```
### Blockade the Internet in mainland China? Try this: 
```bash
bash $HOME/termux-install-msf/core/change.sh
```
