function showPass() {
    const x = document.getElementById("id_password1");

    if (x) {
        if (x.type === "password") {
            x.type = "text";
        } else {
            x.type = "password";
        }
    }

}/*
    Function which listens to the change of the profile image and displays the image
    that the user has picked on the img element.
*/
document.getElementById('image_field').addEventListener('change', function(e) {
    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('profile_image').src = e.target.result;
    }
    reader.readAsDataURL(this.files[0]);
});

