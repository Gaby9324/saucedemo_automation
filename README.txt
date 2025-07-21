1. INSTALACIÓN:
   - Python 3.8+ y pip instalados.
   - Ejecutar: pip install -r requirements.txt
   - Tener Chrome/Firefox instalado.

2. EJECUCIÓN:
   - Ejecutar el test: pytest c:/Users/USER/Documents/GitHub/saucedemo_automation/tests/test_flujo_compra.py -v --html=reports/report.html

3. CONFIGURACIÓN:
   - Editar credenciales en conftest.py si es necesario.
   - Ajustar waits en test_flujo_compra.py según velocidad de red.