
/*
yo soy el creado de este script

*/
// tips de dato string

var nombre = "Carlos";
console.log(nombre);

var nombre = 10;
console.log(typeof nombre);

var nombre = 15.2;
console.log(typeof nombre)


var numero = 1000;
console.log(numero);


// Tipo de dato object
var objeto = {
    nombre : "Juan", 
    apellido : "Perez", 
    telefono : "55443322"
}
console.log(objeto);
console.log(typeof objeto);

// Tipo de dato boolean
var bandera = true;
console.log(bandera);

var bandera = false;
console.log(typeof bandera);

// tipo de dato function
function miFuncion(){}
console.log(miFuncion);
console.log(typeof miFuncion)

//Tipo de dato Symbol
var simbolo = Symbol("mi simbolo");
console.log(simbolo);
console.log(typeof simbolo);

//Tipo clase es una function
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

//Tipo undefined 
var x;
console.log(x);
console.log(typeof x);


x = undefined;
console.log(typeof x);

// null = ausencia de valor
var y=null;
console.log(y);
console.log(typeof y);


//tipo Arreglos 
var autos = ['BMW', 'Audi', 'Volvo'];
console.log(autos);  
console.log(typeof autos)

// Tipo cadena vacia 
var z = ''
console.log(z);
console.log(typeof z)

