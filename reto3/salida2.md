Aqui tienes 3 criterios de aceptacion que integran la historia de usuario y
las reglas de negocio especificas de **BienestarFET**:

1.  **Dado** que el sistema ha enviado una notificacion de recordatorio para una cita agendada, 
**cuando** se verifique que la hora actual es exactamente a las 24:00 horas antes del inicio 
programado de la sesion, **entonces** se envia al usuario un mensaje automatico solicitando confirmacion 
de asistencia.

2.  **Dado** que el usuario ha recibido la notificacion de recordatorio y desea modificar su cita debido a un inconveniente, **cuando** intente cancelar la reserva mas de 4 horas antes del inicio programado (es decir, 
entre las 17:00 y las 23:59 del dia anterior), **entonces** el sistema permite realizar la cancelacion sin costo ni penalizacion.

3.  **Dado** que el usuario ha recibido la notificacion de recordatorio y desea modificar su cita debido a un inconveniente, **cuando** intente cancelar la reserva menos de 4 horas antes del inicio programado (es decir,
decir, entre las 24:00 del d├¡a anterior y la hora de inicio), **entonces** el sistema bloquea la cancelacion y 
muestra un mensaje indicando que solo se permite cancelar hasta 4 horas antes.


