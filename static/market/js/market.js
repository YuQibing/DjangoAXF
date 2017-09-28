/**
 * Created by yuqibing on 26/09/2017.
 */

$(function () {
    $('.leftChildType').click(function () {
        $('#typediv').css('display', 'block')
        $('#sortdiv').css('display', 'none')
    })
    $('#typediv').click(function () {
        $('#typediv').css('display', 'none')
    })

    $('.rightOrder').click(function () {
        $('#sortdiv').css('display', 'block')
        $('#typediv').css('display', 'none')
    })
    $('#sortdiv').click(function () {
        $('#sortdiv').css('display', 'none')
    })
})
