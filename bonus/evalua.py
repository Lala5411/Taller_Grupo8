import json
import ollama

# 10 Casos etiquetados a mano (incluye 3 ambiguos)
casos_test = [
    {"texto": "Quiero agendar cita con el psicólogo para mañana.", "categoria_real": "AGENDAMIENTO"},
    {"texto": "No voy a poder ir a mi cita de deportes de las 3, por favor cancélenla.", "categoria_real": "CANCELACION"},
    {"texto": "Hola, ¿en qué horario atiende bienestar universitario los viernes?", "categoria_real": "CONSULTA"},
    {"texto": "Quiero mover mi cita de orientación del martes para el jueves.", "categoria_real": "REPROGRAMACION"},
    {"texto": "Tengo un problema grave y necesito hablar con alguien.", "categoria_real": "AGENDAMIENTO"}, # Ambiguo
    {"texto": "Ayer no pude ir a mi cita, ¿estoy bloqueado?", "categoria_real": "CONSULTA"}, # Ambiguo
    {"texto": "Por favor quiten mi cita de la tarde.", "categoria_real": "CANCELACION"},
    {"texto": "Necesito cambiar la hora de mi atención de deportes.", "categoria_real": "REPROGRAMACION"},
    {"texto": "Buenas tardes.", "categoria_real": "OTROS"}, # Ambiguo / Incompleto
    {"texto": "Inscripción a torneo de fútbol.", "categoria_real": "AGENDAMIENTO"}
]

PROMPT_V1_ZERO_SHOT = """
Clasifica el siguiente mensaje de BienestarFET en una de estas categorías:
AGENDAMIENTO, CANCELACION, REPROGRAMACION, CONSULTA, OTROS.

Responde ÚNICAMENTE con el nombre de la categoría en mayúsculas.

Mensaje: "{texto}"
"""

PROMPT_V2_FEW_SHOT = """
Eres un clasificador de intención para BienestarFET. Clasifica el mensaje en una de estas categorías según las definiciones:

DEFINICIONES:
- AGENDAMIENTO: El usuario quiere solicitar una cita nueva o acceder a un servicio por primera vez.
- CANCELACION: El usuario pide anular, borrar o cancelar una cita activa.
- REPROGRAMACION: El usuario quiere mover, cambiar de hora/fecha o aplazar una cita existente.
- CONSULTA: El usuario pregunta por horarios, sanciones, bloqueos o requisitos sin pedir cita directa.
- OTROS: Saludos, textos incompletos o solicitudes fuera de dominio.

EJEMPLOS:
Texto: "Buenas, ¿puedo pedir cita de psicología?" -> AGENDAMIENTO
Texto: "Ya no puedo asistir hoy a deportes, borren mi cupo." -> CANCELACION
Texto: "¿Será que me pueden correr la cita de las 9 am para las 10 am?" -> REPROGRAMACION
Texto: "¿Cuántas inasistencias me bloquean el sistema?" -> CONSULTA
Texto: "Hola buenos días." -> OTROS

Mensaje a clasificar: "{texto}"
Responde ÚNICAMENTE con la categoría en mayúsculas.
"""

def evaluar_modelo(nombre_modelo):
    print(f"\n==================================================")
    print(f" EVALUANDO MODELO: {nombre_modelo}")
    print(f"==================================================")
    
    aciertos_v1 = 0
    aciertos_v2 = 0
    
    for i, caso in enumerate(casos_test, 1):
        # Probar V1
        res_v1 = ollama.chat(
            model=nombre_modelo,
            messages=[{"role": "user", "content": PROMPT_V1_ZERO_SHOT.format(texto=caso['texto'])}],
            options={"temperature": 0}
        )['message']['content'].strip()
        
        # Probar V2
        res_v2 = ollama.chat(
            model=nombre_modelo,
            messages=[{"role": "user", "content": PROMPT_V2_FEW_SHOT.format(texto=caso['texto'])}],
            options={"temperature": 0}
        )['message']['content'].strip()
        
        ok_v1 = "✓" if caso['categoria_real'] in res_v1 else "✗"
        ok_v2 = "✓" if caso['categoria_real'] in res_v2 else "✗"
        
        if ok_v1 == "✓": aciertos_v1 += 1
        if ok_v2 == "✓": aciertos_v2 += 1
        
        print(f"Caso {i}: \"{caso['texto']}\"")
        print(f"  Real: {caso['categoria_real']} | V1: {res_v1} [{ok_v1}] | V2: {res_v2} [{ok_v2}]")
        
    print(f"\nRESULTADOS {nombre_modelo}:")
    print(f"  Precisión Prompt V1 (Zero-Shot): {aciertos_v1}/10 ({aciertos_v1*10}%)")
    print(f"  Precisión Prompt V2 (Few-Shot):  {aciertos_v2}/10 ({aciertos_v2*10}%)")

if __name__ == "__main__":
    evaluar_modelo("qwen3.5:4b")
    # Para probar con el modelo pequeño de 0.8b:
    try:
        evaluar_modelo("qwen3.5:0.8b")
    except Exception as e:
        print("\nNota: Para ejecutar con qwen3.5:0.8b recuerda hacer primero: ollama pull qwen3.5:0.8b")