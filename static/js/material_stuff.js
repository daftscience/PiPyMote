function cleanSource(a){var b=a.split(/\n/);b.shift(),b.splice(-1,1);var c=b[0].length-b[0].trim().length,d=new RegExp(" {"+c+"}");return b=b.map(function(a){return a.match(d)&&(a=a.substring(c)),a}),b=b.join("\n")}window.page=window.location.hash||"#about",$(document).ready(function(){"#about"!=window.page&&$(".menu").find("li[data-target="+window.page+"]").trigger("click")}),$(window).on("resize",function(){$("html, body").height($(window).height()),$(".main, .menu").height($(window).height()-$(".header-panel").outerHeight()),$(".pages").height($(window).height())}).trigger("resize"),$(".menu li").click(function(){if($(this).data("target")&&!$(this).is(".active")){$(".menu li").not($(this)).removeClass("active"),$(".page").not(a).removeClass("active").hide(),window.page=$(this).data("target");var a=$(window.page);window.location.hash=window.page,$(this).addClass("active"),a.show();var b=setInterval(function(){$(".pages").animate({scrollTop:0},0)},1);setTimeout(function(){a.addClass("active"),setTimeout(function(){clearInterval(b)},1e3)},100)}}),$("#opensource").click(function(){$.get(window.location.href,function(a){var b=$(a).find(window.page).html();b=cleanSource(b),$("#source-modal pre").text(b),$("#source-modal").modal()})});