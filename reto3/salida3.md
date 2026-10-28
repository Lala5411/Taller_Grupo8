| Caso | Entrada | Resultado esperado | Criterio que cubre |
| :--- | :--- | :--- | :--- |

|**Caso 1**|
|Un estudiante tiene una cita confirmada para mañana y el sistema ejecuta la notificacion diaria.|
|Se envia un recordatorio al estudiante indicando la hora y el servicio de la cita.|
|Criterio 1|

|**Caso 2**| 
|Un estudiante recibe el recordatorio y decide cancelar la cita con m├ís de 4 horas de anticipacion.|
|El sistema libera el cupo disponible y cancela la cita sin generar un registro de inasistencia.| 
|Criterio 2|

| **Caso 3**| 
|Un estudiante recibe el recordatorio pero no asiste a la cita y no ha realizado la cancelacion a tiempo.| 
|Se contabiliza una inasistencia para el estudiante en su historial.| 
|Criterio 3|

*Nota de auto-verificacion: Todos los criterios (1, 2 y 3) provistos en la 
seccion `<criterios>` han sido cubiertos por al menos un caso de prueba en 
la tabla.*


