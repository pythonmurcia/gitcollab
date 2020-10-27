## Rutas de GitCollab

| URL | descripción | Funciones |
|-----|-------------|-----------|
| `/` | Página de inicio de GitCollab | Redirigir a `index.html` si el usuario no ha iniciado sesión. Redirigir a `app.html` si el usuario ha iniciado sesióon |
| `/login` | Ruta para que el usuario inicie sesión | Comprobar si un usuario se encuentra en la base de datos y que los credenciales son válidos. Redirigir a `app.html`|
| `/singup/` | Permite a un usuario registrarse | Debe comprobar que los credenciales son válidos y que el usuario no está ya registrado |
| `/<name>` | Muestra el perfil de <name> | Extrae esta información de una base de datos |
| `/<name>/edit` | Permite editar tu perfil | Conectar con la base de datos y editar a un usuario |
| `/<name>/delete` | Permite eliminar tu perfil después de una pequeña comprobación | Conectar con una base de datos para saber como funciona. |
| `/<name>/<repo>` | Muestra información sobre los repositorios de un usuario |
