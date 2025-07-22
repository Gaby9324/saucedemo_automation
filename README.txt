INSTRUCCIONES PARA EJECUTAR LAS PRUEBAS:

1. Requisitos previos:
   - Java JDK 8 o superior instalado
   - Maven instalado
   - Variables de entorno JAVA_HOME y MAVEN_HOME configuradas

2. Clonar o descomprimir el proyecto

3. Ejecutar las pruebas:
   - Abrir terminal en la raíz del proyecto
   - Ejecutar el comando: mvn test

4. Ver reportes:
   - Después de la ejecución, los reportes estarán disponibles en:
     target/karate-reports/karate-summary.html
   - Abrir este archivo en un navegador web

5. Estructura de pruebas:
   - Las pruebas se encuentran en: src/test/resources/features/user_management.feature


6. Configuración:
   - La URL base está configurada en karate-config.js
   - Los headers por defecto se configuran en el Background del feature

