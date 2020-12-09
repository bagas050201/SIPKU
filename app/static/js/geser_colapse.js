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