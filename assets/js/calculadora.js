let costo= document.getElementById('costo')
let valor = document.getElementById('valor')
let valor2 = document.getElementById('valoriva')
let ganancia = document.getElementById('ganancia')
let precio = 0
let precio2 = 0

costo.addEventListener('input', ()=>{
    let porcentaje = ganancia.value
    let calculo = costo.value
    console.log(calculo)
    console.log(porcentaje)
    calculo=parseFloat(calculo)
    porcentaje=parseFloat(porcentaje)
    precio = calculo/(((100-porcentaje)/100))
    precio2 = (calculo*1.19)/(((100-porcentaje)/100))
    valor.value = precio
    valor2.value = precio2

})