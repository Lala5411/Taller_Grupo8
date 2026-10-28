### REPORTE DE REVISION
- **Estado**: INCORRECTO
- **Reglas Violadas**: R1, R2, R3, R5
- **Accion requerida**: 
  - Implementar validacion de horarios (L-V 08:00 a 17:00) y bloques de 30 minutos.
  - Verificar si el estudiante ya tiene una cita activa antes de permitir nueva agendamiento.
  - Corregir la logica de anticipacion para requerir >= 24 horas en lugar de < 12 horas.
  - Corregir la condicion de inasistencias para bloquear a partir de >= 2 en lugar de > 2.



