/**
 * Created by Andy on 2016/11/20.
 */
function getData(url0, params,retFunc) {
    url0 = 'http://127.0.0.1/bg/' + url0 + '.do';
    var retData = {};
    $.ajax({
        url: url0,
        data: params,
        async: false,
        dataType: 'json',
        cache: false,
        success: function (data, textStatus, jqXHR) {
            retFunc.success(data);
            retData = data;
            //retFfunc.success(data);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            retData = errorThrown;
            retData["code"]='99';
            retData["msg"]='网络不通!!';
            retFunc.error(retData);
        },
        complete: function (jqXHR, textStatus) {
            retFunc.complete(textStatus);
        }
    });
}