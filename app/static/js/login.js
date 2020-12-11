function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    let charCode = (evt.which) ? evt.which : evt.keyCode;
    if ( (charCode > 31 && charCode < 48) || charCode > 57) {
        return false;
    }
    return true;
}

//modal saat lupa password
$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})

//copy text 
function copyText(element) {
    let range, selection;

    if (document.body.createTextRange) {
        range = document.body.createTextRange();
        range.moveToElementText(element);
        range.select();
    } else if (window.getSelection) {
        selection = window.getSelection();        
        range = document.createRange();
        range.selectNodeContents(element);
        selection.removeAllRanges();
        selection.addRange(range);
    }
    
    try {
        document.execCommand('copy');
        console.log(range);
        console.log(selection);
        alert('Copied the text: '+range.endContainer.attributes[0].value);
    }
    catch (err) {
        alert('unable to copy text');
    }
}