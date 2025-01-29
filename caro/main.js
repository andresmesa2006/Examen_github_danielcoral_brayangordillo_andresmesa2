//Asíncronia y funciones callbacks 
// Función simulando una tarea que tomará un tiempo, por ejemplo, una petición a un servidor
function holi(funcionCallback){
    console.log(" ---> ¡Inició tarea!")
    setTimeout(() => {
        console.log(" ---> Tarea Asíncrona ejecutada.")
        funcionCallback()
    },1000);
}

console.log("***** Inicia programa *****")

holi(()=>{console.log("Callback Ejecutado")})

console.log("*** Fin programa ***")

//Gestión de promesas
const promesa1 = new Promise(function(resolve,reject){
console.log("Ejecutando promesa...")
const cumplirpromesa = true;
    if(cumplirpromesa){
        setTimeout(()=>{
            console.log("Pasaron 3 segundos...")
            resolve("Promesa ejecutada con exito!");
        }, 3000);
    }
    else reject("Promesa rechazada")
});
console.log(promesa1)                                                                                                                              