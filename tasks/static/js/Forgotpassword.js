document.addEventListener("DOMContentLoaded", function() {
    let myform = document.querySelector("form");

    let reset_pass_input = document.getElementById("password_tow");
    let confirm_pass_input = document.getElementById("confirm_password_tow");

    myform.addEventListener("submit", function(event) {
        event.preventDefault();

        let reset_password = reset_pass_input.value.trim();
        let confirm_password = confirm_pass_input.value.trim();

        if (reset_password === "" || confirm_password === "") {
            alert("Please fill in all the required fields.");
            return;
        }

        if (reset_password !== confirm_password) {
            alert("Passwords do not match.");
            return;
        }

        this.submit(); 
    });
});