
from fastapi import FastAPI, Body


from fastapi.responses import  HTMLResponse

app= FastAPI(
 title="My Bank API",
 description = "Api Para sistema Bancario, Ejercicio Académico",
 version= "0.0.1"
)


@app.get('/', tags=["Cuenta Ahorro"])
def read_root():
 return HTMLResponse('<h2> My Bank App </h2>')



clientes= {

 3222272028:{
 "id": 70100100,
 "nombre": "pepito",
 "Telefono": "3214567890",
  "Correo": "pp@mail.com",
  "Key":3214,
     "Tipo de Persona": "Persona Natural"

},
3135299915:{
 "id": 1037104337,
 "nombre": "Caro Janne",
 "Telefono": "3135299915",
  "Correo": "caro@mail.com",
  "Key":1234,
    "Tipo de Persona": "Persona Juridica"
}
}

@app.post('/crear_cliente/{phone,id,name,mail,key, type}', tags=["crear clientes"])
def crear_cliente(phone: int = Body(), id: int = Body(), name: str = Body(), mail: str = Body(), key:int = Body(), type:str = Body()):
  """
  phone = input("Telefono")
  id = int(input("Identificacion:"))
  name = input("Nombre")
  mail = input("Correo")
  key = int(input("Clave"))
  type = input("Tipo Cliente")"""
  clientes[phone] = {"id":id,"Nombre": name, "Telefono":phone, "Correo": mail, "Key": key,"Tipo Persona": type}



@app.get('/get_clientes', tags=["Obtener Clientes"])
def obtener_clientes():
    return clientes

@app.get('/get_cliente/', tags=["Obtener Cliente por tipo"])
def obtener_cliente_por_tipo(type: str):
    return type

@app.get('/get_cliente/{clave}', tags=["Obtener Cliente"])
def obtener_cliente(clave: int):
    #for items in clientes:
        if clave in clientes:
            return clientes[clave]
        else:
          return []

@app.put('/modificar_cliente/{phone}', tags=["Modificar cliente"])
def modificar_cliente(phone: int, id: int = Body(), name: str = Body(), mail: str = Body(), key:int = Body(), type:str = Body()):
    for item in clientes:
        if phone in clientes:
            """
            clientes["id"]= id,
            clientes["nombre"] = name,
            clientes["Telefono"]= phone,
            clientes["Correo"]=mail,
            clientes["Key"]=key,
            clientes["Tipo de Persona"]= type"""
        clientes[phone] = {"id": id, "Nombre": name, "Telefono": phone, "Correo": mail, "Key": key, "Tipo Persona": type}

@app.delete('/eliminar_cliente/{phone}', tags=["Eliminar Cliente"])
def eliminar_cliente(phone: int):
    #for item in clientes:
        if phone in clientes:
            clientes.pop(phone)
            return clientes