Alumno: ANdry Yair Aquino callejas
Num Control:23230768
Maestro:Kevin David Molina Gomez
materia:estructura de datos

# Menú Dinámico Flask

![Muestra de página principal](img/principal.png)

Esta aplicación muestra un menú de navegación dinámico y responsivo usando Flask y Bootstrap. El menú se genera a partir de un diccionario anidado en Python y se renderiza recursivamente en la plantilla HTML con Jinja2. Solo la página principal está implementada y los submenús se despliegan usando Bootstrap, sin JavaScript personalizado.

## ¿Cómo funciona?
- El menú se define como un diccionario anidado en `main.py`.
- Una macro recursiva en la plantilla `menu.html` genera el menú y sus submenús.
- Bootstrap (por CDN) da el estilo responsivo y visualmente atractivo.
- Solo la ruta principal (`/`) está implementada; los enlaces del menú no llevan a otras páginas.

![Muestra de desglose y pantalla completa](img/desglose.png)

## ¿Cómo ejecutarlo?
1. Instala Flask si no lo tienes:
   ```bash
   pip install flask
   ```
2. Ejecuta la aplicación:
   ```bash
   python main.py
   ```
3. Abre tu navegador en:
   ```
   http://localhost:5000
   ```

¡Listo! Así puedes ver y probar el menú dinámico. 