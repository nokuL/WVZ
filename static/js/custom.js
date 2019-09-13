(function($){

    $(document).ready(function(){

        $(".pagination").customPaginate({

            itemsToPaginate : ".post"

        });

    });

})(jQuery)

$('.post-wrapper').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
});