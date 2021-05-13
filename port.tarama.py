import os
os.system("clear")
print("-"*65)
print("      Port Tarama Saldırısına Hoşgeldiniz instagram = zumrudu_anka_team      ")
print("      Bu Araç Treangle Tarafından Oluşturulmuştur      ")
print("-"*65)


hedef = input("Lütfen Hedef Ip giriniz : ")
os.system("nmap -A -sV" + " " + hedef)