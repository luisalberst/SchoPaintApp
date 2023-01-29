# Scho-Paint-App

> Version v0.0.2-beta <br />
<br />
<b>Application created for educational purposes as a software exercise</b>

## QUICKSTART

### Requeriments

- Python <= 3.10.9
- Kivy

#### Create Executable / Android Apk

- Buildozer (For Android build)
- Pyinstaller (For Windows build)

### Installers (How to create own app)

#### Setup terminal and pip

```bash
$ python -m pip install --upgrade pip setuptools virtualenv
```

#### Virtual environment

1. Create the virtual environment named `kivy_env` in ur current directory:
```bash
$ python -m virtualenv kivy_venv
```
2. Activate virtual environment (Open Terminal on ur current directory):
- Windows (CMD)
```bash
$ kivy_venv\Scripts\activate
```
- Windows (bash terminal)
```bash
$ source kivy_venv/Scripts/activate
```
- Linux / macOS
```bash
$ source kivy_venv/bin/activate
```

#### Install Kivy

```bash
$ python -m pip install "kivy[full]" kivy_examples
```

##### Check Install

- Windows (CMD)
```bash
$ python kivy_venv\share\kivy-examples\demo\showcase\main.py
```
- Linux / macOS
```bash
$ python kivy_venv/share/kivy-examples/demo/showcase/main.py
```

#### Install Buildozer (Create Android App)

- With your kivy_venv active, execute the next command on your bash window
```bash
$ git clone https://github.com/kivy/buildozer.git
$ cd buildozer
$ sudo python setup.py install
```
- After, navigate to your project directory and run:
```bash
$ buildozer init
```
- Wait until install, and edit `buildozer.spec` with basic config: `title - package.name - version (method 1)`
- To create your own apk / app android, run next command
```bash
$ buildozer -v android debug
```
- Go to your project directory, folder bin and search you generate app.
- Plug an android device and move apk.

#### Install Pyinstaller (Create Windows App)

- Create a folder into which the packaged app will be created. For example create a `windows-build` folder and change to that directory.
```bash
$ mkdir windows-build
$ cd windows-build
```
- Then type or execute the module pyinstaller with python: 
```bash
$ python -m PyInstaller --name SchoPaintApp path\files\main.py
```
- or 
```bash
$ PyInstaller --name SchoPaintApp path\files\main.py
```
* Where `Path` must be, e.g. `C:/users/myuser/desktop/files/main/py`
- You can also add an icon.ico file to the application folder in order to create an icon for the executable.
```bash
$ python -m PyInstaller --name SchoPaintApp --icon path\files\icon.ico path\files\main.py
```
- Wait until compile the project

#### Works with .spec files (Create Windows App)

The spec file will be locate on windows-build. 
- Open the `SchoPaintApp.spec` and add to beginning these lines `from kivy_deps import sdl2, glew`
If u need add aditionals files, `locate a = Analysis` inside this `data = []`
- To add adicionals files to your build, need use a tuple with parameters `('path to file', 'path inside build')`
To add dependencies sdl2 and glew on build, we need locate `coll = COLLECT` or `exe = EXE (if you use before pyinstaller --onefile)`
- On `COLLECT`, add marked lines:
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
- On `EXE`, add marked lines:
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
- Save edit, and execute with python your .spec file
```bash
$ python -m PyInstaller SchoPaintApp.spec
```
- At the end you will find the executable on your `windows-build` folder


## Further help

To get more help:
- [VirtualEnv](https://virtualenv.pypa.io/en/latest/installation.html)
- [Installing Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Create a Package for Android](https://kivy.org/doc/stable/guide/packaging-android.html)
- [Create a Package for Windows](https://kivy.org/doc/stable/guide/packaging-windows.html)