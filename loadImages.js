document.addEventListener("DOMContentLoaded", function(event) {
    loadFeaturedImage();
    loadDEyeLogo();
});

featuredImgSrc = "images/featuredImage.jpg"
dEyeLogoImg = "images/DEyeLogoWhite.png"

function loadFeaturedImage() {
    var featuredImage = document.getElementById("featured-image");
    featuredImage.setAttribute("class", "featured-image");
    featuredImage.setAttribute("src", featuredImgSrc);
    console.log("Done loading featured image.");
}

function loadDEyeLogo() {
    var dEyeLogo = document.getElementById("deye-logo");
    dEyeLogo.setAttribute("class", "dEyeLogo");
    dEyeLogo.setAttribute("src", dEyeLogoImg);
}
