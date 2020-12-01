# Proyecto de Simulación. Agentes

Autor: Tony Raul Blanco Fernández - C411

## 1. Ideas para la solución

Dada la bibliografía usada, se modelo un ambiente dado las características definidas. En el cual intervienen tanto agentes como objetos. Además de las variaciones efectuadas sistemáticamente dados los parámetros. Estos elementos serán expuestos a lo largo de este documento.

## 2. Modelos de agentes considerados

En este ambiente conviven dos agentes, los bebes y los robots. Los bebes se mueven de forma aleatoria dadas las reglas del problema. La selección de la siguiente acción esta determinada por la disponibilidad de casillas adyacentes o obstáculos.

Los robots son, por decirlo de alguna manera, el agente principal, el cual estamos evaluando en la simulación.

Los robots fueron modelados como Agente Reactivo y Agente Reactivo con Objetivo (Cognitivo)

Las acciones de ambos están ordenadas por prioridades de forma intencional, dada la naturaleza de los objetivos.

### Agente Reactivo

El orden de condición-acción es la siguiente:

1. Si esta sobre una casilla sucia => Limpia la casilla.
2. Si se carga a un bebe y se encuentra sobre una casilla de corral => Deja al bebe en esta casilla.
3. Si se carga a un bebe pero no estas en una casilla de corral => Camina sobre un pasaje valido hacia una casilla de corral aleatoria y vacía.
4. Si hay casillas alrededor, elige una aleatoria siempre prefiriendo este orden: Bebe sin Corral, Casilla Sucia, Casilla Vacía, Corral

### Agente Cognitivo

Este agente esta pendiente además de los objetivos por los que ha sido creado, su tarea es mantener a raya a los bebes siempre que tenga margen de suciedad en el ambiente (S). Si este valor se acerca a los limites. Entonces se dispone a limpiar.

Las primeras tres reglas se mantienen del Agente Reactivo. Y en adición: 

4. Si la suciedad actual < S => Busca a un bebe en el ambiente, se mueve en un camino valido hacia el.
5. Si la suciedad actual > S => Se mueve en un camino valido hacia una casilla sucia cercana.

>> Nota: S no es necesariamente el margen de los objetivos del ambiente. Son mas bien locales al robot.

Estas simples diferencias en las reglas permiten observar resultados que difieren y claramente contrastan.

## 4. Ideas seguidas para la implementación

La simulación utilizo eventos para la realización de los turnos. En cada turno los agentes actuaban, ordenados según la orientación, recibiendo a todo el estado del ambiente como sensor. 

Al turno de un agente, utilizando el estado del ambiente, ejecuta sus condiciones de forma prioritaria para determinar la acción a realizar. Luego de estas, la simulación evalúa si el estado del ambiente es final. De serlo, entonces termina la simulación.

Utilizamos una herencia sencilla para los elementos del ambiente. Ya que todos compartían el ser ubicados en una posición especifica. 

No fue usada una matriz para los cálculos, en lugar de esto, se realizaban consultas sobre un arreglo de objetos tratados de la forma mas básica. Esto reduce la eficiencia de las búsquedas, pero facilitaba mucho la implementación y la flexibilidad de las operaciones.

Al culminar `t` turnos, el ambiente se varia,  conservando los mismo elementos y sus estados, pero en posiciones diferentes y manteniendo las reglas. O sea, no se alteran, ni se añaden ni se retiran. Solo se mueven. 

Las búsquedas realizadas por los agentes se realizan con un BFS.

## 5.  Simulaciones

Ahora se mostraran los resultados de una serie de simulaciones utilizando diferentes parámetros. Por cada conjunto de parámetros se ejecutaran 30 simulaciones y se mostraran los resultados generales.



##### S1:  ancho 10, altura 10, obstáculos 10%, suciedad inicial 10%, bebes 4, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 15 / 30
- Suciedad promedio: 28.02% 

Cognitivo:

- Trabajos perfectos:  0/ 30
- Despedido: 12/ 30
- Suciedad promedio:  21.53 %

##### S2:  ancho 10, altura 10, obstáculos 20%, suciedad inicial 10%, bebes 4, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 15/ 30
- Suciedad promedio: 28.11% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 15 / 30
- Suciedad promedio: 26.31%

##### S3:  ancho 15, altura 15, obstáculos 10%, suciedad inicial 20%, bebes 4, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 4/ 30
- Suciedad promedio: 15.72% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 2 / 30
- Suciedad promedio:  11.78%

##### S4:  ancho 15, altura 15, obstáculos 30%, suciedad inicial 5%, bebes 5, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 16 / 30
- Suciedad promedio: 31.10% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 4 / 30
- Suciedad promedio:  16.73%

##### S5:  ancho 30, altura 30, obstáculos 20%, suciedad inicial 0%, bebes 6, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio: 24.54% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 3 / 30
- Suciedad promedio:  15.29%

##### S6:  ancho 20, altura 20, obstáculos 10%, suciedad inicial 10%, bebes 5, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio: 16.28% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 5 / 30
- Suciedad promedio:  14.24%

##### S7:  ancho 15, altura 15, obstáculos 10%, suciedad inicial 40%, bebes 2, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 0 / 30
- Suciedad promedio: 8.43% 

Cognitivo:

- Trabajos perfectos:  3 / 30
- Despedido: 2 / 30
- Suciedad promedio: 9.38%

##### S8:  ancho 20, altura  20, obstáculos 5%, suciedad inicial 0%, bebes 10, t 20

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 10 / 30
- Suciedad promedio: 29.2% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 8 / 30
- Suciedad promedio:  24.77%

##### S9:  ancho 15, altura 15, obstáculos 25%, suciedad inicial 40%, bebes 1, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 1 / 30
- Suciedad promedio: 10.36% 

Cognitivo:

- Trabajos perfectos:  5 / 30
- Despedido: 0 / 30
- Suciedad promedio:  3.4%

##### S10:  ancho 15, altura 15, obstáculos 0%, suciedad inicial 0%, bebes 5, t 15

Reactivo:

- Trabajos perfectos:  0 / 30
- Despedido: 1 / 30
- Suciedad promedio: 11.8% 

Cognitivo:

- Trabajos perfectos:  0 / 30
- Despedido: 1/ 30
- Suciedad promedio:  11.43%

## Conclusiones

Ciertamente los resultados no destacan en cuanto a calidad al desempeño del Agente Cognitivo sobre el Reactivo. Aunque ciertamente el tiempo de ejecución (dada la implementación) fue considerablemente mejor en el Reactivo, unas 10 veces menor que el Cognitivo.  Aun así solo el Cognitivo logro limpiar toda la casa alcanzando la condición de victoria.


>> Notas: Varios robots puede ejecutarse en un mismo ambiente, por como fue creado este programa. Pero por no ensuciar los resultados según la orientación. No se publicaron resultados con estos parámetros.

