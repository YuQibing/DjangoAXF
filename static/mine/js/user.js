/**
 * Created by yuqibing on 28/09/2017.
 */
$(function () {
    $('#userAccount').change(function () {
        var account = $(this).val();
        var url = 'http://127.0.0.1:8000/axf/checkaccount/';
        $.get(url, {'account': account}, function (result) {
            $('#status').html(result.status);
        });
    });
});