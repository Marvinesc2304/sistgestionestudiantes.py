import sys
from archivos import leer_csv, guardar_csv, exportar_json
from estudiantes import buscar_estudiante, agregar_estudiante, eliminar_estudiante, mostrar_estudiantes
from estadisticas import estadisticas_completas, mostrar_estadisticas, texto_generado

ARCHIVO_CSV = "tarea_de_Estudiantes.csv"

def mostrar_menu():
    print("\n" + "-"*50)
    print("SISTEMA DE GESTION DE ESTUDIANTES")
    print("-"*50)
    print("1. Mostrar todos los estudiantes")
    print("2. Buscar estudiante")
    print("3. Agregar estudiante")
    print("4. Eliminar estudiante")
    print("5. Ver estadisticas")
    print("6. Guardar cambios")
    print("7. Exportar a JSON")
    print("8. Generar reporte de texto")
    print("9. Salir y guardar")
    print("-"*50)

def buscar_menu(estudiantes):
    try:
        termino = input("\nIngrese nombre o apellido a buscar: ").strip()
        if not termino:
            print("Termino de busqueda vacio")
            return
        resultados = buscar_estudiante(estudiantes, termino)
        if resultados:
            print(f"\nSe encontraron {len(resultados)} estudiante(s):")
            mostrar_estudiantes(resultados)
        else:
            print(f"No se encontraron estudiantes con '{termino}'")
    except Exception as e:
        print(f"Error en busqueda: {e}")

def agregar_menu(estudiantes):
    try:
        print("\nAGREGAR NUEVO ESTUDIANTE")
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("Error: El nombre es obligatorio")
            return
        apellido = input("Apellido: ").strip()
        if not apellido:
            print("Error: El apellido es obligatorio")
            return
        while True:
            try:
                edad = int(input("Edad: "))
                if edad <= 0 or edad > 120:
                    print("Error: Edad invalida (debe ser entre 1 y 120)")
                    continue
                break
            except ValueError:
                print("Error: Por favor ingrese un numero valido")
        carrera = input("Carrera: ").strip()
        if not carrera:
            print("Error: La carrera es obligatoria")
            return
        ciclo = input("Ciclo (ej: 1ro, 2do, 3ro, etc): ").strip()
        if not ciclo:
            print("Error: El ciclo es obligatorio")
            return
        notas = []
        print("Ingrese notas (deje vacio para terminar):")
        while True:
            try:
                nota_input = input(f"Nota {len(notas)+1}: ").strip()
                if not nota_input:
                    break
                nota = float(nota_input)
                if 0 <= nota <= 100:
                    notas.append(int(nota) if nota.is_integer() else nota)
                else:
                    print("Error: Nota debe estar entre 0 y 100")
            except ValueError:
                print("Error: Ingrese un numero valido")
        agregar_estudiante(estudiantes, nombre, apellido, edad, carrera, ciclo, notas)
    except Exception as e:
        print(f"Error al agregar estudiante: {e}")

def eliminar_menu(estudiantes):
    try:
        nombre = input("\nIngrese el nombre del estudiante a eliminar: ").strip()
        if not nombre:
            print("Error: Nombre vacio")
            return
        apellido = input("Ingrese el apellido del estudiante a eliminar: ").strip()
        if not apellido:
            print("Error: Apellido vacio")
            return
        resultados = buscar_estudiante(estudiantes, f"{nombre} {apellido}")
        if resultados:
            print("\nSe eliminara al siguiente estudiante:")
            mostrar_estudiantes(resultados)
            confirmar = input("Esta seguro? (s/n): ").lower()
            if confirmar == 's':
                eliminar_estudiante(estudiantes, nombre, apellido)
            else:
                print("Eliminacion cancelada")
        else:
            print(f"No se encontro al estudiante {nombre} {apellido}")
    except Exception as e:
        print(f"Error al eliminar: {e}")

def guardar_cambios(estudiantes):
    return guardar_csv(ARCHIVO_CSV, estudiantes)

def main():
    print("\nIniciando Sistema de Gestion de Estudiantes...")
    estudiantes = leer_csv(ARCHIVO_CSV)
    if not estudiantes:
        print("No se pudieron cargar datos. Se iniciara con lista vacia.")
        estudiantes = []
    print(f"{len(estudiantes)} estudiantes cargados")
    cambios_pendientes = False
    while True:
        try:
            mostrar_menu()
            opcion = input("\nSeleccione una opcion (1-9): ").strip()
            if opcion == '1':
                mostrar_estudiantes(estudiantes)
            elif opcion == '2':
                buscar_menu(estudiantes)
            elif opcion == '3':
                agregar_menu(estudiantes)
                cambios_pendientes = True
            elif opcion == '4':
                eliminar_menu(estudiantes)
                cambios_pendientes = True
            elif opcion == '5':
                stats = estadisticas_completas(estudiantes)
                if stats:
                    mostrar_estadisticas(stats)
            elif opcion == '6':
                if guardar_cambios(estudiantes):
                    cambios_pendientes = False
            elif opcion == '7':
                if exportar_json(estudiantes):
                    print("Reporte JSON exportado exitosamente")
            elif opcion == '8':
                stats = estadisticas_completas(estudiantes)
                if stats:
                    reporte = texto_generado(stats, estudiantes)
                    if reporte:
                        try:
                            with open("reporte_completo.txt", "w", encoding='utf-8') as f:
                                f.write(reporte)
                            print("Reporte guardado en 'reporte_completo.txt'")
                        except Exception as e:
                            print(f"Error al guardar reporte: {e}")
            elif opcion == '9':
                print("\nCerrando sistema...")
                if cambios_pendientes:
                    print("Hay cambios sin guardar.")
                    guardar = input("Desea guardar antes de salir? (s/n): ").lower()
                    if guardar == 's':
                        guardar_cambios(estudiantes)
                print("Hasta luego")
                sys.exit(0)
            else:
                print("Opcion invalida. Por favor seleccione 1-9")
        except KeyboardInterrupt:
            print("\n\nInterrupcion detectada. Saliendo...")
            if cambios_pendientes:
                guardar = input("Guardar cambios antes de salir? (s/n): ").lower()
                if guardar == 's':
                    guardar_cambios(estudiantes)
            sys.exit(0)
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Por favor, intente nuevamente")

if __name__ == "__main__":
    main()

print: 'hola mundo equisde'
