# Análisis Comparativo - Reto 1: BienestarFET

## 1. Lo que la IA tuvo que adivinar con mi Prompt Malo
Al tirarle solo un prompt malo (`"Hazme una función para agendar citas."`), el modelo `qwen-demo` o tuvo de otra que inventar y dar por sentado varias cosas:

1. **Lenguaje de programación:** Supuso por su cuenta que queríamos Python, porque sí.
2. **Anticipación mínima:** Ni se enteró de la regla de las 24 horas de anticipación; o no puso validación o inventó cualquier número.
3. **Control de inasistencias:** Ignoró por completo la sanción de bloquear por 30 días a quien acumule 2 faltas en el semestre.
4. **Horario de atención:** No limitó las citas al horario de Lunes a Viernes de 8:00 a 17:00 ni a los bloques exactos de 30 minutos.
5. **Citas activas concurrentes:** Pasó por alto el límite de máximo 1 cita activa por servicio por estudiante.

---

## 2. Comparando las respuestas de la IA

### Prompt Malo vs. Prompt Nuevo (Fórmula Base)
- **Prompt Malo:** Nos soltó un código súper genérico que no servía para la FET. No revisaba horarios ni faltas y solo devolvía un True o False muy básico.
- **Prompt Nuevo:** Se notó de una la diferencia al usar la etiqueta `<reglas>`. La IA aplicó bien las 5 reglas de negocio, metió el cálculo para revisar que fueran al menos 24 horas de anticipación (`>= 24h`) y validó que estuviera entre 8:00 y 17:00.
- **Lo que aún se puede mejorar:** Aunque cumplió con todo, para asegurar que el bloque sea exactamente de 30 minutos le sirvió bastante que las variables de entrada vinieran bien tipadas.

### Prompt Nuevo vs. Prompt Variante (Sin Restricciones)
- **Prompt Nuevo (Con Restricciones):** Se limitó a usar la librería nativa `datetime` de Python,logrando un código limpio, liviano y sin enredos.
- **Prompt Variante (Sin Restricciones):** Al dejarle la puerta abierta, el modelo se puso creativo y empezó a importar librerías externas como`dateutil` o `pydantic` para validar datos, haciendo el código innecesariamente más complejo.