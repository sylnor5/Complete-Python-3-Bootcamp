# El equipo de ChatRadar

Un coordinador reparte el trabajo, los especialistas trabajan en paralelo, alguien comprueba
el resultado y la fundadora aprueba.

| Rol | Quién | Hace | No hace |
|---|---|---|---|
| Fundadora | persona | Decide: textos, clasificaciones, qué se publica | — |
| Coordinador | Claude (sesión principal) | Divide el trabajo, reparte, junta resultados, programa, sube | Decidir por la fundadora |
| Marketing | agente `chatradar-marketing` | Textos y mensajes, en 4 idiomas | Editar archivos |
| Psicólogo | agente `chatradar-psicologo` | Cómo lo vive cada lado; anclaje y sensibilidad | Editar archivos |
| Verificador | agente `chatradar-verificador` | Comprueba hechos; revisa listas desde los dos lados | Editar archivos |
| QA | agente `chatradar-qa` | Prueba la web en navegador (móvil, 4 idiomas) con capturas | Editar el código |
| Redes | agente `chatradar-redes` (sesión aparte desde el lanzamiento) | Calendario, publicaciones y respuestas propuestas en 4 idiomas | Publicar o responder solo |
| Diseño | skills `impeccable` y `emil-design-eng` | Claridad visual, maquetas | — |

Las definiciones de los agentes están en `.claude/agents/` (raíz del repositorio).

## Cómo pasa una tarea
1. El coordinador anota la tarea en PENDIENTES.md.
2. Reparte: lo independiente va en paralelo (por ejemplo, marketing y psicólogo a la vez).
3. Antes de mostrar algo a la fundadora: el verificador comprueba hechos y QA prueba en navegador.
4. La fundadora aprueba. Las decisiones nuevas se anotan en DECISIONES.md.
5. El coordinador sube el cambio y da el comando para actualizar la web.

## Dónde aprueba siempre la fundadora
- Cualquier texto visible nuevo o cambiado.
- Clasificaciones (afirmaciones, origen y línea editorial de fuentes).
- Publicar algo hacia afuera (dominio, redes, mensajes, pagos).
