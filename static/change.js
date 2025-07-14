function home(){
  window.location = '/'
}
const incomeCheckbox = document.getElementById('income')
const incomeEnt = document.getElementById('income-ent')
const savingCheckbox = document.getElementById('saving')
const savingEnt = document.getElementById('saving-ent')
function income_checkbox_click(){
  if (incomeCheckbox.checked){
    incomeEnt.style.display = 'block'
  }else{
    incomeEnt.style.display = 'none'
  }
}
incomeCheckbox.addEventListener('change', income_checkbox_click)
function saving_checkbox_click(){
  if (savingCheckbox.checked){
    savingEnt.style.display = 'block'
  }else{
    savingEnt.style.display = 'none'
  }
}
savingCheckbox.addEventListener('change', saving_checkbox_click)
function submit(){
    const income = incomeEnt.value
    const saving = savingEnt.value
    fetch('/change2', {
            method : "POST",
            headers : { "Content-Type": "application/json" },
            body: JSON.stringify({income, saving})
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