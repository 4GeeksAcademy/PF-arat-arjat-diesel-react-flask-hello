from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'
    
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # El password va a ser encriptado, creo que son mas de 100 caracteres
    password = db.Column(db.String(500), nullable=False)    
    rol = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.email}>'

    def serialize(self):
        return {
            # do not serialize the password, its a security breach
            "id": self.id,
            "nombre": self.nombre, 
            "email": self.email,
            "rol": self.rol,
        }

# Las variables no llevan tildes o ñ
# todas las clases deben llevar repr y serialize
class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_producto = db.Column(db.String(100), nullable=False)
    VIN_matricula = db.Column(db.String(100), nullable=False)
    transporte = db.Column(db.String(100), nullable=False)
    empresa_institucion = db.Column(db.String(100), nullable=False)
    nombre_chofer_propietario = db.Column(db.String(100), nullable=False)       # Esta registrado como usuario el chofer ?
    telefono = db.Column(db.String(100), nullable=False)                        # Con 20 caracteres estaria ok
    kilometraje_inicial = db.Column(db.Float, nullable=False)
    # fallas = db.Column(db.String(200), nullable=False)                          # Cuales serian las fallas?, va en reparacio 
    capture_DTC = db.Column(db.String(100), nullable=False)
   # solucion = db.Column(db.String(200), nullable=False)                          # va en reparacion
    # tecnico_id = db.Column(db.Integer)                                          # el tecnico seria un usuario registrado?
                                                                                # El tecnico tiene que estar en reparacion
    #técnico = db.relationship('Usuario', backref='vehiculos')
    # fecha_ingreso = db.Column(db.Date, nullable=False)                        # va en reparacion
    # fecha_salida = db.Column(db.Date)                                         # va en reparacion
    # costo_reparacion = db.Column(db.Float)                                    # va en reparacion

class Reparacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer)                                         #Clave foranea de vehiculo
    #vehículo = db.relationship('Vehiculo', backref='reparaciones')
    fecha_ingreso = db.Column(db.Date, nullable=False)                          #Agregar
    fecha_reparacion = db.Column(db.Date, nullable=False)
    # fecha_salida = db.Column(db.Date)                                         # Agregar
    costo_reparacion = db.Column(db.Float, nullable=False)
    monto_cancelado_cliente = db.Column(db.Float)                               #No entiendo, puede pagar en forma parcial?
   # monto_cancelado_tecnico = db.Column(db.Float)                                 # se calcula con el porcentaje
    porcentaje_ganancia_tecnico = db.Column(db.Float)                           
    porcentaje_ganancia_empresa = db.Column(db.Float)
    check_list_pago = db.Column(db.Boolean)                                     # Que es esto?

class Reporte(db.Model):                                                    #Para que es esto?
    id = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer)
   # vehículo = db.relationship('Vehiculo', backref='reportes')
    fecha_reporte = db.Column(db.Date, nullable=False)
    contenido_reporte = db.Column(db.String(500), nullable=False)

# Agregar todos las funciones repr y serialize, fijate en usuario que te hice un ejemplo
# Agregar las clases en admin.py, en la linea 4 y luego igual que la 14, para que lo puedas ver en el modelado