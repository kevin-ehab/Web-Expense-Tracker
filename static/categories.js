function home(){
    window.location = '/'
}

const submit = document.getElementById('submit')
submit.addEventListener('click', function(){
    let food = document.getElementById('food').value
    let transportation = document.getElementById('transportation').value
    let shopping = document.getElementById('shopping').value
    let bills = document.getElementById('bills').value
    let entertainment = document.getElementById('entertainment').value
    let healthcare = document.getElementById('healthcare').value
    fetch('/categories2', {
        method : "POST",
        headers : { "Content-Type": "application/json" },
        body: JSON.stringify({food,transportation,shopping,bills,entertainment,healthcare})
    })
    .then(res=>res.json())
    .then(data=> {
        alert(data.message)
        if (data.redirect){
            window.location = '/options'
        }
    })
})