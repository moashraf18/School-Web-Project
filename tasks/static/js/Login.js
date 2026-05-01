document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("signup-form").addEventListener("submit", function(event) {
        event.preventDefault();

        let username1 = document.getElementById("login-username").value.trim();
        let password1 = document.getElementById("login-password").value.trim();

        if (username1 === "" || password1 === "") {
            alert("Please fill in all the required fields.");
            return;
        }

        this.submit(); 
    });
});