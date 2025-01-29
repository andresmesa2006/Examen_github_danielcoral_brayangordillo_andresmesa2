const mensaje = document.getElementById('mensaje'); 
function nuevo_item(id) { 
const div = document.createElement("div"); 
div.textContent = `Item ${id} en el contenedor`; 
div.setAttribute("class", "item borde fuente"); 
div.setAttribute("id", `item${id}`); 
return div 
} 
// obteniendo elemento del DOM 
const elemento = document.getElementById('contenedor');

//el elemento nuevo se agrega al final de la sto de los del et 
let div = nuevo_item(4); 
elemento.appendChild(div); 


//// removeChild(child) 
///
//Elimina un elemento DOM de su padre. 
// // El elemento eliminado se devuelve como resultado. 
let item = document.querySelector("#item2"); 
mensaje.textContent = elemento.removeChild(item); 

//replaceChild

item=document.querySelector('#item');
div= nuevo_item(5);
elemento.replaceChild(div, item);



// // insertBefore(new, node) 
//// Inserta un elemento nuevo antes de otro elemento. 

item = document.querySelector("#item3|"); 
div = nuevo_item(6); 
elemento.insertBefore(div, item); 

// // Cuendo el nodo es nulo agrega el elemento al final. 
// div nuevo item (7);

//div = nuevo_item(7);
//elemento.insertBefore(div, null);

// *********************************************************************
// ********** Propiedades para modificacion de elementos ***************
// *********************************************************************


// *********************** before() ************************* //
// Inserta contenido antes del elemento seleccionado

div=nuevo_item(8);
elemento.before(div);

// *********************** after() ************************* //
// Inserta contenido después del elemento seleccionado

div=nuevo_item(9);
elemento.after(div);

// *********************** prepend() ************************* //
// Inserta contenido al principio de un elemento DOM

div=nuevo_item(10);
elemento.prepend(div);

// *********************** append() ************************* //
// Inserta contenido al final de un elemento DOM

div=nuevo_item(11);
elemento.append(div);

// ********************** replaceChildren() ******************************************************** 
// remplaza todos los hijos de un elemento DOM

div = nuevo_item(12);
let div2=nuevo_item(13);
elemento.replaceChild(div, div2);

// ********************** replaceWith() ****************************
// Reemplaza un elemento DOM con otro elemento DOM

div=nuevo_item(14);
elemento.replaceWith(div);

// ********************** remove() *****************************************
// Elimina un elemento DOM del DOM

elemento.remove();
