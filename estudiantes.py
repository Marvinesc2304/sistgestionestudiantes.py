def buscar_estudiante(estudiantes, termino):
    resultados = []
    termino = termino.lower()
    try:
        for estudiante in estudiantes:
            nombre_completo = f"{estudiante.get('nombre', '')} {estudiante.get('apellido', '')}".lower()
            if termino in nombre_completo or termino in estudiante.get('nombre', '').lower() or termino in estudiante.get('apellido', '').lower():
                resultados.append(estudiante)
        return resultados
    except Exception as e:
        print(f"Error en busqueda: {e}")
        return []

def agregar_estudiante(estudiantes, nombre, apellido, edad, carrera, ciclo, notas):
    try:
        nuevo_estudiante = {
            "nombre": nombre.strip(),
            "apellido": apellido.strip(),
            "edad": str(edad),
            "carrera": carrera.strip(),
            "ciclo": ciclo.strip(),
            "notas": notas
        }
        if not nuevo_estudiante["nombre"]:
            print("Error: El nombre no puede estar vacio")
            return False
        if not nuevo_estudiante["apellido"]:
            print("Error: El apellido no puede estar vacio")
            return False
        if not nuevo_estudiante["carrera"]:
            print("Error: La carrera no puede estar vacia")
            return False
        if not nuevo_estudiante["ciclo"]:
            print("Error: El ciclo no puede estar vacio")
            return False
        estudiantes.append(nuevo_estudiante)
        print(f"Estudiante {nombre} {apellido} agregado correctamente")
        return True
    except Exception as e:
        print(f"Error al agregar estudiante: {e}")
        return False

def eliminar_estudiante(estudiantes, nombre, apellido):
    try:
        for i, estudiante in enumerate(estudiantes):
            if estudiante.get('nombre', '').lower() == nombre.lower() and estudiante.get('apellido', '').lower() == apellido.lower():
                eliminado = estudiantes.pop(i)
                print(f"Estudiante {eliminado['nombre']} {eliminado['apellido']} eliminado")
                return True
        print(f"No se encontro al estudiante {nombre} {apellido}")
        return False
    except Exception as e:
        print(f"Error al eliminar estudiante: {e}")
        return False

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    print("\n" + "-"*80)
    print(f"{'NOMBRE':<15} {'APELLIDO':<15} {'EDAD':<5} {'CARRERA':<15} {'CICLO':<8} {'NOTAS'}")
    print("-"*80)
    try:
        for est in estudiantes:
            nombre = est.get('nombre', 'N/A')
            apellido = est.get('apellido', 'N/A')
            edad = est.get('edad', 'N/A')
            carrera = est.get('carrera', 'N/A')
            ciclo = est.get('ciclo', 'N/A')
            notas = est.get('notas', [])
            notas_str = ';'.join(str(n) for n in notas) if notas else 'Sin notas'
            print(f"{nombre:<15} {apellido:<15} {edad:<5} {carrera:<15} {ciclo:<8} {notas_str}")
        print("-"*80)
        print(f"Total: {len(estudiantes)} estudiantes\n")
    except Exception as e:
        print(f"Error al mostrar estudiantes: {e}")