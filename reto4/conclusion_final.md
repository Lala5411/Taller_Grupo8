# Análisis Comparativo - Reto 4: BienestarFET

## 1. Lo que pasó en la Parte A (Cadena de Pensamiento con phi-demo)

- **Pregunta directa en una línea:** Cuando le tiramos el código a la IA de rapidez a ver por qué fallaba, solo agarró el error más evidente (que el código pedía `< 12` horas en lugar de `< 24`), Pero se comió completito el fallo de las inasistencias (`inasistencias > 2`) , dejando pasar a los estudiantes que tenían exactamente 2 faltas.

- **Evaluación paso a paso:** Cuando la pusimos a evaluar variable por variable con datos en mano (`inasistencias = 2` y `horas = 18`), no pudo tomar "atajos". Al hacer la prueba paso a paso, cayó en la cuenta de que `2 > 2` da `False` y que el sistema dejaba agendar la cita cuando no debía, encontrando el fallo grave de lógica.

---

## 2. Lo que pasó en la Parte B (Cuando la memoria no da para más)

### Prueba 1: Con `/set parameter num_ctx 512`
Al recortarle la memoria a 512 tokens y pedirle una respuesta larga, la IA llenó el vaso de una. Para la segunda pregunta, la instrucción inicial (`"Empieza con VEREDICTO:"`) quedó por fuera de la foto (se borró del contexto). Como la IA ya no la "veía", se le olvidó por completo seguir la regla en la segunda respuesta.

### Prueba 2: Con `/set system`
Al meter la regla directamente en el System Prompt, la historia fue otra. No importó qué tan larga se puso la charla ni cuánto se llenó la memoria: la orden del System Prompt se quedó bien clavada ahí. Por eso, la IA respondió ambas preguntas arrancando sin falta con la palabra "VEREDICTO:".

---

## 3. ¿Qué nos enseña todo esto?

1. **La memoria de la IA es limitada:** Si la charla se alarga mucho, lo que le pediste al principio se va al olvido por el límite de tokens.

2. **El System Prompt es el ancla:** Todo lo que sea vital (las reglas de negocio de BienestarFET, formatos o límites) tiene que ir en el System Prompt o en el Modelfile. Nunca lo dejes como un mensaje suelto en el chat.

3. **Pensar paso a paso evita cegueras:** Hacer que el modelo piense paso a paso (Chain of Thought) lo obliga a probar los datos de verdad antes de dar una respuesta, evitando que apruebe un código que viene con errores escondidos.