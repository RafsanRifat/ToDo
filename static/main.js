function goBack() {
    window.history.back();
}

function editFunction() {
    const x = document.getElementById("show-hide");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}