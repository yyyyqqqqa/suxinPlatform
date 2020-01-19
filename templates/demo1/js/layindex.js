$(function () {
    getMenuData();
    $(".icon_menu").click(function () {
        laySwitch();
    });
    menuShowOrHide();
    //window.onresize=menuShowOrHide;
    $(window).resize(function () {
        //延迟执行,防止多次触发
        setTimeout(function () {
            menuShowOrHide();
        }, 100);
    });
});

//获取所有菜单数据 			
function getMenuData() {
    var data =
        "<div class=\"list-group\">" +
        "<h1 title=\"导航1\"><img src=\"nav/home.png\"></h1>" +
        "<div class=\"list-wrap\">" +
        "<h2>站点管理1<i></i></h2>" +
        "<ul>" +
        "<li>" +
        "<a navid=\"channel_main\">" +
        "<span>默认站点1</span>" +
        "</a>" +
        "<ul>" +
        "<li><a navhref=\"others/1.html\" navid=\"channel_main1\"><span>站点1</span></a></li>" +
        "<li><a navhref=\"others/2.html\" navid=\"channel_main2\"><span>站点2</span></a></li>" +
        "<li><a navhref=\"others/3.html\" navid=\"channel_main3\"><span>站点3</span></a></li>" +
        "</ul>" +
        "</li>" +
        "<li>" +
        "<a navid=\"channel_2main\">" +
        "<span>默认站点2</span>" +
        "</a>" +
        "<ul>" +
        "<li><a navhref=\"others/4.html\" navid=\"channel_2main1\"><span>站点4</span></a></li>" +
        "<li><a navhref=\"others/5.html\" navid=\"channel_2main2\"><span>站点5</span></a></li>" +
        "<li><a navhref=\"others/6.html\" navid=\"channel_2main3\"><span>站点6</span></a></li>" +
        "</ul>" +
        "</li>" +
        "</ul>" +
        "</div>" +
        "</div>" +
        "<div class=\"list-group\">" +
        "<h1 title=\"导航2\"><img src=\"nav/pus.png\"></h1>" +
        "<div class=\"list-wrap\">" +
        "<h2>测试数据<i></i></h2>" +
        "<ul>" +
        "<li>" +
        "<a navid=\"channel_3main\">" +
        "<span>测试数据</span>" +
        "</a>" +
        "<ul>" +
        "<li><a><span>站点1</span></a></li>" +
        "<li><a href=\"http://www.qq.com.cn\" target=\"ifr\" navid=\"channel_3main2\"><span>站点2</span></a></li>" +
        "<li><a><span>站点3</span></a></li>" +
        "</ul>" +
        "</li>" +
        "</ul>" +
        "</div>" +
        "</div>";

    $("#sidebar-nav").html(data);

    initMenu();
}

//初始化导航菜单
function initMenu() {
    var navGroupObj = $("#sidebar-nav .list-group");
    navGroupObj.each(function (index) {
        var navHtml;
        if (index == 0) {
            navHtml = $("<li>" + $(this).children("h1").attr("title") + "</li>").appendTo($(".main-nav ul"));
            $(this).children("h1").addClass("selected");
            $(this).show();
        } else {
            navHtml = $("<li>" + $(this).children("h1").attr("title") + "</li>").appendTo($(".main-nav ul"));
        }

        navHtml.click(function () { //导航栏点击事件
            $(this).parent().children("li").removeClass("selected");
            $(this).addClass("selected");
            navGroupObj.hide();
            navGroupObj.eq($(".main-nav ul").children("li").index($(this))).show();
        });
        //隐藏所有的url
        $(this).find("ul").hide();

        $(this).find("ul").each(function (i) {
            $(this).children("li").each(function (j) {
                if ($(this).children("ul").length > 0) //有子节点
                {
                    $(this).children("a").append("<b class=\"expandable close\"></b>");
                    $(this).children("a").addClass("icon folder");
                    $(this).children("a").click(function () {
                        if ($(this).children(".expandable").hasClass("open")) {
                            $(this).children(".expandable").removeClass("open");
                            $(this).children(".expandable").addClass("close");
                            $(this).parent().children("ul").slideUp(300);
                        } else {
                            $(this).children(".expandable").removeClass("close");
                            $(this).children(".expandable").addClass("open");
                            $(this).parent().children("ul").slideDown(300);
                        }
                    });
                    $(this).children("a").children("span").before("<b class=\"icon folder\"></b>");

                    if ($(this).parent().parent().children("a").length > 0) {
                        $(this).children("a").children(".icon").css("marginLeft", parseInt($(this).parent().parent().children("a").children(".icon").css("marginLeft")) + 16);
                    } else {
                        $(this).children("a").children(".icon").css("marginLeft", 0)
                    }

                } else //无子节点
                {
                    $(this).children("a").children("span").before("<b class=\"icon file\"></b>");

                    $(this).children("a").click(function () {
                        navGroupObj.find("ul li a").removeClass("selected");
                        $(this).addClass("selected");

                        if ($('.navtab #' + $(this).attr("navid")).length > 0) { //已经存在
                            $('.navtab #' + $(this).attr("navid")).trigger('click');
                        } else {
                            var navtabLi = '<li onclick="navLiClick(this)" id="' + $(this).attr("navid") + '"><a><span>' + $(this).children('span').html() + '</span></a><i class="btni"></i></li>';

                            var frameHtml = '<iframe class="main_frame" id="' + $(this).attr("navid") + '" frameborder="0" src="' + $(this).attr("navhref") + '"></iframe>';

                            $('.navtab').append(navtabLi);
                            $('.navtab').children('li').removeClass('active');
                            $('.navtab').children('li:last-child').addClass('active');

                            $('.navContain iframe').removeClass('active');
                            $('.navContain').append(frameHtml);
                            $('.navContain').children('iframe:last-child').addClass('active');
                        }


                        $(".btni").off().on("click", function (event) {
                            event.stopPropagation(); //禁止外面div事件
                            var parent = $(this).parent();
                            var id = parent.attr("id");
                            var prev_id = parent.prev().attr("id");

                            if (parent.hasClass("active")) { //判断关闭的是否为当前页面
                                parent.prev().addClass("active");
                                $(".navContain iframe").removeClass('active');
                                if (prev_id == "home") {
                                    $(".navContain #first").addClass('active');
                                } else {
                                    $(".navContain #" + prev_id).addClass('active');
                                }
                            }
                            parent.remove();
                            $(".navContain #" + id).remove();
                        });

                        //禁用浏览器自身的鼠标右键事件
                        var navtab = document.getElementById('menuTab');
                        navtab.oncontextmenu = function () {
                            return false;
                        }

                        $(".navtab li").off().on("mousedown", function (e) {
                            var obj = this;
                            var id = $(obj).attr("id");
                            if (id == "home") {
                                return false;
                            }
                            setTimeout(function () {
                                if (3 == e.which) { //鼠标右击
                                    var navul = $(".main-container .closetab");
                                    navul.css({
                                        display: "block",
                                        top: 27,
                                        left: $(obj).context.offsetLeft + $(obj).width() / 2 - 10
                                    });
                                    navul.html("<li><a href=\"javascript:void(0)\" onclick=\"closethis(\'" + id + "\')\">关闭当前</a></li><li><a href=\"javascript:void(0)\" onclick=\"closeother(\'" + id + "\')\">关闭其他</a></li><li><a href=\"javascript:void(0)\" onclick=\"closeall()\">关闭全部</a></li>");
                                    navul.on("mouseleave", function () {
                                        $(this).css("display", "none");
                                    })
                                }
                            }, 300);
                        })


                        //保存到cookie
                        if (typeof ($(this).attr("navid")) != "undefined") {
                            addCookie("dt_manage_navigation_cookie", $(this).attr("navid"), 240);
                        }
                    });

                    if ($(this).parent().parent().children("a").length > 0) {
                        $(this).children("a").children(".icon").css("marginLeft", parseInt($(this).parent().parent().children("a").children(".icon").css("marginLeft")) + 16);
                    } else {
                        $(this).children("a").children(".icon").css("marginLeft", 0);
                    }
                }
            });
            if (i == 0) {
                $(this).show();
                if ($(this).children("li").first().children("ul").length > 0) {
                    $(this).children("li").first().children("a").children(".expandable").removeClass("close");
                    $(this).children("li").first().children("a").children(".expandable").addClass("open");
                    $(this).children("li").first().children("ul").show();
                }
            }
        });

    });
    //定位或跳转到相应的菜单
    linkMenuTree(true);
}

function navLiClick(obj) {
    $(".navContain iframe").removeClass('active');
    var id = $(obj).attr("id");
    if (id == "home") {
        $(".navContain #first").addClass('active');
    } else {
        $(".navContain #" + id).addClass('active');
    }

    $(obj).siblings().removeClass("active");
    $(obj).addClass("active");
}

//关闭当前
function closethis(id) {
    var navli = $(".navtab #" + id);
    var prev_id = navli.prev().attr("id");

    if (navli.hasClass("active")) { //判断关闭的是否为当前页面
        navli.prev().addClass("active");
        $(".navContain iframe").removeClass('active');
        if (prev_id == 'home') {
            $(".navContain #first").addClass('active');
        } else {
            $(".navContain #" + prev_id).addClass('active');
        }
    }
    navli.remove();
    $(".navContain #" + id).remove();
    $(".mainContain .closetab").css("display", "none");
}
//关闭其他
function closeother(id) {
    $(".navContain iframe").each(function (i) {
        if ($(this).attr("id") != id && $(this).attr("id") != "first") {
            $(this).remove();
        }
    });
    $(".navtab li").each(function (j) {
        if ($(this).attr("id") != id && $(this).attr("id") != "home") {
            $(this).remove();
        }
    });
    $(".navtab li").removeClass("active");
    $(".navtab #" + id).addClass("active");
    $(".navContain iframe").removeClass('active');
    $(".navContain #" + prev_id).addClass('active');
    $(".main-container .closetab").css("display", "none");
}
//关闭所有
function closeall() {
    $(".navContain iframe").each(function (i) {
        if ($(this).attr("id") != "first") {
            $(this).remove();
        }
    });
    $(".navtab li").each(function (j) {
        if ($(this).attr("id") != "home") {
            $(this).remove();
        }
    });
    $(".navtab #home").removeClass("active");
    $(".navtab #home").addClass("active");
    $(".navContain #first").addClass('active');
    $(".main-container .closetab").css("display", "none");
}

//页面布局切换
function laySwitch() {
    $("body").toggleClass("laymini"); //这个设置也很有学问，可以改变了很多东西的样式。
}

//隐藏、显示菜单
function menuShowOrHide() {
    var wid = parseInt($(window).width());
    if (wid < 800) {
        $("body").addClass("laymini");
    } else {
        $("body").removeClass("laymini");
    }
}

//定位或跳转到相应的菜单
function linkMenuTree(islink, navid) {
    var navObj = $("#main-nav");
    var navGroupObj = $("#sidebar-nav .list-group");
    var navItemObj = $("#sidebar-nav .list-group .list-wrap");

    //读取Cookie,如果存在该ID则定位到对应的导航
    var cookieObj;
    var argument = arguments.length;
    if (argument == 2) {
        cookieObj = navGroupObj.find('a[navid="' + navid + '"]');
    } else {
        cookieObj = navGroupObj.find('a[navid="' + getCookie("dt_manage_navigation_cookie") + '"]');
        //getCookie为其他js文件里面的方法，可以互相引用
    }
    if (cookieObj.length > 0) {
        //显示所在的导航和组
        //删除所有的选中样式
        navGroupObj.find("ul li a").removeClass("selected");
        //删除所有的list-group选中样式
        navGroupObj.removeClass("selected");
        //删除所有的main-nav选中样式
        navObj.children("a").removeClass("selected");
        //自身添加样式
        cookieObj.addClass("selected");
        //设置父list-group选中样式
        cookieObj.parents(".list-group").addClass("selected");
        //设置父main-nav选中样式
        navObj.children("a").eq(navGroupObj.index(cookieObj.parents(".list-group"))).addClass("selected");
        //隐藏所有的list-group
        navGroupObj.hide();
        //显示自己的父list-group
        cookieObj.parents(".list-group").show();
        //遍历所有的LI父节点
        cookieObj.parents("li").each(function () {
            //搜索所有同级LI且有子菜单的右图标为+号及隐藏子菜单
            $(this).siblings().each(function () {
                if ($(this).children("ul").length > 0) {
                    //设置自身的右图标为+号
                    $(this).children("a").children(".expandable").removeClass("open");
                    $(this).children("a").children(".expandable").addClass("close");
                    //隐藏自身子菜单
                    $(this).children("ul").hide();
                }
            });
            //设置自身的右图标为-号
            if ($(this).children("ul").length > 0) {
                $(this).children("a").children(".expandable").removeClass("close");
                $(this).children("a").children(".expandable").addClass("open");
            }
            //显示自身的UL
            $(this).children("ul").show();
        });
        //检查是否需要保存到cookie
        if (argument == 2) {
            addCookie("dt_manage_navigation_cookie", navid, 240);
        }
        //检查是否需要跳转链接
        if (islink == true && cookieObj.attr("href") != "" && cookieObj.attr("href") != "#") {
            frames["ifr"].location.href = cookieObj.attr("href");
        }
    } else if (argument == 2) {
        //删除所有的选中样式
        navGroupObj.find("ul li a").removeClass("selected");
        //保存到cookie
        addCookie("dt_manage_navigation_cookie", "", 240);
    }
}
