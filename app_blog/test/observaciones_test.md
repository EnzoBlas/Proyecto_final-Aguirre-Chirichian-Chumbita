##Por si la plantilla de excel no se puede ver. (Efectivamente, no se pudo cargar)

Nombre del Proyecto	Proyecto_final-Aguirre-Chirichian-Chumbita/app_blog		
Navegador:	Google Chrome		
No. Caso de Prueba	#1		
Version:	103.0.5060.53 (Build oficial) (64 bits)		
Escrito por	Enzo Chumbita, Fabrizio Chirichian, Fabiola Aguirre		
Descripción:	Bitácora de pequeñas pruebas Unit tests para verificar el funcionamiento del proyecto		
Probado por	Fabiola Aguirre 		
Probado en:	Windows		
						
						
Prueba1	fecha:27-06-2022	
accion:Cargar la página de inicio --- //home.html	
Resultado_Esperado: Redirigir a la página de inicio 	
Resultado_Actual: La página de inicio carga correctmente	
Estado: Aprobado	
Test: ViewsTestCase en test_vista_paginas.py

Prueba2	fecha:27-06-2022	
accion: Cargar la página de publicaciones --- //post_list.html
Resultado_Esperado: Ir a la página de publicaciones 	
Resultado_Actual: Se redireccionó correctamente a la página de publicaciones	
Estado: Aprobado	
Test: ViewsTestCase en test_vista_paginas.py

Prueba3	fecha:27-06-2022	
accion: Cargar la página de mensajes del perfil de usuario--- //message_list.html
Resultado_Esperado: Ir a la págna de mensajes	
Resultado_Actual: La página de mensajes respondió correctamente	
Estado: Aprobado	
Test: ViewsTestCase en test_vista_paginas.py

Prueba4	fecha:27-06-2022	
accion: Escribir un título con multiples caracteres
Resultado_Esperado: Un titulo con caracteres random	
Resultado_Actual: El título del post tuvo 20 caracteres random
Estado: Aprobado	
Test: test_post_caracteres.py
