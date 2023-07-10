class Persona{
    constructor(nombre, apellido){
        this._nombre = nombre; 
        this._apellido = apellido;
    }
    //para llamar un metodo como si fuera un atributo
    get nombre(){
        return this._nombre;
    }
    //para llamar un metodo para modificar un valor como si fuera un atributo
    set nombre(nombre){
        this._nombre = nombre;
    }
}

let persona1 = new Persona('Juan', 'Perez');
console.log( persona1.nombre );
persona1.nombre = 'Juan Carlos';//set nombre('Juan Carlos')
console.log( persona1.nombre );//get nombre