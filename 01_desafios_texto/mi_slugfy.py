def slugify(cadena):
    cad = cadena.replace(" ", "-")

    for letra in cad:
        if not letra.isalnum() and letra != "-" and letra != "_":
            cad = cad.replace(letra,"")
    return(cad)

print(slugify("www. def/ casa*por" ))  #www_def_casa_por

print(slugify("_texto% con caracteres$# especial-es")) # texto-con-caracteres-especial-es
print(slugify("Este es un ejemplo!!!")) # este-es-un-ejemplo
