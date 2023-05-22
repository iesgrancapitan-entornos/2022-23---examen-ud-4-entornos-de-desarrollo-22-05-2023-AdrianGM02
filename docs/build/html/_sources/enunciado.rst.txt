EXAMEN
========


Examen Tema 4 Entornos de Desarrollo - 1DAW
Refactorización, Documentación y control de versiones

El examen se divide en 3 bloques claramente diferenciados: Refactorización, Documentación y control de versiones. Cada uno de ellos con una puntuación sobre 10. Para dar por superado el RA relacionado con el tema 4, se deben aprobar las 3 partes.

En cada apartado se indica la puntuación y que parte corresponden. Las 3 se puntúan sobre 10

Sigue detalladamente las instrucciones del examen. Cualquier duda, pregunta a tu profesor.

En el repositorio tienes en código fuente que será la base sobre la cual desarrollaremos el examen. Dividiremos el examen en 3 partes, y las utilizaremos para desarrollar las versiones de git y github. Evidentemente, usaremos las buenas prácticas de git y github que hemos estado trabajando durante el curso
Ramas y Merge I
Para el workflow del examen, utilizaremos las siguientes ramas: desarrollo, refactorización, documentación. Crealas cuando se te indique.

Crea la rama "desarrollo"

Refactorización
Crea la rama "refactorizacion" a partir de la rama desarrollo y cambiate a esa rama (CV - 0.25 puntos)

Haz las refactorizaciones que necesites para que "Guau" sea un campo de la clase Perro llamado "ladra" y se inicialize en el constructor. (RF - 4 puntos)

Compromete el estado actual con el mensaje "Refactorizacion 1 Perro - Nombre y Apellidos" (CV - 0.25 puntos)

Extrae una superclase a partir de la clase "Coche" llamada "Vehículo" con los campos:

num_serie
fabricante
color
Compromete el estado actual con el mensaje "Refactorizacion 2 Superclase Vehículo - Nombre y Apellidos". (RF - 6 puntos)

Fusiona la rama "refactorizacion" en la rama "desarrollo" (CV - 0.5 puntos)

Documentación
Crea la rama "documentacion" a partir de la rama desarrollo y cambiate a esa rama (CV - 0.25 puntos)

Documenta con el formato Docstring "reStructuredText" las clases y los métodos para que aparezcan sus descripciones, autor, y descripción de los parámetros y devoluciones de cada método. Compromete el estado actual con el mensaje "Documentación 1 - Nombre y Apellidos" (DOC - 2.5 puntos)

Añade todos los rst necesarios para que aparezca la documentación de todos las clases (DOC - 1 punto)

Añade en el index un rst para que haya un enlace donde aparezca el enunciado completo del examen (DOC - 1 punto)

Añade en la documentación: (DOC - 3 puntos)

Autor: Tu nombre y apellidos
Nombre del proyecto "Examen Entornos"
Versión: una versión con notación "versionado semántico"
copyright: El que tu quieras
Añade las extensiones "autodoc, intersphinx, todo, mathjax, napoleon, autosummary
Usa el tema "sphinx_rtd_theme"
Genera la documentación html usando la generación de documentación sphinx y guárdalo en tu repositorio en una carpeta que se llame "doc". Compromete el estado actual con el mensaje "Documentación 2 Javadoc - Nombre y Apellidos" (DOC - 2.5 puntos)

Control de Versiones
Fusiona la rama "documentacion" en la rama "desarrollo" (CV - 0.5 puntos)
Pull Request
Actualiza tu repositorio, si no lo has hecho ya.

Realiza un fork del repositorio del examen a tu cuenta de github. (CV - 0.5 puntos)

En el repositorio forkado, ve a la rama de documentación y modifica la etiqueta title del index.html con tu nombre y apellidos

Compromete los cambios con la etiqueta "pull request Nombre y apellidos" (CV - 0.25 puntos)

Realiza un pull request de la rama documentacion de tu repositorio forkado sobre la rama desarrollo del repositorio del examen (CV - 2.5 puntos)

Acepta los cambios y haz un merge de tu pull request (CV - 0.5 puntos)

No borres el repositorio de tu cuenta hasta que el examen esté corregido

Issues
Observa los issues que deberías tener en tu repositorio de examen.




Cierralos con un solo commit que contenga en la etiqueta "Cerrando Issues - Nombre y Apellidos" (CV - 1.5 puntos)

Ramas y Merge II
Fusiona la rama desarrollo en la rama main (CV - 0.5 puntos)
Github Pages
Crea una página con tu repositorio de la rama main. En la url "iesgrancapitan-entornos.github.io/repositorioexamen/doc" debe aparecer tu documentación sphinx (CV - 0.5 puntos)
Tags y Releases
Añade un tag en el primer commit del repositorio de la rama main con la v0.0.1 y la descripción "Primera versión alpha - Nombre y Apellidos" (CV - 0.5 puntos)

Añade otro tag en el último commit (sin crear otro commit nuevo) con la v1.0.0 "Primera Release Candidate - Nombre y Apellidos" (CV - 0.5 puntos)

Sube sólo los tags al repositorio. Estos tags deben aparecer también en la pestaña release (CV - 0.5 puntos)

Gitlab
Crea un repositorio en el grupo de Entornos de gitlab. Añadelo a tu repositorio local y súbelo. Deberás tener el mismo repositorio tanto en github como gitlab (CV - 0.5 puntos)
Nota
En caso de cualquier duda y/o errata, será resuelta durante la realización del examen