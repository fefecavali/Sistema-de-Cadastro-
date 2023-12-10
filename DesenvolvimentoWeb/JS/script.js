
function verifica_cadastro() {
    var name_user = document.getElementById("name").value;
    var date_user = document.getElementById("date").value;
    var email_user = document.getElementById("email").value;
    var password_user = document.getElementById("password").value;

    if (name_user === "" || date_user === "" || email_user === "" || password_user === "") {
        alert("Por favor preencha os campos corretamente!")
        return;
        }
    }


function verifica_login() {
    var email_user = document.getElementById("email").value;
    var password_user = document.getElementById("password").value;

    if (email_user === "" || password_user === "") {
        alert("Por favor preencha os campos corretamente!")
        return;
        }
    }
