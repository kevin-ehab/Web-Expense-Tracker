function home(){
    window.location = '/'
}
function categories(){
    window.location = '/categories'
}
function change(){
    window.location = '/change'
}
function generateDashboard() {
    fetch('/dashboard2')
        .then(res => res.json())
        .then(data => {
                alert(data.message);
                window.location = '/dashboard';
        })
        .catch(err => {
            console.error("Error generating dashboard:", err);
            alert("Something went wrong while generating the dashboard.");
        });
}