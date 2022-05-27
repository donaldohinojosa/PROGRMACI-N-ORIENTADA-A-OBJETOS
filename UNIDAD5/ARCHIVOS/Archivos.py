import json
data = {}
data['alumnos'] = []
data['alumnos'].append({
    'id': '1',
    'nombre':'Imano',
    'apellido':'Arredondo',
    'edad':22,
    'grado':7 })
data['alumnos'].append({
    'id': '2',
    'nombre':'Juan',
    'apellido':'Flores',
    'edad':31,
    'grado':2 })
data['alumnos'].append({
    'id': '3',
    'nombre':'Imano',
    'apellido':'Teodoro',
    'edad':22,
    'grado':1 })

f=open("Archivos.txt", "w")
f.writelines(data)
f.close()
