```python
from datetime import datetime, timedelta
from typing import Tuple, Optional

def puede_agendar_cita(
    estudiante_id: str,
    servicio: str,
    fecha_hora_inicio: datetime,
    inasistencias_semestre: int = 0,
    bloqueos_activos: bool = False,
    cita_activa_actual: Optional[datetime] = None
) -> Tuple[bool, str]:
    """
    Valida si un estudiante cumple los requisitos para agendar una cita en 
el sistema BienestarFET.

    Reglas de validacion aplicadas:
    1. Horario: Lunes a viernes, 08:00 - 17:00, bloques de 30 minutos.
    2. Maximo una cita activa por servicio para cada estudiante.
    3. Anticipacion minima de 24 horas.
    4. Cancelacion permitida hasta 4 horas antes (no aplica al agendar
nuevo, pero implica logica de disponibilidad).
    5. Dos inasistencias bloquean el agendamiento por 30 dias.

    Args:
        estudiante_id (str): Identificador unico del estudiante.
        servicio (str): Tipo de servicio (Atencion, Deportes, Orientacion).
        fecha_hora_inicio (datetime): Fecha y hora tentativa para la cita.
        inasistencias_semestre (int): Numero de inasistencias registradas en el semestre actual.
        bloqueos_activos (bool): Indica si existe un bloqueo activo por inasistencia previa.
        cita_activa_actual (Optional[datetime]): Fecha y hora de una cita ya agendada para este estudiante y servicio.

    Returns:
        Tuple[bool, str]: Retorna (es_valido, motivo) donde es_valido es booleano y motivo es la razon de validacion o error.
    """
    
    # Regla 1: Validar horario (Lunes a Viernes, 08:00 - 17:00)
    dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    dia_actual = fecha_hora_inicio.strftime('%A').lower()
    
    if dia_actual not in dias_semana:
        return False, f"El d├¡a {dia_actual} no esta disponible. Solo se atiende de lunes a viernes."
    
    hora_inicio = fecha_hora_inicio.hour
    hora_fin = 17
    
    # Verificar si la hora de inicio esta dentro del rango permitido (08:00 - 17:00)
    if hora_inicio < 8 or hora_inicio >= 17:
        return False, f"La hora {hora_inicio}:00 est├í fuera del horario de atencion (08:00 - 17:00)."
    
    # Verificar si la hora coincide con bloques de 30 minutos
    if hora_inicio % 30 != 0:
        return False, f"La hora {hora_inicio}:00 no es un bloque validado de 30 minutos."

    # Regla 2: Maximo una cita activa por servicio
    if cita_activa_actual is


