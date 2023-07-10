for(let valor = 0; valor <= 10; valor++){
    if (valor%2 !== 0){
        console.log(valor);
        // break; // rompe la iteración
        continue; //continua con la iteración
    }
    else{
        // continue
        console.log(valor)
    }
}