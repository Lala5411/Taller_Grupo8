# Taller de Ingeniería de Prompts y Contexto - Caso 4: BienestarFET

**Integrantes del Grupo:**
- [Laura Catherine Quintero Vega]
- [Estefania Jimenez Peña]

**Módulo:** Diplomado en Ingeniería de Software con IA y Sistemas Agénticos  
**Institución:** Fundación Escuela Tecnológica de Neiva (FET)  
**Caso Elegido:** Caso 4 - BienestarFET  
**Modelos Evaluados:** `qwen-demo` (qwen3.5:4b), `phi-demo` (phi4-mini)  
**Equipo Utilizado:** [PC Ryzen 5, 20 GB RAM / AMD Radeon(TM) Vega 8 Graphics]  

---

## Estructura del Repositorio
- `reto1/`: Rescate de prompt malo con fórmula base y delimitadores.
- `reto2/`: System prompts del revisor (v1, v2, v3) y matriz de resistencia a prompt injection.
- `reto3/`: Encadenamiento de prompts (Few-shot -> Criterios -> Tabla de pruebas).
- `reto4/`: Razonamiento paso a paso (CoT) y gestión de la ventana de contexto.
- `bonus/`: (Opcional - Scripts de automatización en Python).

---

## Reflexión Final del Grupo

### 1. ¿Qué fue lo que mejor funcionó en el caso BienestarFET?
Definitivamente, lo que mejor nos funcionó fue ponerle límites claros al System Prompt y separar bien las instrucciones de la información que ingresa el usuario (como en el Reto 2 v2 y v3). En un sistema como BienestarFET, un usuario que no sabe podría meter texto o comentarios maliciosos dentro del código para saltarse reglas clave como la de las 2 inasistencias o pedir cita con menos de 24 horas de anticipación. Al ordenarle al modelo que trate cualquier código únicamente como datos y no como instrucciones, nos curamos en salud y logramos revisiones mucho más confiables.

### 2. ¿Qué cambiaríamos al pedirle código a una IA?
Si mañana nos toca desarrollar otra función para BienestarFET usando IA, aplicaríamos esto sin pensarlo dos veces:
- **Nada de pedir código a lo loco:**No volveríamos a soltarle un prompt libre. Usaríamos la fórmula estructurada y dejaríamos superclaro qué son las reglas usando etiquetas como (`<reglas>...</reglas>`).
- **Ir paso a paso:** No le pediríamos todo de un solo tiro; primero le pediríamos las Historias de Usuario, luego los Criterios de Aceptación (Dado/Cuando/Entonces) y, solo al final, que nos genere el código.
- **Blindar los System Prompts:** Para evitar que la IA se "invente" cosas, le marcaríamos bien la cancha desde el principio y le exigiríamos respuestas ordenadas, ya sea en formato JSON o en tablas.