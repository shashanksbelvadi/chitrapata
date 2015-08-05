document.addEventListener("DOMContentLoaded", function(event) {
    loadFeaturedImages();
    loadDEyeLogo();
});

featuredImgSrc = "images/featuredImage.jpg";
fI2 = "images/tamalpaisSunset.jpg";
dEyeLogoImg = "images/DEyeLogoWhite.png"

function loadFeaturedImages() {
    var featuredImage = document.getElementById("featured-image");
    var featuredImages = [featuredImgSrc, fI2];

    var i = 0;
    loadFeaturedImage(featuredImage, featuredImages[i]);

    setInterval(function() {
        setTimeout(function() {
            removeFeaturedImage(featuredImage);
            loadFeaturedImage(featuredImage, featuredImages[i]);
        }, 5000);

        i++;
        if (i == featuredImages.length) {
            i = 0;
        }
    }, 10000);
}

function removeFeaturedImage(featuredImage) {
    featuredImage.removeAttribute("src");
}

function loadFeaturedImage(featuredImage, imageSrcPath) {
    featuredImage.setAttribute("class", "featured-image");
    featuredImage.setAttribute("src", imageSrcPath);
    console.log("Done loading featured image.");
}

function loadDEyeLogo() {
    var dEyeLogo = document.getElementById("deye-logo");
    dEyeLogo.setAttribute("class", "dEyeLogo");
    dEyeLogo.setAttribute("src", dEyeLogoImg);
}
