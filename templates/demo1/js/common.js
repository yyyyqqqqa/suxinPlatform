//写缓存cookie
function addCookie(keyName,keyValue,hours){
	if(arguments.length>0)
	{
      var str=keyName+'='+escape(keyValue);	
      var date=new Date();
      date.setTime(date.getTime+hours*3600*1000);
      document.cookie=str+"; expire="+date.toGMTString();
	}
}

//读取缓存cookie
function getCookie(keyName){
	var arrStr=document.cookie.split("; ");
	for(var i=0;i<arrStr.length;i++)
	{
		var temp=arrStr[i].split("=");
		if(temp[0]==keyName)
		{
			return unescape(temp[1]);
		}
	}
	return "";
}












