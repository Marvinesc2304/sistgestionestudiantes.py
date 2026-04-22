import csv
import json
import os

def leer_csv(nombre_archivo):
    estudiantes = []
    try:
        if not os.path.exists(nombre_archivo):
            crear_archivo_ejemplo(nombre_archivo)
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if 'notas' in fila:
                    try:
                        fila['notas'] = [int(n) for n in fila['notas'].split(';')]
                    except ValueError:
                        fila['notas'] = []
                estudiantes.append(fila)
        return estudiantes
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return []
    except PermissionError:
        print(f"Error: No hay permisos para leer {nombre_archivo}")
        return []
    except Exception as e:
        print(f"Error inesperado al leer CSV: {e}")
        return []

def guardar_csv(nombre_archivo, estudiantes):
    if not estudiantes:
        print("No hay datos para guardar")
        return False
    try:
        headers = estudiantes[0].keys()
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=headers)
            escritor.writeheader()
            for estudiante in estudiantes:
                fila = estudiante.copy()
                if 'notas' in fila and isinstance(fila['notas'], list):
                    fila['notas'] = ';'.join(str(n) for n in fila['notas'])
                escritor.writerow(fila)
        print(f"Datos guardados en {nombre_archivo}")
        return True
    except PermissionError:
        print(f"Error: No hay permisos para escribir en {nombre_archivo}")
        return False
    except Exception as e:
        print(f"Error inesperado al guardar CSV: {e}")
        return False

def exportar_json(estudiantes, nombre_archivo="reporte_estudiantes.json"):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)
        print(f"Reporte exportado a {nombre_archivo}")
        return True
    except PermissionError:
        print(f"Error: No hay permisos para escribir {nombre_archivo}")
        return False
    except Exception as e:
        print(f"Error al exportar JSON: {e}")
        return False

def crear_archivo_ejemplo(nombre_archivo):
    datos_de_estudiantes = [
        {"nombre": "Carlos", "apellido": "Perez", "edad": "20", "carrera": "Sistemas", "ciclo": "4to", "notas": "85;90;78"},
        {"nombre": "Ana", "apellido": "Gomez", "edad": "22", "carrera": "Electronica", "ciclo": "6to", "notas": "92;88;95"},
        {"nombre": "Luis", "apellido": "Martinez", "edad": "21", "carrera": "Sistemas", "ciclo": "5to", "notas": "70;75;80"},
        {"nombre": "Maria", "apellido": "Lopez", "edad": "20", "carrera": "Industrial", "ciclo": "4to", "notas": "88;91;87"}
    ]
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            headers = ["nombre", "apellido", "edad", "carrera", "ciclo", "notas"]
            escritor = csv.DictWriter(archivo, fieldnames=headers)
            escritor.writeheader()
            escritor.writerows(datos_de_estudiantes)
        print(f"Archivo {nombre_archivo} creado con datos de ejemplo")
    except Exception as e:
        print(f"Error al crear archivo ejemplo: {e}")