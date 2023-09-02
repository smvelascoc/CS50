def Main():
    nom=input("")
    print(convert(nom))

def convert(nm):
    nm=nm.replace(":)","🙂").replace(":(","🙁")
    return nm

Main()