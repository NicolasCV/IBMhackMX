
var textArea = document.getElementById("inputT");
var ticketLabel = document.getElementById("TL");
var lengthCode = 5;

function enter(){
    goAhead = false;
    inputy=textArea.value;
    console.log(inputy);
    console.log(inputy.length);
    
    if (inputy == "" || inputy.length <= 0 || inputy.length > lengthCode){
        console.log("INVALID")
        ticketLabel.style.color = "red";
        ticketLabel.innerHTML = "Ticket Votante Invalido";
    }
    else{
        goAhead = true;
    }


    if(goAhead){
        window.location.href = "huella.html";
    }

}
