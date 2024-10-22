TempoExperiencia = 5
TempoExperiencia = int(input("Tempo de Experiencia: "))

if TempoExperiencia < 2:
    print("Nivel de Conhecimento Junior")
elif TempoExperiencia > 2 and TempoExperiencia < 5:
    print("Nivel de Conhecimento Pleno")
else:
    print("Nivel de Conhecimento Pleno")