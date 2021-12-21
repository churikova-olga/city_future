$('div.catalog_block_link a').each(function () {
                $(this).hover(
                    function () {
                        $('div.catalog_block_img').addClass('hover_img');
                    },
                    function () {
                        $('div.catalog_block_img').removeClass('hover_img');
                    });
            });
/*Открытие формы Регистрации*/
//Функция показа
function showReg(state){
    document.getElementById('window_reg').style.display = state;    
    document.getElementById('gray').style.display = state;
    }   
/*Открытие формы Входа*/
function showVhod(e){
    document.getElementById('window_vhod').style.display = e;    
    document.getElementById('gray').style.display = e; 
    }
//Закрытие одной формы открытие другой



/*Слайдер Баннер в хедере*/
 jQuery(document).ready(function ($) {

            var jssor_1_options = {
              $AutoPlay: 1,
              $ArrowNavigatorOptions: {
                $Class: $JssorArrowNavigator$
              },
              $BulletNavigatorOptions: {
                $Class: $JssorBulletNavigator$,
                $SpacingX: 16,
                $SpacingY: 16
              }
            };

            var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);

            /*#region responsive code begin*/

            var MAX_WIDTH = 810;

            function ScaleSlider() {
                var containerElement = jssor_1_slider.$Elmt.parentNode;
                var containerWidth = containerElement.clientWidth;

                if (containerWidth) {

                    var expectedWidth = Math.min(MAX_WIDTH || containerWidth, containerWidth);

                    jssor_1_slider.$ScaleWidth(expectedWidth);
                }
                else {
                    window.setTimeout(ScaleSlider, 30);
                }
            }

            ScaleSlider();

            $(window).bind("load", ScaleSlider);
            $(window).bind("resize", ScaleSlider);
            $(window).bind("orientationchange", ScaleSlider);
            /*#endregion responsive code end*/
        });
/*Слайдер акции*/
    jQuery(document).ready(function ($) {

            var jssor_2_options = {
              $AutoPlay: 1,
              $SlideWidth: 240,
              $SlideSpacing: 40,
              $Align: 0,
              $ArrowNavigatorOptions: {
                $Class: $JssorArrowNavigator$
              }
            };

            var jssor_2_options = new $JssorSlider$("jssor_2", jssor_2_options);

            /*#region responsive code begin*/

            var MAX_WIDTH2 = 3000;

            function ScaleSlider2() {
                var containerElement2 = jssor_2_options.$Elmt.parentNode;
                var containerWidth2 = containerElement2.clientWidth;

                if (containerWidth2) {

                    var expectedWidth2 = Math.min(MAX_WIDTH2 || containerWidth2, containerWidth2);

                    jssor_2_options.$ScaleWidth(expectedWidth2);
                }
                else {
                    window.setTimeout(ScaleSlider2, 30);
                }
            }

            ScaleSlider2();

            $(window).bind("load", ScaleSlider2);
            $(window).bind("resize", ScaleSlider2);
            $(window).bind("orientationchange", ScaleSlider2);
            /*#endregion responsive code end*/
        });
/*Слайдер популярное*/
 jQuery(document).ready(function ($) {

            var jssor_3_options = {
              $AutoPlay: 1,
              $SlideWidth: 240,
              $SlideSpacing: 40,
              $Align: 0,
              $ArrowNavigatorOptions: {
                $Class: $JssorArrowNavigator$
              }
            };

            var jssor_3_options = new $JssorSlider$("jssor_3", jssor_3_options);

            /*#region responsive code begin*/

            var MAX_WIDTH3 = 3000;

            function ScaleSlider3() {
                var containerElement3 = jssor_3_options.$Elmt.parentNode;
                var containerWidth3 = containerElement3.clientWidth;

                if (containerWidth3) {

                    var expectedWidth3 = Math.min(MAX_WIDTH3 || containerWidth3, containerWidth3);

                    jssor_3_options.$ScaleWidth(expectedWidth3);
                }
                else {
                    window.setTimeout(ScaleSlider3, 30);
                }
            }

            ScaleSlider3();

            $(window).bind("load", ScaleSlider3);
            $(window).bind("resize", ScaleSlider3);
            $(window).bind("orientationchange", ScaleSlider3);
            /*#endregion responsive code end*/
        });
  jQuery(document).ready(function ($) {

            var jssor_4_options = {
              $AutoPlay: 1,
              $SlideWidth: 240,
              $SlideSpacing: 40,
              $Align: 0,
              $ArrowNavigatorOptions: {
                $Class: $JssorArrowNavigator$
              }
            };

            var jssor_4_options = new $JssorSlider$("jssor_4", jssor_4_options);

            /*#region responsive code begin*/

            var MAX_WIDTH4 = 3000;

            function ScaleSlider4() {
                var containerElement4 = jssor_4_options.$Elmt.parentNode;
                var containerWidth4 = containerElement4.clientWidth;

                if (containerWidth4) {

                    var expectedWidth4 = Math.min(MAX_WIDTH4 || containerWidth4, containerWidth4);

                    jssor_4_options.$ScaleWidth(expectedWidth4);
                }
                else {
                    window.setTimeout(ScaleSlider4, 30);
                }
            }

            ScaleSlider4();

            $(window).bind("load", ScaleSlider4);
            $(window).bind("resize", ScaleSlider4);
            $(window).bind("orientationchange", ScaleSlider4);
            /*#endregion responsive code end*/
        });