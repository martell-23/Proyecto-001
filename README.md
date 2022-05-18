__Proyecto de desarrollo basado en plataformas__

__Docente:__ Marvin Abisrror Zarate

__Estacionamiento Utec__

__Integrantes:__

Hósmer Gilberto Casma Morales.

Sergio Marcelo Ricce Abregú.

Hans Alfonso Mendoza Alva.

Giancarlos Martell.



__Introducción__

El proyecto (Estacionamiento Utec) se basa en una plataforma virtual que permite a los trabajadores registrar en una base de datos a los usuarios del servicio de estacionamiento Utec, mediante su placa de auto y nombre del propietario del auto al momento de ingresar. Además el sistema registra automáticamente la hora de ingreso del vehículo .

__Objetivo principal__

Nuestro objetivo es brindar un sistema de registro eficaz y de simple accesibilidad para que los trabajadores del estacionamiento Utec puedan registrar de manera simple a los usuarios y sus vehículos que usan el servicio. 



 
__Recursos empleados__

__Librerías :__

datetime

flask_sqlalchemy

flask_migrate

flask

__Framework :__

Flask

Psql


__API__

__/Login:__

request : username, password.

return : render_template('login.html')

__/OP1__

Return : render_template('op1.html')


___/Create/Formulario___

request : name , placa.

response : formulario.id , name , placa , date.

return : jsonify(response)

___/Create/<formulario_id>/delete___

query : fomulario_id

return : jsonify({'success': success })


___Hosts___

http://127.0.0.1:5000

localhost:5432

___Forma de autenticación___

El login usa de forma universal un único usuario y contraseña para que el trabajador pueda ingresar al sistema de estacionamiento, siendo estos “Pogbvam” y “Ut3c” respectivamente. En caso se introdusca mal la contraseña, se le mandará un mensaje de error al usuario indicando de que alguno de los dos datos esté incorrecto y se le pedirá que lo intente nuevamente 

___Manejo de errores___

200: Se a aceptado el request exitosamente

302: Recurso solicitado ha sido movido temporalmente a la URL




__Ejecución del sistema__

Al momento de que el usuario ingrese al dominio, llegará a la página principal en donde tendrá la opción de ir a login para poder iniciar sesión y así tener acceso a la función principal del sistema, que es el registro de autos del Estacionamiento Utec 
