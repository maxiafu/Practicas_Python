def procesar_estudiantes():
    estudiantes = [
        {"nombre": "Ana", "edad": "20", "notas": [15, 18, 20]},
        {"nombre": "Carlos", "edad": "22", "notas": [12, 14, 16]}
    ]

    # --- SECCIÓN 1 ---
    total_edades = 0
    for estudiante in estudiantes:
        # BUG 1
        total_edades = total_edades + int(estudiante["edad"])
    print(f"Suma total de edades: {total_edades}")

    # --- SECCIÓN 2 ---
    notas_ana = estudiantes[0]["notas"]
    print("Notas de Ana:")
    # BUG 2
    for i in range(len(notas_ana)):
        print(f"  Nota {i + 1}: {notas_ana[i]}")

    # --- SECCIÓN 3 ---
    # BUG 3
    print(f"Estudiante seleccionado: {estudiantes[0]['nombre']}")

procesar_estudiantes()