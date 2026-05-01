document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("signup-form").addEventListener("submit", function(event) {
        event.preventDefault();

        let username1 = document.getElementById("signup-username").value.trim();
        let password1 = document.getElementById("signup-password").value.trim();
        let cpassword1 = document.getElementById("signup-confirm-password").value.trim();
        let role = document.querySelector('input[name="role"]:checked');

        if (username1 === "" || password1 === "" || cpassword1 === "" || !role) {
            alert("Please fill in all the required fields.");
            return;
        }

        if (password1 !== cpassword1) {
            alert("Password and confirm password are not identical, try again.");
            return;
        }

        this.submit(); 
    });
});