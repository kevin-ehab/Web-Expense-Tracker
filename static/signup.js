function signUp(){
    const account = document.getElementById('account').value
    const password = document.getElementById('password').value
    const saving = document.getElementById('saving').value
    const income = document.getElementById('income').value
    fetch('/signup2', {
        method: ['Post'],
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({account, password, income, saving })
    })
    .then(res => res.json())
    .then(data =>{
        alert(data.message)
        if (data.redirect === 1){
            window.location = '/options'
            localStorage.setItem(state, 'logged')
        }else if (data.redirect === 2){
            window.location = '/login'
        }
    })
}
function home(){
    window.location = '/'
}