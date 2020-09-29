<h1 align="center">GitCollab</h1>
<p align="center">
  <a href="https://github.com/pythonmurcia/gitcollab/blob/master/LICENSE">
    <img alt="License: Apache 2.0" src="https://img.shields.io/hexpm/l/plug?color=gre&label=LICENSE" target="_blank"/>
  </a>
</p>

GitCollab es un proyecto open source creado por la organización de Python Murcia para el [HactoberfestES 2020](https://hacktoberfest.es.python.org/)

**La idea del proyecto es simple, que otros  programadores puedan encontrar proyectos en los que contribuir y que tu puedas encontrar contribuidores para tus proyectos.**

##### GitCollab tiene un grupo de Telegram al que te puedes unir para hablar con otras personas que participen en este proyecto. Únete [aqui](https://t.me/gitcollab)
---

### Como contribuir
El Hacktoberfest busca que todo el mundo pueda contribuir a los proyectos, que tu nivel de experiencia no limite los proyectos en los que puedas participar. Por eso desde Python Murcia queremos hacer todo lo más sencillo posible.

**Hemos organizado el proyecto en issues**, a su vez, los issues están clasificados por tags. **Solo puedes contribuir a los issues con el tag "ayuda"** cada issue con el tag ayuda contiene en el título una breve descripcion de la tarea y un número, que va del 1 al 5. Los issues marcados como "1" son los más sencillos, prácticamente todo el mundo puede contribuir en ellos, mientras que los issues marcados con un "5" son los más complejos o difíciles de implementar. 

En cada uno de estos issues encontrarás una descripción detallada de el task del issue, enlaces que te podrían servir, requisitos, la fecha de entrega (si es que la hay)...

Cuando decidas empezar un issue, deja un comentario explicando que tienes pensado hacer en el thread del issue. Cuando un moderador lo apruebe, se te asignará el issue y se le agregrará la etiqueta de "en curso", lo que significa que nadie más puede contribuir a ese issue hasta que tu lo finalices.

#### Proyecto de GitHub
En [el proyecto "issues" de GitCollab](https://github.com/pythonmurcia/gitcollab/projects/1) hay una representación gráfica con targetas de todos los issues **Un administrador o moderador se encarga de actualizar el proyecto cada hora**.

| Columna   | Descripción                                                                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Esperando | Estos issues no pueden ser asignados aún ya que para poder trabajar en ellos hay que finalizar otros issues, especificados dentro del mismo issue.|
| Por hacer | Los issues en la columna  de "por hacer" pueden ser assignados a contribuidores de GitCollab, puedes pedir que te asignen cualquiera de estos issues para trabajar con él. |                                                               
| En progreso |No puedes trabajar en estos issues ya que otras personas ya están trabajando en ellos, están marcados con el tag "en curso"                      |
| Finalizados - Por revisar | Estos issues ya han sido finalizados y las personas que trabajaran en ellos han creado un pull request, ahora un administrador o moderador de la organización tiene que revisar el trabajo que has hecho antes de hacer merge |
| Finalizados - revisados | Estos issues han sido revisados por un moderador y administrados. Ya están finalizados. |
| Cerrados | Estos issues han sido mergeados con el proyecto después de ser revisados por un administrador, pueden ser reabiertos si un administrador lo considera necesario. |

Cuando se te haya asignado uno de los issues para que trabajes en el, deberás seguir los pasos para trabajar en un repositorio remoto. Es decir:
* Haz un fork del repositorio en GitHub. Haces esto para adquirir permisos de push y poder contribuir en el código.
* Clona el fork del repositorio en tu pc para poder trabajar con el desde local. 
* Crea un branch en el fork del repositorio con el nombre del issue, trabajarás bajo esa rama. Por ejemplo, si estoy trabajando en un issue llamado "crear-login-db" el branch de git se debería llamar igual
* Realiza los cambios necesarios para completar tu issue. Intenta tocar el menor numero de archivos posibles para evitar merge errors. Puedes crear subramas dentro de la rama de tu issue. 
* Conforme trabajes en el fork del proyecto, guarda tu progreso en el stage area con commits. 
* Pushea el código con los comandos `git remote -v`y `git push` para crear una rama remota.
* Ya deberías de poder crear el Pull Request en el repositorio. A la hora de crear la pull  request haz click en la casilla de "permitir commits a los administradores del proyecto"

##### Cuando hayas conseguido que un administrador cierre tu issue, añaderemos tu nombre a la tabla del archivo [contributors.md](https://github.com/pythonmurcia/gitcollab/blob/master/colaborators.md), junto con el numero de issues en los que has participado

---
### Licencia

GitCollab es un proyecto de código abierto que opera bajo la licencia Apache 2.0, que puedes leer en el archivo [LICENSE](https://github.com/pythonmurcia/gitcollab/blob/master/LICENSE) del repositorio.
```
Copyright 2020 Python Murcia

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
---

###### Recuerda seguirnos en [Twitter](https://twitter.com/pythonmurcia) y unirte a [nuestro grupo de Telegram](https://t.me/pythonmurcia)
