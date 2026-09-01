## Conventional Commits

Todos los commits deben seguir la especificación de [Conventional Commits](https://www.conventionalcommits.org/). El formato del mensaje es:
7
```
<tipo>[<scope opcional>]: <descripción>

[cuerpo opcional]
```

**Tipos permitidos:**

- `feat`: Nueva funcionalidad.
- `fix`: Corrección de un bug.
- `docs`: Cambios en documentación.
- `style`: Cambios de formato sin afectar código (espacios, puntuación, etc.).
- `refactor`: Cambio de código que no corrige un bug ni agrega funcionalidad.
- `test`: Agregar o corregir tests.
- `chore`: Cambios en build process o herramientas auxiliares.

Ejemplo: `feat(auth): add login endpoint`

---

## Reglas Generales

- Las specs generadas deben estar en español a menos que el usuario te lo indique antes, el código y su documentación deben estar en inglés
- Para revisar la estructura del proyecto usa el comando ls -T --no-permissions --no-filesize --no-user --no-time --no-git --git-ignore
- Antes de empezar a escribir código revisa las skills instaladas.
- Siempre que se necesite documentación de una librería, framework o herramienta, se debe usar **Context7** para obtenerla antes de escribir código. Esto aplica a:
  - Decisiones de API o funcionalidad de librerías.
  - Resolver dudas sobre configuración o patrones de uso.
  - Verificar comportamientos antes de asumirlos.
- Cuando no encuentres documentación usando **Context7** debes pedirle al usuario la documentación de la dependencia y respaldarla en ./docs/dependencies/[component].md
- **Nunca debes instalar una dependencia sin preguntar primero al usuario.** Antes de agregar cualquier paquete se debe:
  1. Informar qué dependencia se va a instalar y por qué.
  2. Esperar la confirmación del usuario antes de ejecutar el comando de instalación.
- Antes de pensar en instalar una nueva dependencia, revisa las dependencias instaladas y utiliza esa dependencia.
- No asumir: si algo no está claro, preguntar.
- No cometer código sin instrucción explícita del usuario.
- Mantener los cambios mínimos y enfocados.
- Respetar las convenciones y patrones existentes del proyecto.
- Genera subagentes cuando lo consideres necesario.
- Las propuestas de spec futuras se encuentran en ./docs/specs/proposal/[spec-name].md y las spec pendientes a implementar se encuentran en ./docs/specs/pending/[spec-name].md. Una vez desarrolladas estas se deben borrar de los respectivos directorios.
- Backend en Python siguiendo PEP8; usar ruff/black si están configurados en pyproject.toml.
- La clase principal del plugin hereda de InvenTreePlugin y de los mixins necesarios (ver abajo). No añadir mixins que el plugin no use realmente.
- Definir siempre NAME, SLUG, TITLE, AUTHOR, DESCRIPTION, VERSION en la clase del plugin.
- El SLUG debe ser estable entre versiones (se usa como identificador en la base de datos).
- Frontend en TypeScript/React usando @inventreedb/ui; componentes exportados con export default.
- No romper compatibilidad con la versión mínima de InvenTree declarada en pyproject.toml (INVENTREE_API_VERSION / rango soportado).

Recursos de referencia
- Documentación de plugins: https://docs.inventree.org/en/latest/plugins/
- Mixins: https://docs.inventree.org/en/latest/plugins/mixins/
- Plugin creator tool: https://github.com/inventree/plugin-creator
- Walkthrough de ejemplo: https://docs.inventree.org/en/latest/plugins/walkthrough/

---

## Comandos habituales
 
```bash
# Instalar el plugin en modo editable dentro del entorno de InvenTree
pip install -e .
 
# Ejecutar tests
pytest
 
# Frontend (si el plugin usa UserInterfaceMixin)
cd frontend
npm install
npm run dev      # servidor de desarrollo con hot reload
npm run build    # compila assets a my_plugin/static/
 
# Levantar InvenTree en modo desarrollo para probar el plugin
invoke dev.server
```

---

## Reglas de Tests

Los tests se organizan por tipo en rutas fijas, espejando el componente o el adapter que prueban:

- **Tests unitarios**: `./tests/unit/path/to/component` — sin I/O real; usan fakes de los puertos.
- **Tests de integración**: `./tests/integration/path/to/test` — prueban los adapters contra sus dependencias reales (ffmpeg, `std::fs`, etc.).
- **Tests e2e**: `./tests/e2e/path/to/test` — flujos completos de extremo a extremo.

Ejemplo de estructura:

```
tests/
├── unit/
│   ├── domain/format.rs
│   └── application/convert_sync.rs
├── integration/
│   ├── ffmpeg/convert.rs
│   └── filesystem/crud.rs
└── e2e/
    └── conversion_flow.rs
```
