from tkinter.tix import Form
from flet import *
from pymongo import MongoClient

# Conexión a la base de datos
client = MongoClient("mongodb+srv://root:Karma30102001.@cluster0.e5cs5gc.mongodb.net/")
db = client["test"]
collection = db["personas"]

# Función para obtener todos los documentos
def get_personas():
    return list(collection.find())

# Función para crear un nuevo documento
def crear_persona(nombre, edad):
    collection.insert_one({"nombre": nombre, "edad": edad})

# Función para actualizar un documento
def actualizar_persona(id, nombre, edad):
    collection.update_one({"_id": id}, {"$set": {"nombre": nombre, "edad": edad}})

# Función para eliminar un documento
def eliminar_persona(id):
    collection.delete_one({"_id": id})

# Página principal
def main_page(page):
    # Lista de personas
    personas = get_personas()

    # Formulario para crear una nueva persona
    form = Form(
        [
            TextField(label="Nombre"),
            TextField(label="Edad"),
        ],
        submit_button=ElevatedButton("Crear"),
        on_submit=lambda e: crear_persona(e.data["nombre"], e.data["edad"]),
    )

    # Lista de personas
    lista = ListView(
        [
            ListTile(
                title=persona["nombre"],
                subtitle=str(persona["edad"]),
                trailing=[
                    IconButton(
                        icon=icons.EDIT,
                        on_click=lambda e: editar_persona(page, persona["_id"]),
                    ),
                    IconButton(
                        icon=icons.DELETE,
                        on_click=lambda e: eliminar_persona(persona["_id"]),
                    ),
                ],
            )
            for persona in personas
        ]
    )

    page.content = Column([form, lista])

# Página para editar una persona
def editar_persona(page, id):
    persona = collection.find_one({"_id": id})

    # Formulario para editar la persona
    form = Form(
        [
            TextField(label="Nombre", value=persona["nombre"]),
            TextField(label="Edad", value=str(persona["edad"])),
        ],
        submit_button=ElevatedButton("Actualizar"),
        on_submit=lambda e: actualizar_persona(id, e.data["nombre"], e.data["edad"]),
    )

    page.content = form

# Rutas
app = FletApp(
    routes={
        "/": main_page,
        "/editar/:id": editar_persona,
    }
)

app.run()