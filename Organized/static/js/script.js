
document.getElementById('imageInput').addEventListener('change', function(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('inputImage');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
});
    