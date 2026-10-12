# Laboratorio 2 — Desarrollo de Aplicaciones Empresariales

Proyecto académico con Python y Django para practicar el flujo solicitud-respuesta,
las vistas, el contexto y la renderización de plantillas. El proyecto se llama
`lab02` y contiene la aplicación `encuesta`, con tres funcionalidades:

- **Encuesta:** recibe los datos de un formulario y los muestra en otra página,
  incluyendo varios idiomas seleccionados.
- **Operaciones matemáticas:** suma, resta o multiplica dos números, incluidos
  negativos y decimales, y muestra el resultado.
- **Volumen de un cilindro:** recibe altura y diámetro en metros y calcula
  `V = π × (diámetro / 2)² × altura`, utilizando `math.pi`.

Los formularios usan POST y protección CSRF. Los cálculos validan sus entradas.
La contraseña de la encuesta es solo una demostración académica: utiliza datos
ficticios. No se almacena; aparece en la página de respuesta.

## Ejecutar en Windows con CMD

Requisitos: Git y Python **3.14.8**, con el lanzador `py` disponible.
Django **5.2.18** admite Python 3.14; también admite Python 3.12, utilizado en
las pruebas de Linux de este proyecto.

1. Abre una ventana nueva de **CMD**, sin activar el entorno de `todoproject`.
   Comprueba la versión de Python:

   ```bat
   py -3.14 --version
   ```

   Debe indicar `Python 3.14.8`. Si no coincide, comprueba la instalación antes
   de continuar. Si no tienes el lanzador `py`, usa la ruta completa al
   `python.exe` de Python 3.14.8 para crear el entorno en el paso 3.

2. Clona este repositorio en una carpeta independiente:

   ```bat
   if not exist D:\ProyectosDjango mkdir D:\ProyectosDjango
   cd /d D:\ProyectosDjango
   git clone https://github.com/mmachacac/L2-Django-Sem2.git
   cd L2-Django-Sem2
   ```

   Si ya lo clonaste, entra en `D:\ProyectosDjango\L2-Django-Sem2` y omite
   `git clone`. Estos pasos no modifican `todoproject` ni su entorno virtual.

3. Crea el entorno virtual propio del laboratorio:

   ```bat
   py -3.14 -m venv .venv
   ```

   El entorno queda en `D:\ProyectosDjango\L2-Django-Sem2\.venv`. No copies
   un entorno virtual de Linux ni reutilices el de otro proyecto.

4. Instala las dependencias y comprueba las versiones:

   ```bat
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   .venv\Scripts\python.exe --version
   .venv\Scripts\python.exe -m django --version
   .venv\Scripts\python.exe -m pip check
   ```

   Las versiones esperadas son Python `3.14.8` y Django `5.2.18`.
   Usamos el intérprete explícito del entorno; no es necesario activarlo.

5. Entra en la carpeta que contiene `manage.py`, comprueba la configuración
   e inicia el servidor:

   ```bat
   cd lab02
   ..\.venv\Scripts\python.exe manage.py check
   ..\.venv\Scripts\python.exe manage.py runserver 8080
   ```

   `check` debe terminar sin problemas. Mantén CMD abierto mientras utilizas
   el servidor. Para detenerlo, pulsa **Ctrl+C**.

   Django puede advertir que hay migraciones pendientes de sus aplicaciones
   estándar. Los tres ejercicios no necesitan guardar datos en la base.
   Si deseas inicializar esa base local, detén el servidor y ejecuta:

   ```bat
   ..\.venv\Scripts\python.exe manage.py migrate
   ```

   Esto crea o actualiza `lab02\db.sqlite3`, excluido de Git. Después puedes
   volver a ejecutar `runserver 8080`.

## Direcciones de acceso

Con el servidor ejecutándose, abre en el navegador de tu computadora:

| Formulario | Dirección |
| --- | --- |
| Encuesta | `http://127.0.0.1:8080/encuesta/` |
| Operaciones matemáticas | `http://127.0.0.1:8080/encuesta/operaciones/` |
| Volumen de un cilindro | `http://127.0.0.1:8080/encuesta/cilindro/` |

Envía los formularios mediante sus botones. Acceder directamente por GET a las
rutas de envío o cálculo devuelve HTTP 405, porque requieren POST. Un POST sin
token CSRF válido devuelve HTTP 403. Los cálculos con entradas inválidas muestran
un mensaje y devuelven HTTP 400. Para los decimales utiliza punto; altura y
diámetro deben ser mayores que cero.

## Ejecutar en Linux

Utiliza Python 3.12 o 3.14 compatible con Django 5.2.18 y con soporte para `venv`.
Desde una carpeta de proyectos, en un entorno independiente:

```bash
git clone https://github.com/mmachacac/L2-Django-Sem2.git
cd L2-Django-Sem2
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python --version
.venv/bin/python -m django --version
.venv/bin/python -m pip check
cd lab02
../.venv/bin/python manage.py check
../.venv/bin/python manage.py runserver 8080
```

Si el repositorio y su `.venv` ya están preparados, utiliza los existentes.
Las direcciones son las mismas que en Windows. Detén el servidor con **Ctrl+C**.
Para inicializar opcionalmente la base estándar, desde la carpeta de `manage.py`:

```bash
../.venv/bin/python manage.py migrate
```

## Archivos locales y disponibilidad

`requirements.txt` fija `Django==5.2.18`. `.gitignore` excluye `.venv` y otros
nombres habituales de entornos virtuales, cachés y temporales de Python,
archivos `.env`, archivos habituales de credenciales y la base SQLite local.
No introduzcas credenciales reales en el código ni en archivos para versionar.
El servidor y la configuración generada son para desarrollo local.

Para ejecutar desde un clon de GitHub, los archivos de implementación deben
haber sido publicados. Mientras solo existan localmente en Codex, un clon no
los incluirá. Las instrucciones de Windows están preparadas para ejecutarse
allí; las pruebas realizadas hasta ahora corresponden a Linux.
