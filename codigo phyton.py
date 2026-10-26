import sqlite3

# ==========================================
# 1. MODELO DE CLASES (POO)
# ==========================================

# Clase Base (Herencia)
class Persona:
    def __init__(self, identificacion, nombre):
        self.__identificacion = identificacion  # Encapsulamiento
        self.__nombre = nombre

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def nombre(self):
        return self.__nombre

# Clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, identificacion, nombre, programa, promedio=0.0):
        super().__init__(identificacion, nombre)
        self.__programa = programa
        self.__promedio = promedio

    @property
    def programa(self):
        return self.__programa

    @property
    def promedio(self):
        return self.__promedio

# Clase Docente que hereda de Persona
class Docente(Persona):
    def __init__(self, identificacion, nombre, departamento):
        super().__init__(identificacion, nombre)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

# Clase Ticket de Soporte TI
class TicketSoporte:
    def __init__(self, id_estudiante, categoria, descripcion, estado="ABIERTO"):
        self.__id_estudiante = id_estudiante
        self.__categoria = categoria
        self.__descripcion = descripcion
        self.__estado = estado

    @property
    def id_estudiante(self):
        return self.__id_estudiante

    @property
    def categoria(self):
        return self.__categoria

    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def estado(self):
        return self.__estado

# ==========================================
# 2. LOGICA DE BASE DE DATOS (SQLite)
# ==========================================

def crear_base_datos_cun():
    """Crea la base de datos y las tablas necesarias"""
    conn = sqlite3.connect('cun_sistema.db')
    cursor = conn.cursor()
    
    # Tabla Estudiantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id_estudiante TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            programa TEXT NOT NULL,
            promedio REAL DEFAULT 0.0
        )
    ''')
    
    # Tabla Docentes (Para cumplir con la gestión de docentes)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS docentes (
            id_docente TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            departamento TEXT NOT NULL
        )
    ''')
    
    # Tabla Tickets de Soporte TI
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets_soporte (
            id_ticket INTEGER PRIMARY KEY AUTOINCREMENT,
            id_estudiante TEXT NOT NULL,
            categoria TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            estado TEXT DEFAULT 'ABIERTO',
            FOREIGN KEY (id_estudiante) REFERENCES estudiantes (id_estudiante)
        )
    ''')
    conn.commit()
    conn.close()
    print("[Exitoso] Base de datos 'cun_sistema.db' creada correctamente.")

def registrar_estudiante(estudiante: Estudiante):
    """Inserta un objeto Estudiante en la BD"""
    conn = sqlite3.connect('cun_sistema.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)", 
                       (estudiante.identificacion, estudiante.nombre, estudiante.programa, estudiante.promedio))
        conn.commit()
        print(f"[Exitoso] Estudiante {estudiante.nombre} registrado.")
    except sqlite3.IntegrityError:
        print(f"[Error] El estudiante con ID {estudiante.identificacion} ya existe.")
    finally:
        conn.close()

def crear_ticket(ticket: TicketSoporte):
    """Inserta un objeto TicketSoporte en la BD"""
    conn = sqlite3.connect('cun_sistema.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickets_soporte (id_estudiante, categoria, descripcion, estado) VALUES (?, ?, ?, ?)", 
                   (ticket.id_estudiante, ticket.categoria, ticket.descripcion, ticket.estado))
    conn.commit()
    print(f"[Exitoso] Ticket creado para el estudiante ID: {ticket.id_estudiante}.")
    conn.close()

def consultar_tickets():
    """Realiza un JOIN para mostrar los tickets junto al nombre del estudiante"""
    conn = sqlite3.connect('cun_sistema.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT t.id_ticket, e.nombre, t.categoria, t.descripcion, t.estado 
        FROM tickets_soporte t
        JOIN estudiantes e ON t.id_estudiante = e.id_estudiante
    ''')
    registros = cursor.fetchall()
    print("\n--- TICKETS DE SOPORTE CUN ---")
    for r in registros:
        print(f"Ticket #{r[0]} | Estudiante: {r[1]} | Categoría: {r[2]} | Estado: {r[4]}\nDetalle: {r[3]}\n")
    conn.close()

# ==========================================
# 3. EJECUCIÓN DEL PROGRAMA
# ==========================================
if __name__ == '__main__':
    # 1. Crear BD
    crear_base_datos_cun()
    
    # 2. Instanciar objetos (POO)
    est1 = Estudiante("1001", "Ana Gomez", "Ingeniería de Sistemas", 4.2)
    est2 = Estudiante("1002", "Carlos Ruiz", "Administración", 3.8)
    doc1 = Docente("2001", "Prof. Luis Pérez", "Ciencias Básicas")
    
    # 3. Registrar en BD
    registrar_estudiante(est1)
    registrar_estudiante(est2)
    
    # 4. Crear Tickets
    ticket1 = TicketSoporte(est1.identificacion, "Hardware", "El computador del aula 301 no enciende.")
    ticket2 = TicketSoporte(est2.identificacion, "Software", "Problemas de acceso a la plataforma virtual.")
    
    crear_ticket(ticket1)
    crear_ticket(ticket2)
    
    # 5. Consultar e imprimir
    consultar_tickets()