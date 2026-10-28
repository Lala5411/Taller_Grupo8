# Análisis Comparativo - Reto 3: BienestarFET

## 1. Lo que pasó en cada paso de la cadena de prompts
Pasamos el nuevo requisito de BienestarFET («Que el estudiante reciba un recordatorio el día anterior a su cita») a través de una cadena de tres prompts encadenados para llevarlo hasta casos de prueba:

1. **Prompt 1 (Basico para Historia de Usuario):** Le dimos dos ejemplos claros con el formato «Como..., quiero..., para...». El modelo captó de una la estructura y transformó el requisito en una historia perfecta, identificando que el objetivo del recordatorio es permitirle al estudiante confirmar o cancelar con al menos 4 horas de anticipación.
2. **Prompt 2 (Formato Fijo para Criterios Dado/Cuando/Entonces):** Le pasamos la historia entre etiquetas <historia> y le pedimos entre 3 y 5 criterios. En la primera corrida se nos descarriló un poco: la IA se puso creativa e inventó que el recordatorio se debía enviar obligatoriamente por WhatsApp y que el usuario tenía que responder con la palabra "CONFIRMAR". Nos tocó frenarla, meterle restricciones y recordarle las reglas reales de la FET (mínimo 4h para cancelar, 2 inasistencias bloquean por 30 días) para que sacara los criterios limpios.
3. **Prompt 3 (Tabla Markdown y Auto-Verificación):** Le pasamos los criterios corregidos en <criterios> y le pedimos la tabla de casos de prueba con la orden de auto-verificarse antes de entregar. El modelo generó la tabla ordenada con las columnas exigidas y, gracias al bloque de auto-verificación, detectó que le faltaba cubrir el escenario borde de la cancelación tardía (menos de 4 horas antes), agregando ese caso extra al final explícitamente..

---

## 2. Comparando la respuesta inicial vs. la respuesta con auto-verificación

- **Sin la regla de revisión:** La IA tiende a armar la tabla rápido y por encima, dejando criterios de aceptación por fuera o mezclando las entradas con los resultados esperados.

- **Con la instrucción «Antes de entregar, revisa que cada criterio tenga al menos un caso...»:** El modelo hizo una pausa cognitiva antes de botar el texto final. Identificó que había dejado por fuera la regla del bloqueo por 2 inasistencias y la ventana límite de cancelación, añadiendo los casos faltantes y marcándolos con la nota requerida.

### 3. Lo que nos dejó este reto
- **Encadenamiento:** Pedirle a la IA que pase de un requisito nuevo directamente a casos de prueba en un solo prompt es buscarse problemas o alucinaciones. Ir paso a paso (Historia -> Criterios -> Tabla) garantiza que cada nivel valide al anterior.

- **Los ejemplos mandan:** Darle un par de ejemplos bien maqueteados con el formato deseado evita perder tiempo explicándole la teoría a la IA; el modelo simplemente replica la estructura de inmediato.

3. **Forzar la auto-verificación evita vacíos:** Obligar al modelo a revisar su propia salida antes de responder es el mejor truco para que llene sus propios vacíos de lógica sin que nosotros tengamos que estar corrigiéndolo manualmente a cada rato.