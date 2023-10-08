
n1 = float(input("Veuillez entrer la première note : "))
n2 = float(input("Veuillez entrer la deuxième note : "))
n3 = float(input("Veuillez entrer la troisième note : "))
moyenne = (n1 + n2 + n3) / 3
mention = ""


if moyenne >= 16:
    mention = "très bien"
elif moyenne >= 14:
    mention = "bien"
elif moyenne >= 12:
    mention = "assez bien"
elif moyenne >= 10:
    mention = "passable"
else:
    mention = "insuffisant"


print("Votre moyenne et mention : ", moyenne, mention)
