from conexion import Conexion
from logger_base import log
from Persona import Persona

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create, Read, Update, Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
            
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Personas insertadas: {persona}')
                return cursor.rowcount
            

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Personas actualizadas: {persona}')
                return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Personas eliminadas: {persona}')
                return cursor.rowcount
            

if __name__ == '__main__':
    # Insertar una persona
    #  persona1 = Persona(nombre='Karla', apellido='Gonzalez',email='Kgonzales@mail.com')
    #  personas_insertadas = PersonaDAO.insertar(persona1)
    #  log.debug(f'Personas insertadas: {personas_insertadas}')

    # Actualizar una persona
        # persona1 = Persona(id_persona=1, nombre='Juan Carlos', apellido='Juarez', email='jcjuarez@mail.com')
        # personas_actualizadas = PersonaDAO.actualizar(persona1)
        # log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Eliminar una persona
        persona1 = Persona(id_persona=18)
        personas_eliminadas = PersonaDAO.eliminar(persona1)
        log.debug(f'Personas eliminadas: {personas_eliminadas}')
    
    
    # Pruebas
        personas = PersonaDAO.seleccionar()
        for persona in personas:
            log.debug(persona)
