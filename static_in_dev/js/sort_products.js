$(document).ready(function () {

    $('select.sort').change(function () {

        var items = $('.products__item.category-products__item');
        var sort_type = $(this).children("option:selected").val();

        if (sort_type == 'За зростанням ціни') {

            items.sort(function (a, b) {

                var contentA = parseInt($(a).attr('price'));
                var contentB = parseInt($(b).attr('price'));
                return (contentA < contentB) ? -1 : (contentA > contentB) ? 1 : 0;
            });
        }
        else if (sort_type == 'За спаданням ціни') {

            items.sort(function (a, b) {

                var contentA = parseInt($(a).attr('price'));
                var contentB = parseInt($(b).attr('price'));
                return (contentA > contentB) ? -1 : (contentA < contentB) ? 1 : 0;
            });
        }
        else if (sort_type == 'За назвою') {

            items.sort(function (a, b) {

                var contentA = $(a).attr('name');
                var contentB = $(b).attr('name');
                return (contentA < contentB) ? -1 : (contentA > contentB) ? 1 : 0;
            });
        }

        $('.products').html(items);

    })

})