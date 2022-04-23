import os
install1 = input("Do you really want to install msf? Will take up 1.3 gigabytes of space? [y/n]: ")
if install1 == 'y':
    os.system('echo Install the upgrade. && pkg up')
    os.system('cd core/ && python start.py')
    print("Done.")
else:
    exit()
