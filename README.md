# TwitchPlaysGames
TwitchPlaysGames "easy" to use for everyone is a project which aims to provide an easy environment for all kind of users to get their TwitchPlays in their streams in almost no-time without even programming. Also no need to install Python, no need to install Node.js, no need to install libraries if you are using the executable file on releases.
![image](https://user-images.githubusercontent.com/25936173/119594928-fb35e480-bddc-11eb-822a-ad43fac394e0.png)

This is version-1, failures may occur.

Information for OBS overlay, Browser sources at:
- http://127.0.0.1:8877/currentmode [current_mode] # Democracy or Anarchy
- http://127.0.0.1:8877/counter [time-after-pressing-start-emulator] # Countup
- http://127.0.0.1:8877/currentapm [current_apm] # Actions x minute
- http://127.0.0.1:8877/currentmode_stats [current_stats] # [Anarchy,Democracy]

# EN<br>
TwitchPlaysGames is an application made entirely in Python which includes it's own webserver so you can get info in realtime in your OBS overlay.<br><br>
TwitchPlaysGames attempts for a very easy to use method the own software will try to download the emulator for you and in your Documents/TwitchPlays-Storage/Configs you will find a sample config and you can create your own for every game.<br><br> You only will need to press the button "Launch" and the software will execute the emulator for you, will connect to the Twitch Chat and start getting commands to process them.<br><br>

# Instructions:
- Go to the settings.yaml file on the same folder as the executable file, and you will see this stuff<br>
- You can go to the settings.yaml file and change your language to 'en' English or 'es' Spanish.
```
twitch-bot:
    - oauth: "oauth:1234"
    - channel: "jonirulah"
```
You need to get your oauth at https://twitchapps.com/tmi/ and change the channel to yours and place it on the oauth parameter.
    

# You can add ROMS to TwitchPlaysGames
Just place the file at Documents/TwitchPlays-Storage/Roms and restart the software, it will automatically detect the ROM for you.

# You can add more configs to TwitchPlaysGames 
Just create a new file at Documents/TwitchPlays-Storage/Configs and add your config example:
```
name: Configuration for Pokemon RED (GBA)
author: Jonirulah

commands:
  a:
    key-press-type: maintain
    keys-order: sametime
    press-time: 0.1
    keys-to-press:
      key: L
    
  b:
    key-press-type: maintain
    keys-order: sequential
    press-time: 0.1    
    keys-to-press:
      key: K

  up:
    key-press-type: single-tap
    keys-order: sequential
    keys-to-press:
      key: W

  right:
    key-press-type: single-tap
    keys-order: sametime
    keys-to-press:
      key: D
```
You can add keys to get pressed at the same time or keys to get pressed sequentially within the press-time<br>
You can use "single-tap" or "maintain", "maintain" will always need a press-time since it is needed to maintain the time you need, and "single-tap" will do a single-tap at the maximum speed possible, if your emulator doesn't recognise the movement it's probably because it's way too fast and you should use maintain with a very low press-time.

# You can add more emulators to TwitchPlaysGames
  You just need to get to the settings.yaml file and add your own entry example<br>
   ```
Visual Boy Advance:
    - name: Emulator TEST (GBA)
    - version: v0.0
    - url: https://github.com/visualboyadvance-m/visualboyadvance-m/releases/download/v2.1.4/visualboyadvance-m-Win-32bit.zip<br>
    - exec_file: visualboyadvance.exe<br>
  ```
# TwitchPlaysGames
TwitchPlaysGames "fácil" de usar para todo el mundo es un proyecto el cual aspira a crear un entorno de fácil uso para todo tipo de usuarios para tener en su stream su TwitchPlays en muy poco tiempo sin tener conocimientos de programación. No hay necesidad de instalar Python, ni instalar Node.js, ni librerías, siempre que no estes usando el código fuente tal cual.

# ES<br>
TwitchPlaysGames es una aplicación creada unicamente en Python la cual incluye su propio servidor web en el cual puedes obtener información en tiempo real en tu Overlay de OBS.<br><br>
TwitchPlaysGames tiene como intención una manera de poder crear tus propios TwitchPlays sin ser un maestro programando, el programa descargará el emulador por tí (siempre que el enlace esté funcionando) y en la carpeta Documents/TwitchPlays-Storage/Configs encontrarás un fichero de configuración el cual puedes usar como plantilla para el juego que quieras.<br><br> Lo único que tendrás que hacer una vez te bajes el ejecutable es crear tu fichero de configuración y darle al botón "Launch" o "Iniciar" si tienes el lenguaje en español.<br><br> El programa se conectará de forma automática al Chat de Twitch del canal que indiques y empezará a obtener los comandos para procesarlos.

TwitchPlaysGames is an application made entirely in Python which includes it's own webserver so you can get info in realtime in your OBS overlay.<br><br>
TwitchPlaysGames attempts for a very easy to use method the own software will try to download the emulator for you and in your Documents/TwitchPlays-Storage/Configs you will find a sample config and you can create your own for every game.<br><br> You only will need to press the button "Launch" and the software will execute the emulator for you, will connect to the Twitch Chat and start getting commands to process them.<br><br>

# Instrucciones:
- Ves al fichero settings.yaml en la misma carpeta que el ejecutable y verás estas 3 líneas en el fichero.<br>
```
twitch-bot:
    - oauth: "oauth:1234"
    - channel: "jonirulah"
```
Necesitas obtener tu token de autentificación en https://twitchapps.com/tmi/ y ponerlo en el parámetro oauth, también debes cambiar el canal por el tuyo.
    

# Puedes añadir ROMS a TwitchPlaysGames
Simplemente mete el archivo en la carpeta Documents/TwitchPlays-Storage/Roms y reinicia el programa, automáticamente detectará la ROM por ti.

# Puedes añadir más ficheros de configuración a TwitchPlaysGames 
Simplemente crea un fichero en Documents/TwitchPlays-Storage/Configs ya añade tu configuración, aquí tienes un ejemplo.
```
name: Configuration for Pokemon RED (GBA)
author: Jonirulah

commands:
  a:
    key-press-type: maintain
    keys-order: sametime
    press-time: 0.1
    keys-to-press:
      key: L
    
  b:
    key-press-type: maintain
    keys-order: sequential
    press-time: 0.1    
    keys-to-press:
      key: K

  up:
    key-press-type: single-tap
    keys-order: sequential
    keys-to-press:
      key: W

  right:
    key-press-type: single-tap
    keys-order: sametime
    keys-to-press:
      key: D
```
Puedes añadir teclas para ser pulsadas al mismo tiempo o teeclas que serán presionadas de forma secuencial durante el press-time que indiques.<br>
Puedes usar "single-tap" o "maintain", "maintain" siempre requerirá el uso de un press-time ya que es necesario para mantener la tecla el tiempo indicado, y luego está el modo "single-tap", "single-tap" hará un toque a la tecla a la máxima velocidad posible, es posible que la velocidad sea tan alta que ni el emulador reconozca el input, en ese caso es recomendable que cambies el modo "single-tap" a "maintain" con un press-time muy bajo.

# Puedes añadir mas emuladores a TwitchPlaysGames
  Debes acceder al fichero settings.yaml y añadir una nueva entrada, aquí tienes un ejemplo:<br>
   ```
Visual Boy Advance:
    - name: Emulador TEST (GBA)
    - version: v0.0
    - url: https://github.com/visualboyadvance-m/visualboyadvance-m/releases/download/v2.1.4/visualboyadvance-m-Win-32bit.zip<br>
    - exec_file: visualboyadvance.exe<br>
  ```
