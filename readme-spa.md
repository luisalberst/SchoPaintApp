# Scho-Paint-Aplicación

> Versión v0.0.2-beta <br />
<b> Aplicación creada con fines educativos como ejercicio de software </b> <br />
<b> Actualmente disponible para el uso de la Técnica de Dibujo Libre </b>

## INICIO RÁPIDO

### Requisitos

-Python <= 3.10.9
- Kivy

#### Crear ejecutable / Android Apk

- Buildozer (Para compilación de Android)
- Pyinstaller (Para compilación de Windows)

### Instaladores (Cómo crear una aplicación propia)

#### Configurar terminal y pip

```bash
$ python -m pip install --upgrade pip setuptools virtualenv
```

#### Ambiente virtual

1. Cree el entorno virtual llamado `kivy_env` en su directorio actual:
```bash
$ python -m virtualenv kivy_venv
```
2. Activar entorno virtual (Abrir Terminal en su directorio actual):
- Ventanas (CMD)
```bash
$ kivy_venv\Scripts\activate
```
- Windows (terminal bash)
```bash
$ source kivy_venv/Scripts/Activate
```
-Linux/macOS
```bash
$ source kivy_venv/bin/Activate
```

#### Instalar Kivy

```bash
$ python -m pip install "kivy[full]" kivy_examples
```

##### Comprobar instalación

- Ventanas (CMD)
```bash
$ python kivy_venv\share\kivy-examples\demo\showcase\main.py
```
-Linux/macOS
```bash
$ python kivy_venv/share/kivy-examples/demo/showcase/main.py
```

#### Instalar Buildozer (Crear aplicación de Android)

- Con su kivy_venv activo, ejecute el siguiente comando en su ventana bash
```bash
$ clon de git https://github.com/kivy/buildozer.git
$ cd buildozer
$ sudo python setup.py install
```
- Después, navegue hasta el directorio de su proyecto y ejecute:
```bash
$ buildozer init
```
- Espere hasta la instalación y edite `buildozer.spec` con la configuración básica: `title - package.name - version (method 1)`
- Para crear su propia apk / aplicación de Android, ejecute el siguiente comando
```bash
$ buildozer -v Android debug
```
- Vaya al directorio de su proyecto, al contenedor de carpetas y busque la aplicación que genera.
- Conecte un dispositivo Android y mueva apk. Installe y ejecute.

#### Instalar Pyinstaller (Crear aplicación de Windows)

- Cree una carpeta en la que se creará la aplicación empaquetada. Por ejemplo, cree una carpeta `windows-build` y cambie a ese directorio.
```bash
$ mkdir windows-build
$ cd windows-build
```
- Luego escriba o ejecute el módulo pyinstaller con python:
```bash
$ python -m PyInstaller --name SchoPaintApp ruta\files\main.py
```
- o
```bash
$ PyInstaller --name SchoPaintApp ruta\files\main.py
```
* Donde `Path` debe ser, p. `C:/usuarios/miusuario/escritorio/files/main.py`
- También puede agregar un archivo icon.ico a la carpeta de la aplicación para crear un icono para el ejecutable.
```bash
$ python -m PyInstaller --name SchoPaintApp --icon ruta\files\icon.ico ruta\files\main.py
```
- Esperar hasta compilar el proyecto

#### Funciona con archivos .spec (Crear aplicación de Windows)

El archivo de especificaciones se ubicará en windows-build.
- Abra `SchoPaintApp.spec` y agregue al comienzo de estas líneas `from kivy_deps import sdl2, glew`
Si necesita agregar archivos adicionales, ubique `a = Analysis` dentro de este `data = []`
- Para agregar archivos adicionales a su compilación, necesita usar una tupla con parámetros `('ruta al archivo', 'ruta dentro de la compilación')`
Para agregar dependencias sdl2 y glew en compilación, necesitamos ubicar `coll = COLLECT` o `exe = EXE (si usa antes de pyinstaller --onefile)`
- En `COLLECT`, añade líneas marcadas:
```diff
    coll = COLLECT(
        exe, 
+       Tree('path\\files\\'),
        a.binaries,
        a.zipfiles,
        a.datas,
+       *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
        strip=False,
        upx=True,
        name='touchtracer'
    )
```
- En `EXE`, agregue líneas marcadas:
```diff
    exe = EXE(
        pyz,
+        Tree('path\\files\\'),
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
+        *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
        [],
        name='schopaintapp',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=True,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=['path\files\icon.ico'],
    )
```
- Guarde la edición y ejecute con python su archivo .spec
```bash
$ python -m PyInstaller SchoPaintApp.spec
```
- Al final encontrarás el ejecutable en tu carpeta `windows-build`


## Más ayuda

Para obtener más ayuda:
- [Entorno Virtual (Python)](https://virtualenv.pypa.io/en/latest/installation.html)
- [Instalación de paquetes](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Crear un paquete para Android](https://kivy.org/doc/stable/guide/packaging-android.html)
- [Crear un paquete para Windows](https://kivy.org/doc/stable/guide/packaging-windows.html)