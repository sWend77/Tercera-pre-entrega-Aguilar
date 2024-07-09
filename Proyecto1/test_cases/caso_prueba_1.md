# Caso de Prueba 1: Registro de Usuario

## Descripción
Este caso de prueba verifica que el proceso de registro de un nuevo usuario funcione correctamente.

## Pasos
1. Navegar a la página de registro.
2. Llenar el formulario de registro con los siguientes datos:
    - Nombre: tsunami
    - Correo electrónico: susi@hotmail.com
    - Contraseña: asd123
3. Hacer clic en el botón "Registrarse".

## Resultados Esperados
- El sistema debe mostrar un mensaje de éxito indicando que el registro se completó correctamente.
- El usuario debe ser redirigido a la página de inicio de sesión.

## Resultados Obtenidos
- El usuario se registro correctamente, pero no se mostro el mensaje de exito en el inicio.

## Estado
- Fallido

## Solucion
- El error fue causado por mala sintaxis a la hora de pasar el contexto al template. Luego de corregirlo, se renderizo correctamente.