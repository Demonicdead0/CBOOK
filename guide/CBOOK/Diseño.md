El diseño es algo que siempre me complica la verdad, pero ahorita me está gustando esta paleta de colores que tengo en obsidian, se llama ITS Theme lo cual, me gustaría que sea de ese color, por ahora solo tendrá **Modo nocturno** ya que hacer para otro diseño sería complicado, bueno, ahora, cómo sería la interfaz?
Pues primero que debe tener lo siguiente:
# Principal
- [ ] Soporta el sistema markdown
- [ ] También debe soportar Maktex o Tex para las fórmulas matemáticas.
- [ ] lo primero que debe aparecer en la pantalla es **seleccionar notebook** y debe elegir una carpeta que contendrá todos los datos, (esto es principalmente para que se pueda exportar a otros lados con mayor facilidad)
	- [ ] Luego de eso tendrás una pantalla principal para que vea todos los elementos creados
	- [ ] En la parte de abajo existirá un botón que es para crear nuevo tema 

# Vista
- [ ] Menú principal.
- [ ] Contenido
- [ ] Archivos

# Prototipo Alpha

## Menú principal
```handdrawn-ink
{
	"versionAtEmbed": "0.3.3",
	"filepath": "Ink/Drawing/2025.1.27 - 18.50pm.drawing",
	"width": 500,
	"aspectRatio": 1
}
```

## Contenido de la carpeta


```handdrawn-ink
{
	"versionAtEmbed": "0.3.3",
	"filepath": "Ink/Drawing/2025.1.27 - 19.00pm.drawing",
	"width": 500,
	"aspectRatio": 1
}
```
Todavía tengo que pensar como diferenciar entre carpeta y archivo, pero por el momento se vería algo así el contenido de una carpeta, que si haces click en una carpeta, pues te muestra casi el mismo diseño y solo cambia el contenido, como una forma recursiva de hacerlo 
## Archivo

```handdrawn-ink
{
	"versionAtEmbed": "0.3.3",
	"filepath": "Ink/Drawing/2025.1.27 - 19.08pm.drawing",
	"width": 500,
	"aspectRatio": 1
}
```
En sí, tiene tres secciones.
- A: En esta sección, muestra un índice del contenido que se está viendo.
- B: El contenido principal.
- C: Cuando pones *play* en la sección B, puedes ejecutar ese código donde arriba puedes poner el input y output y ejecutas el código. También la idea principal es contar el tiempo que se tardó en ejecutar un código y también mostrar la cantidad de líneas ejecutadas (aunque creo creo que es más difícil esto pero bueno).
Y claro un encabezado para regresar.
También para poner código también.