/**
 * Created by yuqibing on 26/09/2017.
 */

$(function () {
    initSwiperWheel()
    initSwiperBuy()

})

function initSwiperWheel() {
    var swiperWheel = new Swiper('#topSwiper', {
        direction: 'horizontal',
        pagination: '.swiper-pagination',
        speed: 500,
        loop: true,
        autoplay: 2000,
        control: true,
    });
}

function initSwiperBuy() {
    var mySwiper2 = new Swiper('#swiperMenu', {
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 2,
        loop: false,
    });
}

