import os
import django
from datetime import date
from decimal import Decimal

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sweettooth.settings')  # Cambia "sweettooth" por el nombre de tu proyecto
django.setup()

# Importar el modelo Pago
from pagos.models import Pago

# Crear pagos para los pacientes
# Paciente 1: Juan Pérez
pago1 = Pago(
    id_servicio=1,
    id_paciente=1,
    nombre_paciente='Juan Pérez',
    tipo_tratamiento='Consulta general',
    descripcion_tratamiento='Revisión médica de rutina',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 4, 30),
    monto_pago=Decimal('500.00'),
    metodo_pago='Tarjeta',
    estado_pago='pendiente',
)
pago1.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago1.nombre_paciente}")

pago2 = Pago(
    id_servicio=1,
    id_paciente=1,
    nombre_paciente='Juan Pérez',
    tipo_tratamiento='Tratamiento dental',
    descripcion_tratamiento='Limpieza dental',
    especialista_responsable='Dr. Martínez',
    fecha_pago=date(2025, 5, 2),
    monto_pago=Decimal('400.00'),
    metodo_pago='Transferencia',
    estado_pago='pendiente',
)
pago2.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago2.nombre_paciente}")

pago3 = Pago(
    id_servicio=1,
    id_paciente=1,
    nombre_paciente='Juan Pérez',
    tipo_tratamiento='Chequeo cardiovascular',
    descripcion_tratamiento='Chequeo general de corazón',
    especialista_responsable='Dr. Martínez',
    fecha_pago=date(2025, 5, 10),
    monto_pago=Decimal('600.00'),
    metodo_pago='PayPal',
    estado_pago='pendiente',
)
pago3.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago3.nombre_paciente}")

pago4 = Pago(
    id_servicio=1,
    id_paciente=1,
    nombre_paciente='Juan Pérez',
    tipo_tratamiento='Revisión oftalmológica',
    descripcion_tratamiento='Chequeo de vista',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 5, 15),
    monto_pago=Decimal('200.00'),
    metodo_pago='Tarjeta',
    estado_pago='pendiente',
)
pago4.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago4.nombre_paciente}")

# Paciente 2: Ana Martínez
pago5 = Pago(
    id_servicio=2,
    id_paciente=2,
    nombre_paciente='Ana Martínez',
    tipo_tratamiento='Tratamiento dental',
    descripcion_tratamiento='Limpieza dental',
    especialista_responsable='Dr. García',
    fecha_pago=date(2025, 5, 5),
    monto_pago=Decimal('800.00'),
    metodo_pago='PayPal',
    estado_pago='pendiente',
)
pago5.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago5.nombre_paciente}")

pago6 = Pago(
    id_servicio=2,
    id_paciente=2,
    nombre_paciente='Ana Martínez',
    tipo_tratamiento='Consulta general',
    descripcion_tratamiento='Chequeo general de salud',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 5, 8),
    monto_pago=Decimal('500.00'),
    metodo_pago='Tarjeta',
    estado_pago='pendiente',
)
pago6.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago6.nombre_paciente}")

pago7 = Pago(
    id_servicio=2,
    id_paciente=2,
    nombre_paciente='Ana Martínez',
    tipo_tratamiento='Chequeo cardiovascular',
    descripcion_tratamiento='Revisión de corazón',
    especialista_responsable='Dr. García',
    fecha_pago=date(2025, 5, 12),
    monto_pago=Decimal('700.00'),
    metodo_pago='Transferencia',
    estado_pago='pendiente',
)
pago7.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago7.nombre_paciente}")

pago8 = Pago(
    id_servicio=2,
    id_paciente=2,
    nombre_paciente='Ana Martínez',
    tipo_tratamiento='Revisión oftalmológica',
    descripcion_tratamiento='Chequeo de vista',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 5, 20),
    monto_pago=Decimal('250.00'),
    metodo_pago='PayPal',
    estado_pago='pendiente',
)
pago8.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago8.nombre_paciente}")

# Paciente 3: Carlos Ruiz
pago9 = Pago(
    id_servicio=3,
    id_paciente=3,
    nombre_paciente='Carlos Ruiz',
    tipo_tratamiento='Chequeo cardiovascular',
    descripcion_tratamiento='Chequeo general de corazón y presión arterial',
    especialista_responsable='Dr. Martínez',
    fecha_pago=date(2025, 6, 1),
    monto_pago=Decimal('1000.00'),
    metodo_pago='Transferencia',
    estado_pago='pendiente',
)
pago9.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago9.nombre_paciente}")

pago10 = Pago(
    id_servicio=3,
    id_paciente=3,
    nombre_paciente='Carlos Ruiz',
    tipo_tratamiento='Revisión general',
    descripcion_tratamiento='Revisión médica de rutina',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 6, 3),
    monto_pago=Decimal('450.00'),
    metodo_pago='Tarjeta',
    estado_pago='pendiente',
)
pago10.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago10.nombre_paciente}")

pago11 = Pago(
    id_servicio=3,
    id_paciente=3,
    nombre_paciente='Carlos Ruiz',
    tipo_tratamiento='Consulta dental',
    descripcion_tratamiento='Limpieza dental',
    especialista_responsable='Dr. García',
    fecha_pago=date(2025, 6, 5),
    monto_pago=Decimal('650.00'),
    metodo_pago='PayPal',
    estado_pago='pendiente',
)
pago11.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago11.nombre_paciente}")

pago12 = Pago(
    id_servicio=3,
    id_paciente=3,
    nombre_paciente='Carlos Ruiz',
    tipo_tratamiento='Revisión oftalmológica',
    descripcion_tratamiento='Chequeo de vista',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 6, 10),
    monto_pago=Decimal('350.00'),
    metodo_pago='Transferencia',
    estado_pago='pendiente',
)
pago12.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago12.nombre_paciente}")

# Paciente 4: Sofía González
pago13 = Pago(
    id_servicio=4,
    id_paciente=4,
    nombre_paciente='Sofía González',
    tipo_tratamiento='Consulta oftalmológica',
    descripcion_tratamiento='Revisión de vista y prescripción de gafas',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 5, 10),
    monto_pago=Decimal('200.00'),
    metodo_pago='Tarjeta',
    estado_pago='pendiente',
)
pago13.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago13.nombre_paciente}")

pago14 = Pago(
    id_servicio=4,
    id_paciente=4,
    nombre_paciente='Sofía González',
    tipo_tratamiento='Consulta general',
    descripcion_tratamiento='Chequeo de salud',
    especialista_responsable='Dr. García',
    fecha_pago=date(2025, 5, 12),
    monto_pago=Decimal('400.00'),
    metodo_pago='PayPal',
    estado_pago='pendiente',
)
pago14.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago14.nombre_paciente}")

pago15 = Pago(
    id_servicio=4,
    id_paciente=4,
    nombre_paciente='Sofía González',
    tipo_tratamiento='Chequeo cardiovascular',
    descripcion_tratamiento='Chequeo de corazón',
    especialista_responsable='Dr. Martínez',
    fecha_pago=date(2025, 5, 15),
    monto_pago=Decimal('600.00'),
    metodo_pago='Transferencia',
    estado_pago='pendiente',
)
pago15.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago15.nombre_paciente}")

pago16 = Pago(
    id_servicio=4,
    id_paciente=4,
    nombre_paciente='Sofía González',
    tipo_tratamiento='Revisión oftalmológica',
    descripcion_tratamiento='Chequeo de vista',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 5, 20),
    monto_pago=Decimal('250.00'),
    metodo_pago='PayPal',
    estado_pago='pendiente',
)
pago16.save()  # Guardar el pago
print(f"⚡ Creando pago para {pago16.nombre_paciente}")

# Medicamento para Juan Pérez
pago17 = Pago(
    id_servicio=1,
    id_paciente=1,
    nombre_paciente='Juan Pérez',
    tipo_tratamiento='Medicamento',
    descripcion_tratamiento='Ibuprofeno 400mg - Caja de 10 tabletas',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 5, 25),
    monto_pago=Decimal('150.00'),
    metodo_pago='Efectivo',
    estado_pago='pendiente',
)
pago17.save()
print(f"💊 Creando pago de medicamento para {pago17.nombre_paciente}")

# Medicamento para Ana Martínez
pago18 = Pago(
    id_servicio=2,
    id_paciente=2,
    nombre_paciente='Ana Martínez',
    tipo_tratamiento='Medicamento',
    descripcion_tratamiento='Amoxicilina 500mg - Tratamiento de 10 días',
    especialista_responsable='Dra. Martínez',
    fecha_pago=date(2025, 5, 26),
    monto_pago=Decimal('250.00'),
    metodo_pago='Transferencia',
    estado_pago='pendiente',
)
pago18.save()
print(f"💊 Creando pago de medicamento para {pago18.nombre_paciente}")

# Medicamento para Carlos Ruiz
pago19 = Pago(
    id_servicio=3,
    id_paciente=3,
    nombre_paciente='Carlos Ruiz',
    tipo_tratamiento='Medicamento',
    descripcion_tratamiento='Enalapril 10mg - Control de presión arterial',
    especialista_responsable='Dr. García',
    fecha_pago=date(2025, 6, 12),
    monto_pago=Decimal('180.00'),
    metodo_pago='Tarjeta',
    estado_pago='pendiente',
)
pago19.save()
print(f"💊 Creando pago de medicamento para {pago19.nombre_paciente}")

# Medicamento para Sofía González
pago20 = Pago(
    id_servicio=4,
    id_paciente=4,
    nombre_paciente='Sofía González',
    tipo_tratamiento='Medicamento',
    descripcion_tratamiento='Lágrimas artificiales - Gotas oculares',
    especialista_responsable='Dr. López',
    fecha_pago=date(2025, 5, 22),
    monto_pago=Decimal('120.00'),
    metodo_pago='Efectivo',
    estado_pago='pendiente',
)
pago20.save()
print(f"💊 Creando pago de medicamento para {pago20.nombre_paciente}")
