FastAPI CRUD Notes es un proyecto diseñado para gestionar notas mediante una API construida con FastAPI, utilizando MongoDB como base de datos. El objetivo principal de este proyecto es ofrecer un conjunto de endpoints para crear, leer, actualizar y eliminar (CRUD) notas de manera eficiente y escalable.

Cada nota tiene atributos como título, contenido, etiquetas, fecha de creación, historial de versiones, y más. La API permite a los usuarios no solo gestionar estas notas, sino también llevar un registro de los cambios realizados a lo largo del tiempo mediante un historial de versiones.

Características Principales:
Creación de Notas: Permite crear una nueva nota con atributos personalizados como título, contenido, etiquetas, etc.
Lectura de Notas: Posibilita la obtención de todas las notas o de una nota específica a través de su ID.
Actualización de Notas: Facilita la modificación de una nota existente y registra los cambios en un historial de versiones.
Eliminación de Notas: Permite eliminar una nota específica de la base de datos.


<hr />
Instalación y Ejecución

Clonar el repositorio:
```bash
git clone https://github.com/usuario/FastAPI-CRUD-Notes.git
cd FastAPI-CRUD-Notes
```

Instalar las Dependencias:
```bash
pip install -r requirements.txt
```

Ejecutar la Aplicación:
```bash
uvicorn app.main:app --reload
```

Documentación Interactiva:
- Accede a la documentación interactiva en http://127.0.0.1:8000/docs para probar los endpoints de la API.

<hr />


Endpoints de la API
POST /api/notes:

Descripción: Crea una nueva nota.
Entrada: Un objeto JSON que contiene los detalles de la nota (título, contenido, etiquetas, etc.).
Salida: El ID de la nota recién creada.
GET /api/notes:

Descripción: Recupera una lista de todas las notas.
Entrada: Ninguna.
Salida: Una lista de notas.
GET /api/notes/{note_id}:

Descripción: Recupera los detalles de una nota específica.
Entrada: El ID de la nota.
Salida: Los detalles de la nota.
PUT /api/notes/{note_id}:

Descripción: Actualiza una nota existente.
Entrada: El ID de la nota y un objeto JSON con los campos a actualizar.
Salida: El número de documentos modificados.
DELETE /api/notes/{note_id}:

Descripción: Elimina una nota específica.
Entrada: El ID de la nota.
Salida: Un mensaje de confirmación de eliminación.