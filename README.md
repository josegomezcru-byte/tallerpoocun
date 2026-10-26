# Sistema de Gestión TI y Académica - CUN 🎓

Este proyecto es la solución al Taller Práctico Integrador de la Corporación Unificada Nacional de Educación Superior (CUN). Permite la gestión de estudiantes, docentes y tickets de soporte técnico mediante una arquitectura basada en Programación Orientada a Objetos (POO) y una base de datos relacional SQLite.

## 🚀 Características
- **POO Avanzada:** Implementación de Clases, Herencia (clase base `Persona`), Encapsulamiento (modificadores de acceso privados y `@property`) y Composición.
- **Base de Datos:** Integración con `SQLite3` nativo de Python (`cun_sistema.db`).
- **Consultas Relacionales:** Uso de `JOIN` para asociar los tickets de soporte con los estudiantes registrados.

## 📂 Estructura del Proyecto
- `main.py`: Contiene toda la lógica del modelo de clases (POO) y las funciones de conexión e inserción a la base de datos.
- `cun_sistema.db`: Archivo generado automáticamente al ejecutar el script, contiene las tablas `estudiantes`, `docentes` y `tickets_soporte`.
- `README.md`: Documentación del proyecto.

## 🛠️ Cómo ejecutar el proyecto

1. Asegúrate de tener **Python 3.x** instalado en tu sistema.
2. Clona este repositorio:
   ```bash
   git clone <URL-DE-TU-REPOSITORIO>