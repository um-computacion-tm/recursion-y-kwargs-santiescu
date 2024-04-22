import unittest

database={
    1:{"nombre1":"Pablo",
       "nombre2":"Diego",
       "apellido1":"Ruiz",
       "apellido2":"Picasso"},
    2:{"nombre1":"Elio",
       "apellido1":"Anci"},
    3:{"nombre1":"Elias",
       "nombre2":"Marcos",
       "nombre3":"Luciano",
       "apellido1":"Marcelo",
       "apellido2":"Gonzalez"}
}
def buscar_datos(*args):
    for id,usuario in database.items():
        for nombre in args:
            if nombre in usuario.values():
                return id
    return 'no existe el usuario'



class TestBuscardatos(unittest.TestCase):
    def test_usuario1(self):
        result=buscar_datos("Pablo","Diego","Ruiz","Picasso")
        self.assertTrue(result==1)

    def test_usuario2(self):
        result=buscar_datos("Elio","Anci")
        self.assertTrue(result==2)

    def test_usuario3(self):
        result=buscar_datos("Elias","Marcos","Luciano","Marcelo","Gonzalez")
        self.assertTrue(result==3)

    def test_usuarionoexiste(self):
        result=buscar_datos("Ignacio","Milutin",)
        self.assertTrue(result=='no existe el usuario')


unittest.main()