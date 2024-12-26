kolichestvo = int(input())
def pysto():
    for verh in range(kolichestvo):
        print(" " * ((kolichestvo - verh)) + "/" + (verh * " ") + (verh * " ") + "\\")
    for niz in range(kolichestvo):
        print((" " * (niz + 1)) + "\\" + ((kolichestvo - niz - 1) * " ") + ((kolichestvo - niz - 1) * " ") + "/")
pysto()
print()
def polno():
    for verh in range(kolichestvo):
        print(" " * ((kolichestvo - verh)) + "/" + (verh * "/") + (verh * "\\") + "\\")
    for niz in range(kolichestvo):
        print((" " * (niz + 1)) + "\\" + ((kolichestvo - niz - 1) * "\\") + ((kolichestvo - niz - 1) * "/") + "/")
polno()