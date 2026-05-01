window.addEventListener("DOMContentLoaded" , function(){

    localStorage.removeItem("isloggedin");

    setTimeout(function(){
        window.location.href = "index.html";
    } , 4000); // redirect the user to home page after 4 seconds

});