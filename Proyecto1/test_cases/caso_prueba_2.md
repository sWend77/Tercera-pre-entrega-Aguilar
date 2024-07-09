# Caso de Prueba 2: Busqueda en formulario de mercado

## Descripción
Este caso de prueba verifica que el proceso de busqueda de instrumentos en el formulario de la seccion 'mercado', funcione correctamente.

## Pasos
1. Navegar a la página de mercado.
2. Seleccionar que tipo de accion desea realizar(compra,venta).
3. Escribir el tipo de instrumento, opcionalmente especificando su marca o modelo en el formulario.
    - Busqueda: "Guitarra fender". 
4. Realizar la busqueda.

## Resultados Esperados
- El resultado debe mostrar exitosamente todas las publicaciones creadas en el template 'resultado_busqueda_instrumentos.html'
- El usuario debe poder interactuar y ver las caracteristicas principales de los instrumentos.

## Resultados Obtenidos
- Error de tipo: ("ValueError" at /app-include/resultado-busqueda-instrumentos/)

## Estado
- Fallido

## Solucion
- El error fue causado por una falla en el orden y el acomodo de los filtros en la view 'buscar_instrumentos'. Una vez ordenados, se pudo realizar la busqueda sin problemas.