spin = input()
electric_charge = input()

if spin == '1' and electric_charge == '0':
    print('Photon Boson')
else:
    if electric_charge == '-1/3':
        print('Strange Quark')
    elif electric_charge == '2/3':
        print('Charm Quark')
    elif electric_charge == '-1':
        print('Electron Lepton')
    else:
        print('Muon Lepton')
