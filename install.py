import os
install1 = input("Please return to your country, such as'China' : ")
if install1.title() == 'china':
    os.system('sed -i 's@^(deb.*stable main)$@#\1\ndeb https://mirrors.hit.edu.cn/termux stable main@' $PREFIX/etc/apt/sources.list ')
    os.system('echo Install the upgrade. && pkg up')
    os.system('cd core/ && python start.py')
    print("Done.")
else:
    os.system('echo Install the upgrade. && pkg up')
    os.system('cd core/ && python start.py')
    print("Done.")
