import os
instal = input("Please return to your country, such as'China' : ")
install = instal.title()
if install == 'china':
    os.system('bash core/change_sources.sh')
    os.system('echo Install the upgrade. && apt update && apt upgrade -y')
    os.system('bash core/change_sources.sh')
    os.system('cd core/ && python start.py')
    print("Done.")
else:
    os.system('echo Install the upgrade. && pkg up')
    os.system('cd core/ && python start.py')
    print("Done.")
