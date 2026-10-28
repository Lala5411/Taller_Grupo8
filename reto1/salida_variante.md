```python
from datetime import datetime, timedelta
from typing import Tuple, Optional

def puede_agendar_cita(
    estudiante_id: int,
    servicio: str,
    fecha_hora_desired: datetime,
    inasistencias_semestre: int = 0,
    bloqueos_activos: list[datetime] = None,
    citas_activas: dict[str, datetime] = None
) -> Tuple[bool, str]:
    """
    Valida si un estudiante cumple los requisitos para agendar una cita en 
el sistema BienestarFET.

    Parametros:
        estudiante_id (int): Identificador unico del estudiante.
        servicio (str): Tipo de servicio solicitado (ej. 'atencion', 'deportes', 'orientacion').
        fecha_hora_desired (datetime): Fecha y hora deseada para la cita.
        inasistencias_semestre (int): Numero de inasistencias registradas en el semestre actual.
        bloqueos_activos (list[datetime]): Lista de fechas hasta las cuales el estudiante esta bloqueado por inasistencia.
        citas_activas (dict[str, datetime]): Diccionario mapeando servicio a la fecha/hora de la cita activa actual.

    Reglas validadas:
        1. Horario v├ílido: Lunes a viernes, entre 08:00 y 17:00, en bloques de 30 minutos.
        2. Maximo una cita activa por servicio.
        3. Anticipacion minima de 24 horas.
        4. Cancelacion permitida hasta 4 horas antes (no aplica para agendar nueva, pero se considera si existe cita previa).
        5. Bloqueo por inasistencia: Si hay >= 2 inasistencias y la fecha deseada esta dentro del periodo de bloqueo (30 dias), es invalido.

    Retorno:
        Tuple[bool, str]: 
            - bool: Indica si el agendamiento es valido.
            - str: Motivo detallado si no es valido; mensaje vacio si es valido.

    Ejemplo:
        >>> puede_agendar_cita(123, 'atencion', datetime.now() + timedelta(days=1, hours=5))
        (True, '')
        >>> puede_agendar_cita(123, 'atencion', datetime.now())
        (False, 'La cita debe agendarse con al menos 24 horas de anticipacion.')
    """
    # Regla 1: Horario valido (Lunes a viernes, 08:00 - 17:00, bloques de 30 min)
    dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    dia_semana = fecha_hora_desired.weekday()
    
    if dia_semana < 0 or dia_semana > 4:
        return False, f"El servicio solo se ofrece de lunes a viernes (dia actual: {dias_semana[dia_semana]})"
    
    hora = fecha_hora_desired.hour
    minuto = fecha_hora_desired.minute
    
    # Verificar rango horario


