function goBack() {
    window.history.back();
}

// Collection edit
function editFunction() {
    const x = document.getElementById("show-hide");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

// Collection-item edit
function itemEditFunction() {
    const z = document.getElementById("show-hide-item");
    if (z.style.display === "none") {
        z.style.display = "block";
    } else {
        z.style.display = "none";
    }
}


// dashboard-login-info
function infoFunction() {
    const y = document.getElementById("user-info");
    if (y.style.display === "none") {
        y.style.display = "block";
    } else {
        y.style.display = "none";
    }
}