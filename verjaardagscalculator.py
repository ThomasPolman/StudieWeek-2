import random

aantal_deelnemers = 15


def simulatie(aantal_mensen):
    verjaardagen = []
    maanden = ["Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober", "November", "December"]
    for i in range(0, aantal_mensen):
        maand = random.choice(maanden)
        if maand == "Februari":
            dag = random.randint(1, 29)
        elif maand == "April" or maand == "Juni" or maand == "September" or maand == "November":
            dag = random.randint(1, 31)
        else:
            dag = random.randint(1, 32)

        verjaardag = str(dag) + " " + maand
        verjaardagen.append(verjaardag)
        print("\nDe verjaardag van persoon %s is %s"%(i+1, verjaardag))
    kansberekening(aantal_mensen)
    match = False
    for i in range(len(verjaardagen)):
        if gelijke_verjaardag(verjaardagen, verjaardagen[i], i):
            match = True
            break
    if not match:
        print("\nGeen van de verjaardagen valt op een gelijke dag")

def kansberekening(aantal_mensen):
    if aantal_mensen < 2:
        print("\nEr is maar één persoon!")

    noemer = 365
    countdown = 364
    for i in range(2, aantal_mensen + 1):
        noemer = noemer * countdown
        countdown -= 1
    deler = 365 ** aantal_mensen
    kans = 1 - noemer / float(deler)
    afgerond_percentage = round(kans*100, 2)
    print("\nDe kans dat er een verjaardag op gelijke dag valt voor %s mensen is %s procent"%(aantal_mensen, afgerond_percentage)) 

def gelijke_verjaardag(lijst, datum, index):
    mensen = []
    for i in range(len(lijst)):
        if lijst[i] == datum and i != index:
            mensen.append(i+1)
    if mensen:
        mensen.append(index+1)
        print("\nDe volgende mensen hebben een gelijke verjaardag:")
        for persoon in mensen:
              print("\nPersoon %s"%(persoon))
        return True
    else:
        return False
    
simulatie(aantal_deelnemers)
