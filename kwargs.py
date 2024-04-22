#un solo * es una lista (args)
#2 * un diccionario (kwargs)
def escribir_el_nombre(*args,**kwargs):
    print("      Inicio")
    print(kwargs)
    for arg in args:
        print(arg)
    for keys,values in kwargs.items():
        print("key",keys,'value',values)


escribir_el_nombre(
    primer_nombre='Luciano',
    segundo_nombre='Cristian',
    primer_apellido='Toneatti',
    segundo_apellido='Gandolfo'
)

escribir_el_nombre(
    primer_nombre='Nehuen',
    primer_apellido='Donozco',
    segundo_apellido='Marquez'
)

escribir_el_nombre(
    primer_nombre='Celina',
    segundo_nombre='Anahi',
    primer_apellido='Guerra Diaz'
)


