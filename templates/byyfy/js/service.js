/**
 * Created by Andy on 2016/11/20.
 */
function getData(url1, params,retFunc) {
    url1 = 'http://127.0.0.1/bg/bg/' + url1 + '.do';
    var retData = {};
    $.ajax({
        url: url1,
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

function getData11(url1, params) {
    url1 = 'http://127.0.0.1/bg1/bg/' + url1 + '.do';
    var retData = {};
    $.ajax({
        url: url1,
        data: params,
        async: false,
        dataType: 'json',
        cache: false,
        success: function (data, textStatus, jqXHR) {
            retData = data;
            //retFfunc.success(data);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            retData["code"]='99';
            retData["msg"]='网络不通!!';
            retData = errorThrown;
        },
        complete: function (jqXHR, textStatus) {

        }
    });
    return retData;
}