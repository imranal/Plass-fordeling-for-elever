file_not_found = False
try:
    fil = open('elevrelasjon.txt','r+')
except FileNotFoundError:
    file_not_found = True
    print("Ingen elev relasjoner funnet......danner nye relasjoner.")

if file_not_found:
    
    fil = open('elevrelasjon.txt','w')
    fil.write("Uke 45\n")

    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def find_pupil(linjenr):
        name=""
        with open(fname) as f:
            for i, l in enumerate(f):
                if i==linjenr:
                    name = l
        return name

    def first_match(fname):
        import random
        antall_elever = file_len(fname)
        even = antall_elever % 2 == 0 
        randomize_elev_seating = random.sample(range(1,antall_elever+1), antall_elever)
        count = 1
        if even:
            for nr in randomize_elev_seating:
                if count % 2 == 1: # if odd pupil
                    fil.write(str(nr) + ",")
                else: # finish pair jump line
                    fil.write(str(nr) + "\n")
                count = count + 1
        else:
            for nr in randomize_elev_seating:
                if count < antall_elever - 2:
                    if count % 2 == 1: # if odd pupil
                        fil.write(str(nr) + ",")
                    else: # finish pair jump line
                        fil.write(str(nr) + "\n")
                    count = count + 1
                else:
                    if count < antall_elever:
                        fil.write(str(nr) + ",")
                    else:
                        fil.write(str(nr) + "\n")
    first_match("10B.txt")

else:
    while True:
        print("\n\n")
        print("================================\n")
        print("|           Meny Valg          |\n")
        print("================================\n")
        print("1) Print klassekart for Uke XX  \n")
        print("2) Legg til elev i klassen      \n")
        print("3) Lag ny klassekart            \n")
        print("0) Lukk program             \n\n\n")
        value = int(input("Tast inn: "))

        if value == 0:
            break

        #elif value == 1: