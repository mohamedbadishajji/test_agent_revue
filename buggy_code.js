// Bug 1 : == au lieu de ===
function checkAge(age) {
    if (age == 18) {
        return true;
    }
}

// Bug 2 : var au lieu de let/const
var password = "admin123";

// Bug 3 : console.log oublié
console.log("debug: " + password);

// Bug 4 : Promise non gérée
function fetchData(url) {
    fetch(url)
        .then(response => response.json())
}

// Bug 5 : document.write dangereux
function displayMessage(msg) {
    document.write(msg);
}
