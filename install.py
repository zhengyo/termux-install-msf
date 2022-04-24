import os
install1 = input("Please return to your country, such as'China' : ")
if install1.title() == 'china':
    os.system('bash core/change-sources.sh')
    os.system('echo Install the upgrade. && pkg up')
    os.system('cd core/ && python start.py')
    print("Done.")
else:
    os.system('echo Install the upgrade. && pkg up')
    os.system('cd core/ && python start.py')
    print("Done.")
