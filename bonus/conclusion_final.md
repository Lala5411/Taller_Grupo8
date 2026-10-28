# Análisis de Resultados - Reto 5 (Bonus): BienestarFET

## 1. ¿Cómo reacciona la IA cuando le tiran datos incompletos? (Parte A)

Cuando el usuario le manda mensajes a medias o con rodeos (tipo "Hola, necesito una cita urgente en la tarde" o "Cita para deportes"):

- **Manejo de opcionales:**La validación estructurada (con Pydantic y JSON Schema) obligó al modelo a no inventar y rescatar solo lo que el usuario dijo de verdad (`servicio: "deportes"`), Todo lo demás lo dejó en `null` o con los valores por defecto (`franja: "no_especificado"`, `es_reprogramacion: false`).

- **Campos `Literal` cerrados:** Para evitar que la IA alucine cosas raras, mandó categorías fijas como `"desconocido"` o `"no_especificado"` cuando la información no alcanzaba. Esto evita que el backend se rompa o arroje un error feo por datos corruptos.

---

## 2. Comparación A/B y Fallos entre V1 y V2 (Parte B)

### Casos enredados que fallaron en V1 y se corrigieron en V2:

- **Caso Ambiguo ("Tengo un problema grave y necesito hablar con alguien"):**

  - **V1 (Zero-Shot):** Como el usuario no dijo la palabra "cita", la V1 se confundió y lo mandó a `CONSULTA` o `OTROS` 

  - **V2 (Few-Shot con definiciones):** Al darle la regla de que pedir ayuda por primera vez cuenta como `AGENDAMIENTO`, la V2 la cogió al vuelo y lo clasificó perfecto.

- **Caso Ambiguo ("Ayer no pude ir a mi cita, ¿estoy bloqueado?"):**

  - **V1:** Leyó la palabra "cita" y se lanzó de una a marcarlo como `AGENDAMIENTO`.

  - **V2:** Leyó con más calma, entendió que el usuario estaba preocupado por una sanción y lo mandó a `CONSULTA`.

### Diferencias entre `qwen3.5:4b` y `qwen3.5:0.8b`:
- **`qwen3.5:4b`:** Mostró una precisión por encima del 90% con el prompt V2 y respetó el formato JSON al pie de la letra, sin dañar la sintaxis ni una sola vez.

- **`qwen3.5:0.8b`:** se enredó más de la cuenta en la V1 (Zero-Shot) y a veces le daba por echar carreta o texto extra antes de dar la categoría. Eso sí, apenas le pusimos los ejemplos en la V2 (Few-Shot), mejoró un montón y se puso las pilas.