# Automatización de MonkeyType con Selenium

Proyecto usando **Selenium** y páginas web en tiempo real (MonkeyType). El sistema automatiza la entrada de texto simulando el comportamiento de un usuario y gestionando los cambios dinámicos en la estructura del sitio.

---

## Funcionamiento Técnico

El programa utiliza **Python** y la librería **Selenium** para interactuar con el navegador. La lógica se basa en la identificación constante de elementos activos dentro del **DOM (Document Object Model)** para evitar interrupciones durante la ejecución.

---

## Características principales

- **Interacción con Input Oculto:** El envío de caracteres se realiza directamente al elemento `#wordsInput`, que es el componente encargado de procesar la entrada de texto en la plataforma.
- **Latencia Variable:** Implementación de pausas aleatorias entre pulsaciones de teclas para evitar una cadencia mecánica uniforme.
- **Gestión de Referencias Dinámicas:** Localización del elemento `.word.active` en cada iteración del ciclo para prevenir errores de punteros nulos o caducos.

---

## Instalación y Configuración

### Clonar repositorio
```bash
$ git clone https://github.com/tu-usuario/monkeytype-bot.git
$ cd monkeytype-bot
```
### Entorno 
```bash
$ python -m venv venv
$ source venv/Scripts/activate
```
### Dependencias
```bash
$ pip install -r requirements.txt
```
### Ejecutar
```bash
$ python main.py
```
