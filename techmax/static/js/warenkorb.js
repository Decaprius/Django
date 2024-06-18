let bestellenButtons = document.getElementsByClassName("warenkorb-bestellen")

for (let i = 0; i < bestellenButtons.length; i++){
    bestellenButtons[i].addEventListener('click', function(){
        let artikelID = this.dataset.artikel;
        let action = this.dataset.action;
        updateKundenBestellung(artikelID, action)
    })
}

function updateKundenBestellung(artikelID, action){
    let url = "/artikel_backend/";

    fetch(url, {
        method: 'post',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'artikelID':artikelID, 'action':action})
    })
    .then(()=>location.reload())
}

//Kasse
let formular = document.getElementById('formular')

formular.addEventListener('submit', function(e){
    e.preventDefault()
    document.getElementById('formular-button').classList.add('d-none');
    document.getElementById('bezahlen-info').classList.remove('d-none');
})

document.getElementById('bezahlen-button').addEventListener('click', function(e){
    submitFormular()
})

function submitFormular(){
    alert('Bestellung aufgegeben.')
}
