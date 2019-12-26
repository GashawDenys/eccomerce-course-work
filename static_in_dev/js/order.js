$(document).ready(function () {
    $('#div_id_address').css('display', 'none');

    $('#id_delivery_type').on('click', function () {
        var delivery_type = $(this).val();

        if (delivery_type == 'delivery') {
            $('#div_id_address').css('display', 'block');
        }
        else {
            $('#div_id_address').css('display', 'none');
        }
    })
})