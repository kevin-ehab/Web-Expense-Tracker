const login = document.getElementById('login')
const signUp = document.getElementById('signup')
const options = document.getElementById('options')
const logout = document.getElementById('logout')
if (localStorage.getItem('state') === 'logged'){
    options.style.display = 'block'
    logout.style.display = 'block'
    localStorage.setItem('state', 'unlogged')
}
login.addEventListener('click', function(){
    window.location = '/login'
})
signUp.addEventListener('click', function(){
    window.location = '/signup'
})
options.addEventListener('click' ,function(){
    window.location = '/options'
    localStorage.setItem('state', 'logged')
})
logout.addEventListener('click', function(){
    localStorage.setItem('state', 'unlogged')
    options.style.display = 'none'
    logout.style.display = 'none'
    alert('Logged out successfully')
})