dtn = str(input("informe sua data de nascimento "))
ddtn = int(dtn[0:2])
mdtn = int(dtn[3:5])
adtn = int(dtn[6:10])

atn = str(input("Informe o data de hoje"))
datn = int(atn[0:2])
matn = int(atn[3:5])
aatn = int(atn[6:10])

difa = aatn - adtn
fifa = difa + 17

print("Sua idade é de", difa,"Anos, E daqui à 17 anos terá", fifa,"Anos ")