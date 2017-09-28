/**
 * Created by yuqibing on 26/09/2017.
 */

$(function () {
    $('.leftChildType').click(function () {
        $('#typediv').css('display', 'block')
    })
    $('#typediv').click(function () {
        $('#typediv').css('display', 'none')
    })

    $('.rightOrder').click(function () {
        $('#sortdiv').css('display', 'block')
    })
    $('#sortdiv').click(function () {
        $('#sortdiv').css('display', 'none')
    })
})
