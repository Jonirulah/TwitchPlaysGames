# TwitchPlaysGames
TwitchPlaysGames "easy" to use for everyone is a project which aims to provide an easy environment for all kind of users to get their TwitchPlays in their streams in almost no-time without even programming. Also no need to install Python, no need to install Node.js, no need to install libraries if you are using the executable file on releases.<br><br>
![image](https://user-images.githubusercontent.com/25936173/119594928-fb35e480-bddc-11eb-822a-ad43fac394e0.png)

This is version-1, failures may occur.<br>
At this moment version-1 is chat-broken in the exe file, so you need Python in order to execute it and install a lot of libraries, after compiling it's complaining about a missing library that it's not missing, so at this moment you need the source code in order to get it right.

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
```yaml
twitch-bot:
    - oauth: "oauth:1234"
    - channel: "jonirulah"
```
You need to get your oauth at https://twitchapps.com/tmi/ and change the channel to yours and place it on the oauth parameter.
    

# You can add ROMS to TwitchPlaysGames
Just place the file at Documents/TwitchPlays-Storage/Roms and restart the software, it will automatically detect the ROM for you.

# You can add more configs to TwitchPlaysGames 
Just create a new file at Documents/TwitchPlays-Storage/Configs and add your config example:
```yaml
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
   ```yaml
Visual Boy Advance:
    - name: Emulator TEST (GBA)
    - version: v0.0
    - url: https://github.com/visualboyadvance-m/visualboyadvance-m/releases/download/v2.1.4/visualboyadvance-m-Win-32bit.zip<br>
    - exec_file: visualboyadvance.exe<br>
  ```
# TwitchPlaysGames
TwitchPlaysGames "f??cil" de usar para todo el mundo es un proyecto el cual aspira a crear un entorno de f??cil uso para todo tipo de usuarios para tener en su stream su TwitchPlays en muy poco tiempo sin tener conocimientos de programaci??n. No hay necesidad de instalar Python, ni instalar Node.js, ni librer??as, siempre que no estes usando el c??digo fuente tal cual.

# ES<br>
TwitchPlaysGames es una aplicaci??n creada unicamente en Python la cual incluye su propio servidor web en el cual puedes obtener informaci??n en tiempo real en tu Overlay de OBS.<br><br>
TwitchPlaysGames tiene como intenci??n una manera de poder crear tus propios TwitchPlays sin ser un maestro programando, el programa descargar?? el emulador por t?? (siempre que el enlace est?? funcionando) y en la carpeta Documents/TwitchPlays-Storage/Configs encontrar??s un fichero de configuraci??n el cual puedes usar como plantilla para el juego que quieras.<br><br> Lo ??nico que tendr??s que hacer una vez te bajes el ejecutable es crear tu fichero de configuraci??n y darle al bot??n "Launch" o "Iniciar" si tienes el lenguaje en espa??ol.<br><br> El programa se conectar?? de forma autom??tica al Chat de Twitch del canal que indiques y empezar?? a obtener los comandos para procesarlos.

TwitchPlaysGames is an application made entirely in Python which includes it's own webserver so you can get info in realtime in your OBS overlay.<br><br>
TwitchPlaysGames attempts for a very easy to use method the own software will try to download the emulator for you and in your Documents/TwitchPlays-Storage/Configs you will find a sample config and you can create your own for every game.<br><br> You only will need to press the button "Launch" and the software will execute the emulator for you, will connect to the Twitch Chat and start getting commands to process them.<br><br>

# Instrucciones:
- Ves al fichero settings.yaml en la misma carpeta que el ejecutable y ver??s estas 3 l??neas en el fichero.<br>
```yaml
twitch-bot:
    - oauth: "oauth:1234"
    - channel: "jonirulah"
```
Necesitas obtener tu token de autentificaci??n en https://twitchapps.com/tmi/ y ponerlo en el par??metro oauth, tambi??n debes cambiar el canal por el tuyo.
    

# Puedes a??adir ROMS a TwitchPlaysGames
Simplemente mete el archivo en la carpeta Documents/TwitchPlays-Storage/Roms y reinicia el programa, autom??ticamente detectar?? la ROM por ti.

# Puedes a??adir m??s ficheros de configuraci??n a TwitchPlaysGames 
Simplemente crea un fichero en Documents/TwitchPlays-Storage/Configs ya a??ade tu configuraci??n, aqu?? tienes un ejemplo.
```yaml
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
Puedes a??adir teclas para ser pulsadas al mismo tiempo o teeclas que ser??n presionadas de forma secuencial durante el press-time que indiques.<br>
Puedes usar "single-tap" o "maintain", "maintain" siempre requerir?? el uso de un press-time ya que es necesario para mantener la tecla el tiempo indicado, y luego est?? el modo "single-tap", "single-tap" har?? un toque a la tecla a la m??xima velocidad posible, es posible que la velocidad sea tan alta que ni el emulador reconozca el input, en ese caso es recomendable que cambies el modo "single-tap" a "maintain" con un press-time muy bajo.

# Puedes a??adir mas emuladores a TwitchPlaysGames
  Debes acceder al fichero settings.yaml y a??adir una nueva entrada, aqu?? tienes un ejemplo:<br>
   ```yaml
Visual Boy Advance:
    - name: Emulador TEST (GBA)
    - version: v0.0
    - url: https://github.com/visualboyadvance-m/visualboyadvance-m/releases/download/v2.1.4/visualboyadvance-m-Win-32bit.zip<br>
    - exec_file: visualboyadvance.exe<br>
  ```
