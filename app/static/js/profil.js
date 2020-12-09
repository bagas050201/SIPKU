$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});

function geser_navbar(){
    document.getElementsByClassName("dropdown").style.marginLeft = "1000px";
    document.getElementsByClassName("breadcrumb").style.paddingRight = "1000px";
    console.log("terklik")
}

//image preview disini
let loadFile = function(event) {
let output = document.getElementById('output-image-profil');
output.src = URL.createObjectURL(event.target.files[0]);
output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
}
};