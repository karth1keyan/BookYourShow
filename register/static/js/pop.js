function redirect () {
    var interval = setInterval(myURL, 5000);
    var result = document.getElementById("result");
    
 }

 function myURL() {
    document.location.href = '';
    clearInterval(interval);
 }