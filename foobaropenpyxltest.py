import openpyxl; from openpyxl.formula import Tokenizer; from openpyxl import load_workbook
boulderdata = load_workbook('SCHBoulderScoutingSystem.xlsx', data_only=True)
#print boulderdata.get_sheet_names()
T11 = boulderdata[u'11']
#BM1 = T11['A36']
#BM2 = T11['A37']
#print BM1.value; print BM2.value
#SM = Spybot Per Match(Booleen)
SM1 = T11['B4']
SM2 = T11['B5']
SM3 = T11['B6']
SM4 = T11['B7']
SM5 = T11['B8']
SM6 = T11['B9']
SM7 = T11['B10']
SM8 = T11['B11']
SM9 = T11['B12']
SM10 = T11['B13']
SM11 = T11['B14']
SM12 = T11['B15']
print "Spybot Starting locations. Binary. 1 is yes, 0 is no, none means no data."
print SM1.value, SM2.value, SM3.value, SM4.value, SM5.value, SM6.value, SM7.value, SM8.value, SM9.value, SM10.value, SM11.value, SM12.value
#Boulder Calculations for Auton
#BA = Boulders Aquired per match(Auton)
BA1 = T11['E4']
BA2 = T11['E5']
BA3 = T11['E6']
BA4 = T11['E7']
BA5 = T11['E8']
BA6 = T11['E9']
BA7 = T11['E10']
BA8 = T11['E11']
BA9 = T11['E12']
BA10 = T11['E13']
BA11 = T11['E14']
BA12 = T11['E15']
print "Bot start with ball in auton? Binary. 1 is yes, 0 is no, none means no data."
print BA1.value, BA2.value, BA3.value, BA4.value, BA5.value, BA6.value, BA7.value, BA8.value, BA9.value, BA10.value, BA11.value, BA12.value
#BSh = Boulders Scored per match in high goal(Auton)
BSh1 = T11['F4']
BSh2 = T11['F5']
BSh3 = T11['F6']
BSh4 = T11['F7']
BSh5 = T11['F8']
BSh6 = T11['F9']
BSh7 = T11['F10']
BSh8 = T11['F11']
BSh9 = T11['F12']
BSh10 = T11['F13']
BSh11 = T11['F14']
BSh12 = T11['F15']
print "Auton High Goals."
print BSh1.value, BSh2.value, BSh3.value, BSh4.value, BSh5.value, BSh6.value, BSh7.value, BSh8.value, BSh9.value, BSh10.value, BSh11.value, BSh12.value
#BSl = Boulders Scored per match in Low goal(Auton)
BSl1 = T11['G4']
BSl2 = T11['G5']
BSl3 = T11['G6']
BSl4 = T11['G7']
BSl5 = T11['G8']
BSl6 = T11['G9']
BSl7 = T11['G10']
BSl8 = T11['G11']
BSl9 = T11['G12']
BSl10 = T11['G13']
BSl11 = T11['G14']
BSl12 = T11['G15']
print "Auton Low Goals."
print BSl1.value, BSl2.value, BSl3.value, BSl4.value, BSl5.value, BSl6.value, BSl7.value, BSl8.value, BSl9.value, BSl10.value, BSl11.value, BSl12.value
#Boulder Calculations for Teleop
#Boulder Aquired from Human Player in Teleop
BAH1 = T11['I4']
BAH2 = T11['I5']
BAH3 = T11['I6']
BAH4 = T11['I7']
BAH5 = T11['I8']
BAH6 = T11['I9']
BAH7 = T11['I10']
BAH8 = T11['I11']
BAH9 = T11['I12']
BAH10 = T11['I13']
BAH11 = T11['I14']
BAH12 = T11['I15']
print "This is if the bot acquired a ball from the human player, directly or rolling out of Secret Passage."
print BAH1.value, BAH2.value, BAH3.value, BAH4.value, BAH5.value, BAH6.value, BAH7.value, BAH8.value, BAH9.value, BAH10.value, BAH11.value, BAH12.value
#Low Goal Shots in Teleop
BTl1 = T11['L4']
BTl2 = T11['L5']
BTl3 = T11['L6']
BTl4 = T11['L7']
BTl5 = T11['L8']
BTl6 = T11['L9']
BTl7 = T11['L10']
BTl8 = T11['L11']
BTl9 = T11['L12']
BTl10 = T11['L13']
BTl11 = T11['L14']
BTl12 = T11['L15']
print "This the amount of times the bot tried to score in the low Goal Teleop"
print BTl1.value, BTl2.value, BTl3.value, BTl4.value, BTl5.value, BTl6.value, BTl7.value, BTl8.value, BTl9.value, BTl10.value, BTl11.value, BTl12.value
