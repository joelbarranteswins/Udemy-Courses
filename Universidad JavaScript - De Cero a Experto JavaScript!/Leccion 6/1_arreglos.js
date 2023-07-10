//let autos = new Array('BMW','Mercedes Benz','Volvo');

const autos = ['BMW','Mercedes Benz','Volvo'];
console.log(autos);


//acceder a los elementos internos
console.log(autos[0]);
console.log(autos[2]);

for (let i = 0; i < autos.length; i++){
    console.log(i + ':' + autos[i])
}


//modificar el valor de los arreglos
autos[1] = 'Mercedes joel'
console.log(autos[1])
console.log(autos)


//agregar elemtos
autos.push('Audi');
console.log(autos)