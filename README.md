# Proyecto de Simulacion. Agentes

Autor: Tony Raul Blanco Fernandez - C411

## 1. Ideas para la solucion

Dada la bibliografia usada, se modelo un ambiente dado las caracteristicas definidas. En el cual intervienen tanto agentes como objectos. Ademas de las variaciones efectuadas sistematicamente dados los parametros. Estos elementos seran expuestos a lo largo de este documento.

## 2. Modelos de agentes considerados

En este ambiente conviven dos agentes, los bebes y los robots. Los bebes se mueven de forma aleatoria dadas las reglas del problema. La seleccion de la siguiente accion esta determinada por la disponibilidad de casillas adyasentes o obstaculos empujables.

Los robots son, por decirlo de alguna manera, el agente principal, el cual estamos evaluando en la simulacion.

Los robots fueron modelados como Agente Reactivo y Agente Reactivo con Objetivo (Cognitivo)

Las aciones de ambos estan ordenadas por prioridades de forma intencional, dada la naturaleza de los objetivos.

### Agente Reactivo

El orden de condicion-accion es la siguiente:

1. Si esta sobre una casilla sucia => Limpia la casilla.
2. Si se carga a un bebe y se encuentra sobre una casilla de corral => Deja al bebe en esta casilla.
3. Si se carga a un bebe pero no estas en una casilla de corral => Camina sobre un pasaje valido hacia una casilla de corral aleatoria y vacia.
4. Si hay casillas alrededor, elige una aleatoria siempre prefiriendo este orden: Bebe sin Corral, Casilla Sucia, Casilla Vacia, Corral

### Agente Cognitivo

Este agente esta pendiente ademas de los objetivos por los que ha sido creado, su tarea es mantener a raya a los bebes siempre que tenga margen de suciedad en el ambiente (S). Si este marge se acerca a los limites. Entonces se dispone a limpiar.

Las primeras tres reglas se mantienen del Agente Reactivo. Y en adiion: 

4. Si la suciedad actual < S => Busca a un bebe en el ambiente, se mueve en un camino valido hacia el.
5. Si la suciedad actual > S => Se mueve en un camino valido hacia una casilla sucia cercana.

>> Nota: S no es necesariamente el margen de los objetivos del ambiente. Son mas bien locales al robot.

Estas simples diferencias en las reglas permiten observar resultados que difieren y claramente contrastan.

## 4. Ideas seguidas para la implementacion

La simulacion utilizo eventos para la realizacion de los turnos. En cada turno los agentes actuavan, ordenados segun la orientacion, recibiendo a todo el estado del ambiente como sensor. 

Al turno de un agente, utilizando el estado del ambiente, ejecuta sus condiciones de forma prioritaria para determinar la accion a realizar. Luego de estas, la simulacion evalua si el estado del ambiente es final. De serlo, entonces termina la simulacion.

Utilizamos una herencia sencilla para los elementos del ambiente. Ya que todos compartian el ser ubicados en una posicion especifica. 

No fue usada una matriz para los calculos, en lugar de esto, se realizaban queries sobre un arreglo de objetos tratados de la forma mas basica. Esto reduce la eficiencia de las busquedas, pero facilitaba mucho la implementacion y la flexibilidad de las operaciones.

Al culminar `t` turnos, el ambiente se varia,  conservando los mismo elementos y sus estados, pero en pociciones diferentes y manteniendo las reglas. O sea, no se alteran, ni se añaden ni se retiran. Solo se mueven. 

Las busquedas realizadas por los agentes se realizan con un BFS.

## 5.  Simulaciones

Ahora se mostraran los resultados de una serie de simulaciones utilizando diferentes parámetros. Por cada conjunto de parámetros se ejecutaran 30 simulaciones y se mostraran los resultados generales.



##### S1:  ancho 10, altura 10, obstáculos 10%, suciedad inicial 10%, bebes 4, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 15 / 30
- Suciedad promedio: 28.02% 

Cognitivo:

- Trabajos perfectos:  - / 30
- Despedido: - / 30
- Suciedad promedio:  - %

##### S2:  ancho 10, altura 10, obstáculos 20%, suciedad inicial 10%, bebes 4, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 17 / 30
- Suciedad promedio: 31.06% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

##### S3:  ancho 15, altura 15, obstáculos 10%, suciedad inicial 20%, bebes 4, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio: 12.17% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

##### S4:  ancho 15, altura 15, obstáculos 30%, suciedad inicial 5%, bebes 5, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 10 / 30
- Suciedad promedio: 26.59% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

##### S5:  ancho 30, altura 30, obstáculos 20%, suciedad inicial 0%, bebes 6, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 7 / 30
- Suciedad promedio: 19.6% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

##### S6:  ancho 20, altura 20, obstáculos 10%, suciedad inicial 10%, bebes 5, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 7 / 30
- Suciedad promedio: 19.6% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

##### S7:  ancho 15, altura 15, obstáculos 10%, suciedad inicial 40%, bebes 2, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 7 / 30
- Suciedad promedio: 19.6% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

##### S8:  ancho 20, altura  20, obstáculos 5%, suciedad inicial 0%, bebes 10, t 20

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 7 / 30
- Suciedad promedio: 19.6% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

##### S9:  ancho 15, altura 15, obstáculos 25%, suciedad inicial 40%, bebes 1, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 7 / 30
- Suciedad promedio: 19.6% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

##### S10:  ancho 15, altura 15, obstáculos 0%, suciedad inicial 0%, bebes 5, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 7 / 30
- Suciedad promedio: 19.6% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio:  -%

## Conclusiones

Ciertamente los resultados destacan en cuanto a calidad al desempeño del Agente Cognitivo sobre el Reactivo. Aunque ciertamente el tiempo de ejecución (dada la implementación) fue considerablemente mejor en el Reactivo, unas 10 veces menor que el Cognitivo.  


>> Notas: Varios robots puede ejecutarse en un mismo ambiente, por como fue creado este programa. Pero por no ensuciar los resultados según la orientación. No se publicaron resultados con estos parámetros.

