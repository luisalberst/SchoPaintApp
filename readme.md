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
1. Create the virtual environment named kivy_env in ur current directory:
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
- Wait until install, and edit `buildozer.spec` with basic config: title - package.name - version (method 1)
- To create your own apk / app android, run next command
```bash
$ buildozer -v android debug
```
- Go to your project directory, folder bin and search you generate app.
- Plug an android device and move apk.