function voto(){
    var canAP = document.getElementById("candidatoA");
    var canBP = document.getElementById("candidatoB");
    var canCP = document.getElementById("candidatoC");
    var canDP = document.getElementById("candidatoD");

    arrP=[canAP.value,canBP.value,canCP.value,canDP.value];
    arrP.forEach(element => console.log(element));
    
    var arrayLength = arrP.length;
    
    for (var i = 0; i < arrayLength; i++) {
        if(arrP[i] == "-"){
            error(1);
            return
        }
    }

    if (hasDuplicates(arrP)){
        error(2);
        return;
    }

    localStorage.setItem("array", JSON.stringify(arrP));
    window.location.href = "sure.html";
}

function error(num){
    console.log("ERROR");
    var ins = document.getElementById("INS");
    ins.style.color = "red";
    ins.style.fontWeight = "bolder";

    if (num == 1){
        ins.innerHTML = "No puedes dejar espacios vacios";
        
    }
    else if (num == 2){
        ins.innerHTML = "No se puede repetir las opciones";
    }
}


function hasDuplicates(array) {
    var valuesSoFar = [];
    for (var i = 0; i < array.length; ++i) {
        var value = array[i];
        if (valuesSoFar.indexOf(value) !== -1) {
            return true;
        }
        valuesSoFar.push(value);
    }
    return false;
}

