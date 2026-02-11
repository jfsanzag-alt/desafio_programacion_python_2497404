# Son anagramas ramo y mora
def es_anagrama(pal1, pal2):
    pal1_ord = sorted(pal1.lower())
    pal2_ord = sorted(pal2.lower())
    print(pal1_ord)
    print(pal2_ord)

    return pal1_ord == pal2_ord

print(es_anagrama("pedo", "ramo"))
print(es_anagrama("mora", "ramo"))
print(es_anagrama("Zamora", "ramoza"))
print(es_anagrama("calor", "coral")) # True