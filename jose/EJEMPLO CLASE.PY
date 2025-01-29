from json import dumps

data = [
    {   "NOMBRE":"FARIT",
        "CUENTA":"465465",
        "CLAVE":"5555"
    },
     {
        "NOMBRE":"ALEJANDRO",
        "CUENTA":"8989898",
        "CLAVE":"9999"
    },
    {
        "NOMBRE":"asdasdsad",
        "CUENTA":"8989asd898",
        "CLAVE":"aaaaa"
    }
]

archivo = open("pureba_json.son", "w")

data_json = dumps(data)

archivo.write(data_json)

archivo.close
print(data_json)