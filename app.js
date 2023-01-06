// rolls number between 1 and 6
function roll() {
    let x = Math.floor(Math.random() * 6 + 1);
    let n = document.getElementById("n");
    n.innerHTML = x;

};




function plusSides() {
let s = document.getElementById("count");
console.log(s.innerHTML)
s.innerHTML = parseInt(s.innerHTML) + 1;

};


function minusSides() {
    let s = document.getElementById("count");
    if (s.innerHTML == 0) {
        s.innerHTML = 0;
    } else {
        s.innerHTML = parseInt(s.innerHTML) - 1;
    }
    };

function confirmSides() {
document.getElementById("minus").hidden=true;
document.getElementById("plus").hidden=true;
document.getElementById("confirmsides").hidden=true;
document.getElementById("howmanysides").hidden=true;
document.getElementsByClassName("dice").hidden=false;
}