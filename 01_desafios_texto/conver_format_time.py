from datetime import datetime

def convierte_hora(hora12):
  hora24=""
  
  ind_am_pm = hora12[6] + hora12[7]
  print(ind_am_pm)

  if ind_am_pm == "PM": 
    hora=str(int(hora12[0:2])+12)
  else:
    hora = hora12[0:2]

  min = hora12[3:5]
  print(hora)
  print(min)

  hora24 = hora + ":" + min

  return hora24


hora12="05:25 AM"
print(hora12)
print(convierte_hora(hora12))