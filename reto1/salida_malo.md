Claro que si­. Como no especificaste un lenguaje de programacion concreto,
te proporcionare dos enfoques muy comunes:

1.  **En JavaScript (Frontend):** Ideal si estas creando una pagina web 
interactiva donde el usuario selecciona fecha y hora.
2.  **En Python (Backend/Logistica):** Ideal si necesitas guardar los datos
datos en una base de datos o procesar la agenda programaticamente.

AquÃ­ tienes las soluciones:

---

### OpciÃ³n 1: JavaScript (Para una interfaz web)

Esta funcion simula el proceso de agendar una cita validando que la fecha n
no sea pasada y que haya disponibilidad (en este caso, simulado).

```javascript
function agendarCita(cliente, servicio, fecha, hora) {
    // 1. Validaciones basicas
    if (!cliente || !servicio || !fecha || !hora) {
        return alert("Por favor, completa todos los campos.");
    }

    const fechaObj = new Date(fecha);
    const hoy = new Date();
    
    // Evitar fechas pasadas
    if (fechaObj <= hoy) {
        return alert("No puedes agendar citas para el dia de hoy o fechas pasadas.");
    }

    // Simulacion de verificacion de disponibilidad (en un caso real, esto ira a una API)
    const disponibilidad = Math.random() > 0.2; // 80% de probabilidad de estar libre
    
    if (!disponibilidad) {
        return alert("Lo sentimos, ese horario ya esta ocupado.");
    }

    // 2. Crear el objeto de la cita
    const nuevaCita = {
        id: Date.now(), // ID unico basado en el tiempo actual
        cliente: cliente,
        servicio: servicio,
        fecha: fecha,
        hora: hora,
        estado: "Confirmada",
        fechaAgendamiento: new Date().toLocaleString()
    };

    // 3. Guardar (Simulado)
    const citas = JSON.parse(localStorage.getItem('misCitas')) || [];
    citas.push(nuevaCita);
    localStorage.setItem('misCitas', JSON.stringify(citas));

    alert(`Â¡Cita agendada con Ã©xito!\nCliente: ${cliente}\nServicio: ${serv
${servicio}\nFecha/Hora: ${fecha} a las ${hora}`);
    
    return nuevaCita;
}

// --- Ejemplo de uso ---
const cita = agendarCita("Juan Perez", "Consulta Medica", "2023-12-25", "14
"14:00");
```

---

### Opcion 2: Python (Para logica de servidor o scripts)

Esta funcion es mas robusta y muestra como manejar errores reales, como si 
la hora ya estuviera ocupada en una base de datos.

```python
from datetime import datetime
import random

def agendar_cita(cliente, servicio, fecha_str, hora_str):
    """
    Agenda una cita validando fechas y simulando disponibilidad.
    
    Args:
        cliente (str): Nombre del cliente
        servicio (str): Tipo de servicio
        fecha_str (str): Fecha en formato 'YYYY-MM-DD'


