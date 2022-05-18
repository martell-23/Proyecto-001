Proyecto de desarrollo basado en plataformas  

















Docente: 


Integrantes:
                                       -Hósmer Gilberto Casma Morales
                                       -Sergio Marcelo Ricce Abregú
                                       -Hans Alfonso Mendoza Alva
                                       -Giancarlos Martell.l




















• Un README.md en el repositorio que incluya:
– Nombre del proyecto.
– Integrantes.
– Descripción del proyecto.
– Objetivos principales / Misión / Visión.
– Información acerca de las librerías/frameworks/plugins utilizadas
en Front-end, Back-end y Base de datos.
– El nombre del script a ejecutar para iniciar la base de datos con
datos.
– Información acerca de los API. Requests y Responses de cada
endpoint utilizado en el sistema.
– Hosts.
– Forma de autenticación.
– Manejo de errores HTTP:
500 : Errores en el Servidor
400 : Errores en el Cliente
300 : Redirección
200 : Exitoso
100 : Informacional
– Cómo ejecutar el sistema (Deployment scripts).
• Revisa bien lo que entregas, después de la fecha de entrega no podrás
hacer modificaciones.

















Estacionamiento Utec

Integrantes
-Hósmer Gilberto Casma Morales
-Sergio Marcelo Ricce Abregú
-Hans Alfonso Mendoza Alva
-Giancarlos Martell.l


Introducción 

El proyecto (Estacionamiento Utec) se basa en una plataforma virtual que permite a los trabajadores registrar en una base de datos a los usuarios del servicio de estacionamiento Utec, mediante su placa de auto y nombre del propietario del auto al momento de ingresar. Además el sistema registra automáticamente la hora de ingreso del vehículo .

Objetivo principal
Nuestro objetivo es brindar un sistema de registro eficaz y de simple accesibilidad para que los trabajadores del estacionamiento Utec puedan registrar de manera simple a los usuarios y sus vehículos que usan el servicio. 



 
Recursos empleados

-Librerías :  
datetime
flask_sqlalchemy
flask_migrate
flask
-Framework :
Django
Flash
Psql


API
-/Login 
request : username , password .
return : render_template('login.html')

-/OP1
Return : render_template('op1.html')


-/Create/Formulario
request : name , placa .
response : formulario.id , name , placa , date 
return : jsonify(response)

-/Create/<formulario_id>/delete
query : fomulario_id
return : return jsonify({'success': success })


 Hosts

http://127.0.0.1:5000

Forma de autenticación

El login usa de forma universal un único usuario y contraseña para que el trabajador pueda ingresar al sistema de estacionamiento, siendo estos “Pogbvam” y “Ut3c” respectivamente. En caso se introdusca mal la contraseña, se le mandará un mensaje de error al usuario indicando de que alguno de los dos datos esté incorrecto y se le pedirá que lo intente nuevamente 

Manejo de errores
200: Se a aceptado el request exitosamente
302: Recurso solicitado ha sido movido temporalmente a la URL




Ejecución del sistema 

Al momento de que el usuario ingrese al dominio, llegará a la página principal en donde tendrá la opción de ir a login para poder iniciar sesión y así tener acceso a la función principal del sistema, que es el registro de autos del Estacionamiento Utec 

 
  
