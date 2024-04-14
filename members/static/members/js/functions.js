function showPass() {
    var x = document.getElementById("id_password1");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}