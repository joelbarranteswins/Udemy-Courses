class Persona{
    constructor(nombre, apellido){ 
        //el constructor inicializa la clase
        this.nombre = nombre; 
        this.apellido = apellido;
    }
}

//se instancia la clase o el objeto Persona
let persona1 = new Persona('Juan', 'Perez'); //new crea un espacio en memoria
console.log( persona1 );

let persona2 = new Persona('Carlos', 'Lara');
console.log( persona2 );