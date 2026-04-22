def calcular_promedio(notas):
    try:
        if not notas:
            return 0.0
        return sum(notas) / len(notas)
    except ZeroDivisionError:
        return 0.0
    except TypeError:
        return 0.0

def estadisticas_completas(estudiantes):
    try:
        if not estudiantes:
            print("No hay estudiantes para calcular estadisticas")
            return None
        stats = {
            'total_estudiantes': len(estudiantes),
            'promedios_por_estudiante': [],
            'mejor_promedio': {'nombre': '', 'apellido': '', 'promedio': 0},
            'peor_promedio': {'nombre': '', 'apellido': '', 'promedio': 100},
            'promedio_general': 0,
            'carreras': {}
        }
        suma_total_notas = 0
        for estudiante in estudiantes:
            nombre = estudiante.get('nombre', 'Desconocido')
            apellido = estudiante.get('apellido', '')
            notas = estudiante.get('notas', [])
            carrera = estudiante.get('carrera', 'Sin carrera')
            promedio = calcular_promedio(notas)
            stats['promedios_por_estudiante'].append({
                'nombre': nombre,
                'apellido': apellido,
                'promedio': promedio
            })
            suma_total_notas += promedio
            if promedio > stats['mejor_promedio']['promedio']:
                stats['mejor_promedio'] = {'nombre': nombre, 'apellido': apellido, 'promedio': promedio}
            if promedio < stats['peor_promedio']['promedio'] and notas:
                stats['peor_promedio'] = {'nombre': nombre, 'apellido': apellido, 'promedio': promedio}
            if carrera not in stats['carreras']:
                stats['carreras'][carrera] = {'total': 0, 'suma_promedios': 0}
            stats['carreras'][carrera]['total'] += 1
            stats['carreras'][carrera]['suma_promedios'] += promedio
        if stats['total_estudiantes'] > 0:
            stats['promedio_general'] = suma_total_notas / stats['total_estudiantes']
        return stats
    except Exception as e:
        print(f"Error al calcular estadisticas: {e}")
        return None

def mostrar_estadisticas(estadisticas):
    if not estadisticas:
        print("No hay estadisticas disponibles")
        return
    try:
        print("\n" + "-"*50)
        print("ESTADISTICAS DEL SISTEMA")
        print("-"*50)
        print(f"\nTotal de estudiantes: {estadisticas['total_estudiantes']}")
        print(f"\nMejor promedio: {estadisticas['mejor_promedio']['nombre']} {estadisticas['mejor_promedio']['apellido']} ({estadisticas['mejor_promedio']['promedio']:.2f})")
        print(f"Peor promedio: {estadisticas['peor_promedio']['nombre']} {estadisticas['peor_promedio']['apellido']} ({estadisticas['peor_promedio']['promedio']:.2f})")
        print(f"\nPromedio general: {estadisticas['promedio_general']:.2f}")
        print("\nPor carrera:")
        for carrera, datos in estadisticas['carreras'].items():
            promedio_carrera = datos['suma_promedios'] / datos['total'] if datos['total'] > 0 else 0
            print(f"   {carrera}: {datos['total']} estudiantes, promedio: {promedio_carrera:.2f}")
        print("\nTop 3 mejores estudiantes:")
        top_3 = sorted(estadisticas['promedios_por_estudiante'], 
                      key=lambda x: x['promedio'], reverse=True)[:3]
        for i, est in enumerate(top_3, 1):
            print(f"   {i}. {est['nombre']} {est['apellido']}: {est['promedio']:.2f}")
        print("-"*50 + "\n")
    except Exception as e:
        print(f"Error al mostrar estadisticas: {e}")

def texto_generado(estadisticas, estudiantes):
    try:
        texto = []
        texto.append("-"*60)
        texto.append("REPORTE COMPLETO DE ESTUDIANTES")
        texto.append("-"*60)
        texto.append(f"\nFecha: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        texto.append(f"\nTotal estudiantes: {estadisticas['total_estudiantes']}")
        texto.append(f"Promedio general: {estadisticas['promedio_general']:.2f}")
        texto.append(f"\nMejor estudiante: {estadisticas['mejor_promedio']['nombre']} {estadisticas['mejor_promedio']['apellido']} ({estadisticas['mejor_promedio']['promedio']:.2f})")
        texto.append("\n" + "-"*60)
        texto.append("LISTADO DETALLADO:")
        texto.append("-"*60)
        for est in estudiantes:
            nombre = est.get('nombre', 'N/A')
            apellido = est.get('apellido', 'N/A')
            carrera = est.get('carrera', 'N/A')
            ciclo = est.get('ciclo', 'N/A')
            notas = est.get('notas', [])
            promedio = calcular_promedio(notas)
            texto.append(f"\n{nombre} {apellido}")
            texto.append(f"  Carrera: {carrera}")
            texto.append(f"  Ciclo: {ciclo}")
            texto.append(f"  Notas: {notas}")
            texto.append(f"  Promedio: {promedio:.2f}")
        return "\n".join(texto)
    except Exception as e:
        print(f"Error al generar reporte: {e}")
        return ""