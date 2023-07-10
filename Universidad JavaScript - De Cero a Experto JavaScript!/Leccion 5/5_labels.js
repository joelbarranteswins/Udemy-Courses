inicio:
for(let valor = 0; valor <= 10; valor++){
    if (valor%2 !== 0){
        console.log(valor);
        break inicio; //continua con la iteración con la misma etiqueta
        // continue inicio
    }
    else{
        console.log(valor)
    }
}
