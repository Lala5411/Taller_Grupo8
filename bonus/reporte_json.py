import json
from typing import Literal, Optional
from pydantic import BaseModel, Field
import ollama

# 1. Definición del Esquema Pydantic para BienestarFET
class SolicitudCitaBienestar(BaseModel):
    servicio: Literal["asesoria_psicologica", "deportes", "orientacion_vocacional", "desconocido"] = Field(
        description="El servicio de bienestar solicitado por el estudiante."
    )
    fecha_preferida: Optional[str] = Field(
        default=None, 
        description="La fecha en formato YYYY-MM-DD o descripción de fecha si la menciona."
    )
    franja: Literal["manana", "tarde", "no_especificado"] = Field(
        description="Franja horaria preferida (manana de 8 a 12, tarde de 12 a 17)."
    )
    es_reprogramacion: bool = Field(
        description="Indica si el mensaje menciona cambiar o correr una cita previa."
    )

# 2. Los 6 Mensajes de Prueba (incluye 2 ambiguos/incompletos)
mensajes_prueba = [
    # Mensaje 1: Completo
    "Hola, quisiera agendar una cita de asesoria psicologica para el proximo lunes 15 de mayo por la mañana por favor.",
    # Mensaje 2: Completo reprogramación
    "Buenas tardes, necesito reprogramar mi cita de deportes para el viernes en la tarde.",
    # Mensaje 3: Orientación vocacional
    "Quiero hablar con alguien de orientación vocacional mañana a las 9 am.",
    # Mensaje 4: Completo
    "Me gustaría pedir cita para gimnasio/deportes el jueves a las 3 pm.",
    # Mensaje 5: AMBIGUO 1 (Falta servicio y fecha concreta)
    "Hola, necesito una cita urgente en la tarde porque tengo un problema personal.",
    # Mensaje 6: AMBIGUO 2 (Incompleto)
    "Cita para deportes."
]

def extraer_datos(mensaje: str):
    prompt = f"""
    Extrae la información relevante del siguiente mensaje de un estudiante para agendar una cita en BienestarFET.
    
    Mensaje: "{mensaje}"
    """
    
    response = ollama.chat(
        model="qwen3.5:4b",
        messages=[{"role": "user", "content": prompt}],
        format=SolicitudCitaBienestar.model_json_schema(),
        options={"temperature": 0}
    )
    
    datos_dict = json.loads(response['message']['content'])
    return datos_dict

if __name__ == "__main__":
    print("=== EJECUCIÓN PARTE A: EXTRACCIÓN JSON VALIDADA CON PYDANTIC ===\n")
    for i, msg in enumerate(mensajes_prueba, 1):
        print(f"--- Mensaje {i} ---")
        print(f"Texto: \"{msg}\"")
        try:
            resultado = extraer_datos(msg)
            print("JSON Extraído:")
            print(json.dumps(resultado, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"Error al procesar: {e}")
        print("\n")