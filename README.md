# Proyecto-001
Estacionamiento Utec

Introducción  

El proyecto (Estacionamiento Utec) se basa en una plataforma virtual que permite a los trabajadores registrar en una base de datos a los usuarios del servicio de estacionamiento Utec, mediante su placa de auto y nombre del propietario del auto al momento de ingresar. Además el sistema registra automáticamente la hora de ingreso y salida  del vehículo .

Objetivo principal

Facilitar la forma en la que los empleados y el dueño del servicio estacionamiento utec puedan registrar  más fácilmente a los clientes

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
 
  
