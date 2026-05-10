#-------------------------------------------------------
# BASE DE DATOS 2
# GRUPO: 5
# INTEGRANTES: Mateo Tipán, Luis Vasquez, Martín Ochoa
# NRC: 5480
#-------------------------------------------------------

# --FUNCION PARA MOSTRAR LAS OPCIONES CRUD-------------------------------------------------------
def mostrar_opciones_crud():
    print("\t****************************")  
    print("\t** SISTEMA CRUD UDEMYTEST **")  
    print("\t****************************")  
    print("\tOpciones CRUD:\n")
    print("\t1. Crear registro")
    print("\t2. Consultar registros")
    print("\t3. Actualizar registro")
    print("\t4. Eliminar registro")
    print("\t5. Salir\n\n")

# --FUNCION PARA INSERTAR REGISTROS DE CURSOS-----------------------------------------------------
def insertar_registros(conexion):

    micursor = conexion.cursor()

    SENTENCIA_SQL = """
    INSERT INTO Cursos
    (IDCurso,NombreCurso,Descripcion,PrecioxHora,TipoCurso)
    VALUES(?,?,?,?,?)
    """
    print("\n\t\tINSERTAR NUEVO CURSO:\n")  
    
     ## Ingreso de Informacion
    l_IDCurso = int(input("Ingrese ID del Curso: \t"))
    l_NombreCurso = input("Ingrese Nombre del Curso: \t")
    l_Descripcion = input("Ingrese la Descripcion:\t")
    l_PrecioxHora = input("Ingrese el Precio por Hora \t")
    l_TipoCurso= input("Ingrese Tipo de Curso:\t")   
         
    micursor.execute( SENTENCIA_SQL,(l_IDCurso,l_NombreCurso,l_Descripcion,l_PrecioxHora,l_TipoCurso))
       
    micursor.commit()
    print("\nOk ... Insercion Exitosa: \n")        

# --FUNCION PARA CONSULTAR LOS REGISTROS DE CURSOS-----------------------------------------------------  
def consultar_registros(conexion):
     #Crear Cursor
    micursor = conexion.cursor()
    # 1. Ejemplo: Consulta la tabla "Estudiantes”
    SENTENCIA_SQL = """
        SELECT IDCurso,NombreCurso,Descripcion,
        PrecioxHora,TipoCurso FROM Cursos
    """ 
    micursor.execute(SENTENCIA_SQL)
    
    rows = micursor.fetchall()
    for row in rows:
        print(f"{row.IDCurso}\t{row.NombreCurso}\t{row.Descripcion}\t{row.PrecioxHora}\t{row.TipoCurso}")
    
    print("\nOk ... Proceso Culminado con Exito: \n")


# --FUNCION PARA ACTUALIZAR LOS REGISTROS DE CURSOS-----------------------------------------------------  
def actualizar_registros(conexion):

    micursor = conexion.cursor()
    
    SENTENCIA_SQL = """UPDATE Cursos
    SET PrecioxHora = ?
    WHERE IDCurso= ?"""
    
    ## Ingreso de Informacion
    print("\n\t Actualizar Informacion Cursos:\n")
    l_IDCurso = int(input("Ingrese ID del Curso: \t"))
    l_PrecioxHora = input("Ingrese Nuevo Precio por Hora: \t")
    micursor.execute( SENTENCIA_SQL,(l_PrecioxHora ,l_IDCurso ))
    
    micursor.commit()
    print("\nOk ... Actualización Exitosa. \n")   

# --FUNCION PARA ELIMINAR LOS REGISTROS DE CURSOS-----------------------------------------------------  
def eliminar_registros(conexion):

    micursor = conexion.cursor()
    
    SENTENCIA_SQL = """DELETE FROM Cursos
    WHERE IDCurso=?"""
    
    ## Ingreso de Informacion
    print("\n\t Eliminar Registro Curso:\n")
    l_IDCurso = int(input("Ingrese ID del Curso a Elimnar: \t"))
    
    micursor.execute( SENTENCIA_SQL,(l_IDCurso))
    micursor.commit()   
    print("Ok ... Eliminacion Exitosa. \n")


### Inicio  Programa principal ########
# 1. Importar Biblioteca de conexión
import pyodbc
# 2. Declarar variables de Conexión
name_server ='MSI'
database ='UDEMYTEST1'
username ='pythonconsultor'
password = 'UDLA'
controlador_odbc='SQL Server'

# 3. Crear Cadena de Conexion.
connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

#4. Establece la conexión
try:
    conexion = pyodbc.connect(connection_string) 
except Exception as e:
    print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)    
# Fin Conexion de BDD
else: 
    while True:
        mostrar_opciones_crud()
        opcion = input("Seleccione una opción 1-5:\t")
        
        if opcion == '1':
            insertar_registros(conexion)
        elif opcion == '2':
            consultar_registros(conexion)
        elif opcion == '3':
            actualizar_registros(conexion)
        elif opcion == '4':
            eliminar_registros(conexion)
        elif opcion == '5':
            print("Saliendo del programa..\n\n.")
            break
        else:
            print("Opción no válida.")   
            break     
    
finally:
    print("Conexion Cerrada: \n")
