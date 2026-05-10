
-- CREACION DE LOGIN-USER PARA LA BASE DE DATOS UDEMYTEST-TABLA CURSOS

-- 1. Crear Login
USE MASTER
GO
CREATE LOGIN [pythonconsultor] WITH PASSWORD='UDLA',
DEFAULT_DATABASE=UDEMYTEST1
GO
-- 2. Conceder permiso de Conexion
use [master]
GO
GRANT CONNECT SQL TO [pythonconsultor]
GO
-- 3. Asignar o Crear Usuario de Base de Datos
USE UDEMYTEST1
GO
CREATE USER pythonconsultor FOR LOGIN pythonconsultor
GO
-- 4. Conceder permisor a usuario de BDD Por cada Tabla de la BDD
GRANT SELECT ON Cursos TO pythonconsultor
GO
GRANT INSERT,UPDATE,DELETE ON Cursos TO pythonconsultor
GO
-- 4.1 Condeder todos los Permisos de lectura y escritura -- para todos los objetos de la BDD
ALTER ROLE db_datareader ADD MEMBER pythonconsultor
GO
ALTER ROLE db_datawriter ADD MEMBER pythonconsultor
GO

