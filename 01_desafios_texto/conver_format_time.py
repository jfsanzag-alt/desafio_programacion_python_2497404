def convierte_hora(hora12):
  ind_am_pm = hora12[-2:].lower()

  hora = hora12[:2]
  if ind_am_pm == "pm":
    if hora12[:2] != "12":
      hora=str(int(hora12[0:2])+12)
  else:
    if hora12[:2] == "12":
      hora = "00"

  min = hora12[3:5]

  hora24 = hora + ":" + min

  return hora24

#print(hora12.split(":")) Pasa hora12 a una lista ['05', '45pm']
#hora_convertida = ":".join(hora_lista) une los elem de hora lista separados por ":" 05:45pm

print(convierte_hora("12:40AM")) # 00:40
print(convierte_hora("04:59pm")) # 16:59
print(convierte_hora("10:00PM")) # 22:00
