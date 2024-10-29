---
layout: page
title: Introducción a Git
nav_order: 1
---

## 1. ¿Qué es Git?

### Introducción a Git
- **Git** es un sistema de control de versiones que permite llevar un registro de los cambios realizados en el código a lo largo del tiempo.
- Es útil para **trabajar en equipo** y mantener el control de las diferentes versiones de un proyecto.

### ¿Por qué usar Git?
- Permite **deshacer errores** en el código.
- Facilita el trabajo en **colaboración**.
- **Mantiene un historial** de los cambios realizados.

### Aspectos básicos de Git

Cada vez que se guarda el trabajo, Git crea una confirmación. Una confirmación es una instantánea de todos los archivos en un momento dado. Si un archivo no ha cambiado de una confirmación a la siguiente, Git usa el archivo almacenado anteriormente.

![Linear graph of development in Git](https://learn.microsoft.com/es-es/devops/_img/linear_straight_line.png)


Las confirmaciones crean vínculos a otras confirmaciones, formando un gráfico del historial de desarrollo. Es posible revertir el código a una confirmación anterior, inspeccionar cómo cambian los archivos de una confirmación a la siguiente y revisar información como dónde y cuándo se realizaron los cambios. Las confirmaciones se identifican en Git mediante un hash criptográfico único del contenido de la confirmación. Dado que todo tiene hash, es imposible realizar cambios, perder la información o dañar los archivos sin que Git lo detecte.

### Ramas

Cada desarrollador guarda los cambios en su propio repositorio de código local. Como resultado, puede haber muchos cambios diferentes basados en la misma confirmación. Git proporciona herramientas para aislar los cambios y volver a combinarlos posteriormente. Las ramas, que son punteros ligeros para el trabajo en curso, administran esta separación. Una vez finalizado el trabajo creado en una rama, se puede combinar de nuevo en la rama principal (o troncal) del equipo.

![Commits on a branch](https://learn.microsoft.com/es-es/devops/_img/branching_line.png)

### Archivos y confirmaciones

Los archivos de Git se encuentran en uno de estos tres estados: modificados, almacenados provisionalmente o confirmados. 
Estos 3 estados corresponden con 3 secciones de un proyecto de Git: El **Directorio de Trabajo**, el **Área de Preparación** (o *área de almacenamiento*) y el **Repositorio**.

Cuando se modifica un archivo por primera vez, los cambios solo existen en el *directorio de trabajo*. Todavía no forman parte de una confirmación ni del historial de desarrollo. El desarrollador debe almacenar provisionalmente los archivos modificados que se incluirán en la confirmación. El *área de almacenamiento* provisional contiene todos los cambios que se incluirán en la siguiente confirmación. Una vez que el desarrollador esté satisfecho con los archivos almacenados provisionalmente, los archivos se empaquetan como una confirmación con un mensaje que describe lo que ha cambiado. Esta confirmación pasa a formar parte del historial de desarrollo en el *repositorio*.

![file_status_lifecycle-2](https://learn.microsoft.com/es-es/devops/_img/file_status_lifecycle.2.png)

El almacenamiento provisional permite a los desarrolladores elegir qué cambios de archivo se guardarán en una confirmación para desglosar los cambios grandes en una serie de confirmaciones más pequeñas. Al reducir el ámbito de las confirmaciones, es más fácil revisar el historial de confirmaciones para buscar cambios de archivo específicos.

---

## 2. Instalación de Git

1. **Instalación en Windows**
   - Descargar Git desde [git-scm.com](https://git-scm.com/).
   - Seguir las instrucciones del instalador y configurar opciones básicas.

2. **Instalación en Linux**
   ```bash
   sudo apt update
   sudo apt install git
   ```

3. **Instalación en macOS**
   ```bash
   brew install git
   ```

4. **Verificación de la instalación**
   ```bash
   git --version
   ```

---

## 3. Configuración Inicial de Git

1. **Configurar el nombre de usuario**
   ```bash
   git config --global user.name "Tu Nombre"
   ```

2. **Configurar el correo electrónico**
   ```bash
   git config --global user.email "tuemail@ejemplo.com"
   ```

3. **Comprobación de la configuración**
   ```bash
   git config --list
   ```

---

## 4. Comandos Básicos de Git

### Crear un repositorio
- **Crear un nuevo repositorio** en la carpeta actual:
  ```bash
  git init
  ```

### Clonar un repositorio
- **Clonar un repositorio** remoto:
  ```bash
  git clone <url-del-repositorio>
  ```

### Rastrear cambios
1. **Añadir archivos al área de preparación**:
   ```bash
   git add <archivo>  
   git add .            # Usamos este comando para añadir todos los cambios
   ```

2. **Guardar cambios (commit)**:
   ```bash
   git commit -m "Descripción breve de los cambios"
   ```

### Ignorar archivos

- Archivo .gitignore
- Plantillas de archivos .gitignore.

Las rutas y nombres de archivo que aparezcan en el fichero `.gitignore` serán ignoradas por git siempre que no hayan sido añadidas previamente al área de preparación o al repositorio. Por ejemplo, si añadimos un archivo al área de preparación mediante `git add` y a continuación lo añadimos al fichero `.gitignore`, git lo seguirá manteniendo en el área de preparación, por lo que será incluido en el repositorio si ejecutamos un `git commit`.

De igual manera, si previamente hemos guardado un archivo en el repositorio mediante `git commit` y a continuación lo incluimos en el fichero `.gitignore`, git no lo borrará: será necesario borrarlo del sistema de ficheros (a través de la consola o el navegador de archivos) y añadir los cambios (`git add` y `git commit`) para que se borre del repositorio. Una vez borrado, si lo volvemos a crear veremos que git sí que lo ignora si está incluido en el fichero `.gitignore`.

### Verificar el estado de los cambios
```bash
git status
```

Esquema de colores:
 - *Rojo* - Identifica los archivos *modificados o nuevos*. Si se crean archivos dentro de carpetas nuevas, `git status` solo mostrará el nombre de la carpeta, no su contenido. Si se desea ver el contenido de las carpetas nuevas se deberá ejecutar `git status -u`
 - *Verde* - Identifica los archivos en el *área de preparación*.

El *área de preparación* contiene los *cambios que se añadirán a la nueva versión* cuando ejecutemos un `commit`. Es posible que se pueda dar la siguiente situación:
 - Modificar un fichero (aparecerá en color rojo al hacer un `git status`)
 - Añadir el fichero al área de preparación mediante `git add FICHERO`
 - El fichero aparecerá en color *verde* al hacer un `git status`
 - Volver a modificar el fichero
 - El fichero aparecerá *dos veces* al hacer un `git status`:
   - En color *verde*, indicando que se ha añadido el *primer cambio* al área de preparación
   - En color *rojo*, indicando que hay un *segundo cambio* posterior que *no se ha incluido* en el área de preparación
 - Si se ejecuta un `git commit` en este momento *solamente se incorporará el primer cambio* al repositorio como nueva versión. El segundo cambio seguirá existiendo (el archivo no habrá cambiado), pero no estará guardado en el commit
 - Si se desea agregar el segundo cambio se deberá ejecutar nuevamente `git add` para añadirlo al área de preparación

### Ver historial de commits

Para ver el histórico de commits en el repositorio ejecutamos `git log`:
```bash
git log
git log --oneline
git log --graph
git log --oneline --all --graph --decorate
```

### Ver cambios realizados en anteriores commits
 ``` bash
 git show <commit>
 ```

 Este comando nos permite mostrar los cambios que se introdujeron en un determinado commit. En primer lugar se puede ejecutar `git log` para buscar el hash del commit que nos interese y a continuación ejecutar `git show` indicando después el hash del commit correspondiente.

 Los hash de los commits tienen 40 caracteres, pero no es necesario copiarlos enteros: basta con indicar los primeros caracteres para identificar el commit correctamente.

### Visualizar cambios
```bash
git diff
git diff <commit>
git diff <archivo_o_ruta>
```

Este es uno de los comandos más utilizados en git. Nos permite ver los cambios en los archivos del repositorio o en una ruta específica. Podemos ver también cambios entre los commits

### Quitar archivo del área de preparación
 ```bash
 git reset <archivo>
 ```

 En ocasiones nos encontramos con que hemos añadido cambios al área de preparación que no queremos incorporar al commit. Para ello podemos utilizar este comando, que elimina los cambios del fichero correspondiente del área de preparación. *Los cambios no se pierden* en ningún caso.

### Eliminar las modificaciones con respecto al último commit
 ```bash
 # ¡PELIGRO! Todos los cambios que se hayan hecho al archivo desde el último commit se eliminarán
 git checkout -- <archivo>
 ```

 Este comando es peligroso, ya que **elimina todos los cambios del archivo** que no hayan sido guardados en el repositorio. Es decir, si el archivo tiene cambios y está en color **rojo**, se perderán dichos cambios. Este comando puede ser útil para dejar un archivo tal como estaba en la última versión guardada del repositorio.

### Etiquetado
 ```bash
 git tag NOMBRE_TAG
 ```

 Este comando crea un `tag` en el commit en que nos encontremos en este momento. Un `tag` es un *alias* que se utiliza para *hacer referencia a un commit* sin necesidad de saber su hash. Normalmente se utiliza para *indicar números o nombres de versiones* asociadas a un determinado commit. De esta manera podemos *identificar una versión de una manera más amable*.

 El nombre de los `tag` se puede utilizar con los comandos de git: por ejemplo, `git show`.

---

## 5. Práctica guiada en Linux

Comenzamos instalando Git si aún no lo hemos hecho:
 ```bash
sudo apt update
sudo apt install git
```

Configuramos nuestro nombre y correo dentro de los parámetros globales de Git:

 ```bash
git config --global user.name "Nuestro Nombre"
git config --global user.email correo@edu.gva.es
```

Comenzamos ya nuestro proyecto creando un directorio de trabajo y situándonos en él:
```bash
md clasificacion
cd clasificacion
```

A continuación creamos un repositorio dentro del directorio de trabajo:
```bash
git init
```

Con un editor de texto creamos un fichero llamado `extrae.py` y copiamos en él el contenido del siguiente [programa](./extrae.py).

Comprobamos el estado de los cambios:
```bash
git status
```

Nos aparece en rojo un archivo nuevo que aún no pasado al área de preparación.

Lo pasamos al área de preparación (le indicamos que pase todos los archivos nuevos o modificados):
```bash
git add .
```

Y volvemos a comprobar el estado:
```bash
git status
```

Ahora ya nos aparece en verde, pero nos indica que debemos hacer un commit para guardarlo en el repositorio.

Realizamos el commit indicando un mensaje que nos permita identificar en qué consiste esa actualización.
```bash
git commit -m "Commit inicial"
```

Si volvemos a ejecutar un `git status` ya se nos informa que no hay ningún cambio pendiente de commit.

Vamos a modificar mediante un editor de texto el fichero `extrae.py` para eliminar la siguiente línea que aparece comentada en el código:
```python
#    print(f"Pagina: {pagina}")
```

Una vez eliminada la línea, guardamos el fichero y salimos.

Pasamos el fichero al área de preparación y realizamos un commit:
```bash
git add .
git commit -m "Eliminación línea comentada"
```

Podemos visualizar ahora el historial de cambios en el repositorio. Esto será importante de cara a poder revertir cambios y volver a situaciones anteriores.
```bash
git log
```

Ejecutemos la versión simplificada y observemos el resultado:
```bash
git log --oneline

7e78672 (HEAD -> master) Eliminación línea comentada
c6ac817 Commit inicial
```

Nos aparecen los 2 commits y nos indica que estamos situados (`HEAD`) en la rama `master` (también llamada `main`). Los números que aparecen al principio de la línea son los identificadores acortados del commit.

Podemos visualizar la diferencia entre el último commit (`HEAD`) y el primer commit (en este caso el `c6ac817`):
```bash
git diff c6ac817
```

Nos muestra en rojo la línea que hemos eliminado.

## 6. Práctica a realizar
Crea una carpeta denominada `Sesion1`. Realiza las siguientes acciones en ella:
- Crea un repositorio Git.
- Crea un fichero denominado `libros.txt`. Añade tres títulos de libros cada uno en una línea distinta.
- Haz un primer commit.
- Añade dos libros al archivo `libros.txt`.
- Haz un segundo commit.
Crea un fichero denominado `peliculas.txt`. Añade tres títulos de películas a dicho archivo.
- Haz una captura de pantalla del comando `git status`.
- Crea un fichero denominado `comidas.txt`. Añade tres nombres de comidas a dicho archivo.
- Haz un tercer commit que incluya los archivos `peliculas.txt` y `comidas.txt`.
- Elimina el archivo `comidas.txt` desde el explorador de archivos.
- Añade dos películas más al archivo `peliculas.txt`.
- Haz una captura de pantalla que muestre los cambios en el directorio de trabajo.
- Añade los cambios al área de preparación.
- Haz una captura de pantalla del comando `git status`. Debe indicar que se ha borrado el archivo `comidas.txt` y que se ha modificado el archivo `peliculas.txt`.
- Haz un cuarto commit.
- Crea un archivo denominado `datos.bak`. Añade tres títulos de libros a dicho archivo. **¡IMPORTANTE! No añadas el archivo al área de preparación ni hagas ningún commit**.
- Crea una subcarpeta denominada `output`. Crea un archivo denominado `salida.txt` en su interior. Escribe tu nombre y apellidos en dicho archivo. **¡IMPORTANTE! No añadas los archivos al área de preparación ni hagas ningún commit.**
- Haz una captura de pantalla del comando `git status`. Deben aparecer el archivo `datos.bak` y la carpeta `output` como archivos nuevos (color rojo). Recuerda que, por defecto, git no muestra el contenido de una carpeta desconocida, sino solo el nombre de dicha carpeta; si se desea mostrar los archivos nuevos dentro de carpetas desconocidas se debe ejecutar `git status -u`.
- Crea un archivo `.gitignore` para que los ficheros con extensión `.bak` y el contenido de la carpeta `output/` no se incluyan en el repositorio.
- Haz una nueva captura de pantalla del comando `git status`. Ahora no deben aparecer los archivos `datos.bak` y `output/salida.txt` como archivos nuevos, sino que en su lugar debe aparecer únicamente el archivo `.gitignore`.
- Haz un último commit para incluir el archivo `.gitignore` en el repositorio.
- Haz una captura de pantalla que muestre el histórico de cambios del repositorio.
- Muestra la diferencia entre los 2 últimos commits y captura la pantalla.