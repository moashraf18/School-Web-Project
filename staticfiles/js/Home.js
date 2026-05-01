window.addEventListener("DOMContentLoaded", function () {
    let mycurrentuser = JSON.parse(localStorage.getItem("isloggedin"));

    if (mycurrentuser && mycurrentuser.username) {
        let Welcomemessage = document.querySelector(".welcome h1");
        if (Welcomemessage) {
            Welcomemessage.textContent = `Welcome to our website, ${mycurrentuser.username}!`;
        }


        let mynavbar1 = document.querySelector(".navbar1 ul");
        if (mynavbar1) {
            mynavbar1.innerHTML = `
                <li><a href="index.html">Home</a></li>
                <li><a href="Teacher dashboard.html">Teacher</a></li>
                <li><a href="Admin dashboard.html">Admin</a></li>
                <li><a href="Lougout.html">Logout</a></li>
            `;
        }
    }
});


