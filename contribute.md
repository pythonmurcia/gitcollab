## Contribuir a GitCollab
El Hacktoberfest busca que todo el mundo pueda contribuir a los proyectos, que tu nivel de experiencia no limite los proyectos en los que puedas participar. Por eso desde Python Murcia queremos hacer todo lo más sencillo posible.

**Hemos organizado GitCollab en issues**, a su vez, los issues están clasificados por tags. **Solo puedes contribuir a los issues con el tag "ayuda"** cada issue con el tag ayuda contiene en el título una breve descripcion de la tarea y un número, que va del 1 al 5. Los issues marcados como "1" son los más sencillos, prácticamente todo el mundo puede contribuir en ellos, mientras que los issues marcados con un "5" son los más complejos o difíciles de implementar.

| Dificultad | Explicación                                                                                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------|
|  1         | Estos issues son los más sencillos de GitCollab, prácticamente todo el mundo puede trabajar en ellos y la mayor parte no tienen código en sí. |  
|  2         | Estos issues implican algo de código y conocimiento de algunas herramientas específicas, de todas formas la mayor parte de estos issues pueden ser solucionados sin prácticamente esfuerzo. |
|  3         | Estos issues implican un conocimiento de las herramientas necesarias para completarlos, suelen ser fáciles de implementar en GitCollab pero hay que revisarlos bien. |
|  4         | Estos issues implican un conocimiento profundo de las herramientas necesarias para completarlos, la implementación de estos issues se puede complicar y ha que comprobar que esta sea escalable a largo plazo |
|  5         | Estos issues implican un conocimiento exhaustivo de las herramientas necesariass para completarlos. Serán revisados por más de un administrador antes de ser implementados |

En cada uno de estos issues encontrarás una descripción detallada de el task del issue, enlaces que te podrían servir, requisitos, la fecha de entrega (si es que la hay)...

Cuando decidas empezar un issue, deja un comentario explicando que tienes pensado hacer en el thread del issue. Cuando un moderador lo apruebe, se te asignará el issue y se le agregrará la etiqueta de "en curso", lo que significa que nadie más puede contribuir a ese issue hasta que tu lo finalices.

**Aparte de los tags de dificultad (1, 2, 3, 4, 5) hay numerosos tags más que te ayudan a entender el propósito del issue**, por ejemplo tags con el nombre de las herramientas necesarias para contribuir en ese issue. Vamos a repasar el resto de tags que un issue puede tener:
| Nombre | Descripción|
|--------|------------|
|python    | Necesitas conocer Python para completar los issues marcados con este tag |
|html    | Necesitas conocer HTML para completar los issues marcados con este tag |
|css    | Necesitas conocer CSS para completar los issues marcados con este tag |
|java script  | Necesitas conocer Java Script para completar los issues marcados con este tag |
|jinja2    | Necesitas conocer Jinja2, el motor de plantillas de Flask para completar los issues marcados con este tag |
|diseño | Necesitas conocimieentos en diseño para completar los issues marcados con este tag |


#### Proyecto en GitHub
En [el proyecto "issues" de GitCollab](https://github.com/pythonmurcia/gitcollab/projects/1) hay una representación gráfica con targetas de todos los issues **Un administrador o moderador se encarga de actualizar el proyecto cada hora**, estos están divididos en columnas dependiendo de su estado.

| Columna   | Descripción                                                                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Esperando | Estos issues no pueden ser asignados aún ya que para poder trabajar en ellos hay que finalizar otros issues, especificados dentro del mismo issue.|
| Por hacer | Los issues en la columna  de "por hacer" pueden ser assignados a contribuidores de GitCollab, puedes pedir que te asignen cualquiera de estos issues para trabajar con él. |                                                               
| En progreso |No puedes trabajar en estos issues ya que otras personas ya están trabajando en ellos, están marcados con el tag "en curso"                      |
| Finalizados - Por revisar | Estos issues ya han sido finalizados y las personas que trabajaran en ellos han creado un pull request, ahora un administrador o moderador de la organización tiene que revisar el trabajo que has hecho antes de hacer merge |
| Finalizados - revisados | Estos issues han sido revisados por un moderador y administrados. Ya están finalizados. |
| Cerrados | Estos issues han sido mergeados con el proyecto después de ser revisados por un administrador, pueden ser reabiertos si un administrador lo considera necesario. |

Cuando se te haya asignado uno de los issues para que trabajes en el, deberás seguir los pasos para trabajar en un repositorio remoto. Es decir:
* Haz un fork del repositorio en GitHub. Haces esto para adquirir permisos de push (en una copia local) y poder contribuir en el código.
* Clona el fork del repositorio en tu pc para poder trabajar con el desde local. 
* Crea un branch en el fork del repositorio con el nombre del issue, trabajarás bajo esa rama. Por ejemplo, si estoy trabajando en un issue llamado "crear-login-db" el branch de git se debería llamar igual
* Realiza los cambios necesarios para completar tu issue. Intenta tocar el menor numero de archivos posibles para evitar merge errors. Puedes crear subramas dentro de la rama de tu issue. 
* Conforme trabajes en el fork del proyecto, guarda tu progreso en el stage area con commits. 
* Pushea el código con los comandos `git remote -v`y `git push` para crear una rama remota.
* Ya deberías de poder crear el Pull Request en el repositorio. A la hora de crear la pull  request haz click en la casilla de "permitir commits a los administradores del proyecto"

**Te recomendamos que antes de contribuir te familiarizes con [Git](https://www.git-scm.com/book/es/v2), concretamente con [las implementaciones con GitHub](https://www.git-scm.com/book/es/v2/GitHub-Creaci%C3%B3n-y-configuraci%C3%B3n-de-la-cuenta)**

##### Cuando hayas conseguido que un administrador cierre tu issue, añaderemos tu nombre a la tabla del archivo [contributors.md](https://github.com/pythonmurcia/gitcollab/blob/master/colaborators.md), junto con el numero de issues en los que has participado

---
