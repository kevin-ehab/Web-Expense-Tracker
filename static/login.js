function login(){
    const account = document.getElementById('account').value
    const password = document.getElementById('password').value
    fetch('/login2', {
        method : "POST",
        headers : { "Content-Type": "application/json" },
        body: JSON.stringify({ account , password})
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message)
        if (data.redirect){
            window.location = '/options'
            localStorage.setItem('state', 'logged')
        }
    })
}
function home(){
    window.location = '/'
}