$(document).ready(function () {
    $('.add_to_cart').on('click', function (e) {
        e.preventDefault();
        var product_slug = $(this).attr('data-slug');
        var data = {
            product_slug: product_slug
        }

        $(".buy-btn.product-btn.add_to_cart").html("Товар у кошику");

        $.ajax({
            type: "GET",
            url: "/add_to_cart/",
            data: data,
            success: function (data) {
                $("#cart_count").html(data.cart_total);
            }
        })
    })

    $('.remove_from_cart').on('click', function (e) {
        e.preventDefault();
        var product_slug = $(this).attr('data-slug');
        var data = {
            product_slug: product_slug
        }

        $.ajax({
            type: "GET",
            url: "/remove_from_cart/",
            data: data,
            success: function (data) {
                $("#cart_count").html(data.cart_total);
                $("#" + product_slug).remove();
                $("#cart-total-price").html("<b>" + parseInt(data.cart_total_price) + " грн</b>");
                if (parseInt(data.cart_total) == 0) {
                    $(".cart-table").remove();
                    $(".cart-empty").css("display", "block");
                }
            }
        })
    })

    $('.cart-item-amount').on('click', function () {
        var amount = $(this).val();
        var item_id = $(this).attr('data-id');
        var data = {
            amount: amount,
            item_id: item_id
        }

        $.ajax({
            type: "GET",
            url: "/change_item_amount/",
            data: data,
            success: function (data) {
                $("#cart-item-total-" + item_id).html(parseInt(data.item_total_price) + " грн");
                $("#cart-total-price").html("<b>" + parseInt(data.cart_total_price) + " грн</b>");
            }
        })
    })


})