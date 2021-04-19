var arrayP = JSON.parse(localStorage.getItem("array"));

var dic,primer,segundo,tercero,cuarto;

function showResults(arrP){
    console.log(arrP);
    var ca = arrP[0];
    var cb = arrP[1];
    var cc = arrP[2];
    var cd = arrP[3];
    var dic = {};
    
    dic[ca] = "Candidato A";
    dic[cb] = "Candidato B";
    dic[cc] = "Candidato C";
    dic[cd] = "Candidato D";

    console.log(dic);
    console.log(dic["1er"]);
    console.log(dic["2do"]);
    console.log(dic["3ro"]);
    console.log(dic["4to"]);
    console.log(document.getElementById("1R").textContent)

    primer = document.getElementById("1R");
    segundo = document.getElementById("2R");
    tercero = document.getElementById("3R");
    cuarto = document.getElementById("4R");

    primer.textContent = dic["1er"];
    segundo.textContent = dic["2do"];
    tercero.textContent = dic["3ro"];
    cuarto.textContent = dic["4to"];

}

function cancelar(){
    window.location.href = "votar.html"
}

function confirmar(){
    window.location.href = "sent.html"
}

window.onload = showResults(arrayP)
