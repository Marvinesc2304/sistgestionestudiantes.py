# Sistema de Gestión de Estudiantes

Sistema en Python para gestionar información de estudiantes, incluyendo registro de notas, cálculo de promedios, estadísticas por carrera y exportación de reportes.

## Requisitos

- Python 3.7 o superior
- No requiere librerías externas (solo biblioteca estándar)

## Estructura del Proyecto


gestion_estudiantes/
│
├── ingreso_de_estudiantes_.py # Programa principal (menú interactivo)
├── archivos.py # Manejo de archivos CSV y JSON
├── estudiantes.py # Lógica CRUD de estudiantes
├── estadisticas.py # Cálculos y reportes estadísticos
├── tarea_de_Estudiantes.csv # Base de datos (se crea automáticamente)
└── README.md # Este archivo

text


Primera ejecución: Se creará automáticamente el archivo tarea_de_Estudiantes.csv con datos de ejemplo.

Uso del Programa
Al ejecutar, aparecerá un menú con las siguientes opciones:

Opción	Descripción
1	Mostrar todos los estudiantes registrados
2	Buscar estudiante por nombre o apellido
3	Agregar nuevo estudiante (nombre, apellido, edad, carrera, ciclo, notas)
4	Eliminar estudiante por nombre y apellido
5	Ver estadísticas (promedios, mejor/peor estudiante, análisis por carrera)
6	Guardar cambios manualmente en el archivo CSV
7	Exportar todos los datos a un archivo JSON
8	Generar reporte de texto completo
9	Salir del programa (pregunta si desea guardar cambios)


Formato del Archivo CSV
El archivo tarea_de_Estudiantes.csv tiene la siguiente estructura:

csv
nombre,apellido,edad,carrera,ciclo,notas
Carlos,Perez,20,Sistemas,4to,85;90;78
Ana,Gomez,22,Electronica,6to,92;88;95
Luis,Martinez,21,Sistemas,5to,70;75;80
Maria,Lopez,20,Industrial,4to,88;91;87
Las notas se almacenan separadas por punto y coma (;)

El programa convierte automáticamente las notas a lista de números


Funcionalidades Principales
Gestión de Estudiantes
Agregar estudiantes con nombre, apellido, edad, carrera, ciclo y notas

Buscar por nombre o apellido (búsqueda parcial)

Eliminar estudiantes por nombre y apellido

Visualizar todos los estudiantes en formato tabla

Estadísticas
Promedio general de todos los estudiantes

Mejor y peor promedio individual

Promedio por carrera

Top 3 mejores estudiantes

Promedio individual por estudiante

Persistencia
Guardado automático en CSV

Exportación a JSON

Generación de reporte de texto

Manejo de errores con try/except en todas las operaciones
