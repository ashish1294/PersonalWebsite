//  Responsive Accordion v1.3, Copyright 2014, Joe Mottershaw, https://github.com/joemottershaw/
//  ============================================================================================
    var value = 0;
    $(document).ready(function() {
        $('.responsive-accordion').each(function() {
            // Set Expand/Collapse Icons
                $('.responsive-accordion-minus', this).hide();

            // Hide panels
                $('.responsive-accordion-panel', this).hide();

            // Bind the click event handler
                $('.responsive-accordion-head', this).click(function(e) {
                    // Get elements
                        var thisAccordion = $(this).parent().parent(),
                            thisHead = $(this),
                            thisPlus = thisHead.find('.responsive-accordion-plus'),
                            thisMinus = thisHead.find('.responsive-accordion-minus'),
                            thisPanel = thisHead.siblings('.responsive-accordion-panel');
                            thisli = thisHead.parent();
                            thisarrow = thisHead.find('.arrow');

                    // Reset all plus/mins symbols on all headers
                        //thisAccordion.find('.responsive-accordion-plus').show();
                        //thisAccordion.find('.responsive-accordion-minus').hide();

                    // Reset all head/panels active statuses except for current
                        //thisAccordion.find('.responsive-accordion-head').not(this).removeClass('active');
                        //thisAccordion.find('.responsive-accordion-panel').not(this).removeClass('active').slideUp();

                    // Toggle current head/panel active statuses
                        if (thisHead.hasClass('active')) {
                            thisHead.removeClass('active');
                            //thisPlus.show();
                            //thisMinus.hide();
                            thisPanel.removeClass('active').slideUp();
                            thisli.removeClass('active');
                            value = 0;

                        } else {
                            thisHead.addClass('active');
                            //thisPlus.show();
                            //thisPlus.hide();
                            //thisMinus.show();
                            thisPanel.addClass('active').slideDown();
                            thisli.addClass('active');
                            value = 90;
                        }
                        var rotate = "rotate(" + value + "deg)";
                        var trans = "all 0.4s ease-out";
                        thisarrow.css({
                            "-webkit-transform": rotate,
                            "-moz-transform": rotate,
                            "-o-transform": rotate,
                            "msTransform": rotate,
                            "transform": rotate,
                            "-webkit-transition": trans,
                            "-moz-transition": trans,
                            "-o-transition": trans,
                            "transition": trans
                        });
                });
        });
    });
