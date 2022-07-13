// Function to contorl navbar menu and active class
$(function () {
    $(".toggle").on("click", function () {
        if ($(".menu").hasClass("active")) {
            $(".menu").removeClass("active");
            $(this).find("a").html("<ion-icon name='menu-outline'></ion-icon>");
        } else {
            $(".menu").addClass("active");
            $(this).find("a").html("<ion-icon name='close-outline'></ion-icon>");
        }
    })
});

// Carousel Slider Function
$(document).ready(function () {
    $('.latest-project').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        responsive: [{
                breakpoint: 600,
                settings: {
                    arrows: false,
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
});

// active class for services tab.

$(document).on('click', 'ul li', function () {
    $(this).addClass('active-btn').siblings().removeClass('active-btn')
})

//info class loop to show and hide content via tab

function showInfo(index) {
    const infoSections = document.getElementsByClassName("info")
    for (i = 0; i < infoSections.length; i++) {
        infoSections[i].style.display = "none";
    }
    infoSections[index].style.display = "block";
};

$(document).ready(function () {
    $('.popup-gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
            titleSrc: function (item) {
                return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
            }
        }
    });
});