function showPass() {
    const x = document.getElementById("id_password1");

    if (x) {
        if (x.type === "password") {
            x.type = "text";
        } else {
            x.type = "password";
        }
    }

}

const textarea = document.querySelector("#id_bio");
textarea.addEventListener('input', autoResize, false);

function autoResize() {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
}