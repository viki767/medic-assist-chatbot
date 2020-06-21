
//var bot_url = "http://localhost:7777/";
var bot_url = "http://localhost:7777/chatbot";
var input = {'msg':"No_message",'previous_msg':'No_message'};


var messages = document.getElementById("messages")
//var textbox = document.getElementById("textbox")
var button = document.getElementById("button")

button.addEventListener("click",function(){
    var msg = $.trim($('#textbox').val())
    if (msg != "") {
        receive_message_html(msg); 
    }
    document.getElementById("textbox").value=""
});

var receive_message_html= function(msg) {
    var newMessages = '<div class="outgoing-chats"><div class="outgoing-chats-msg"><p id="received_msg" >'+msg +'</p><span class="time">'+timesstamp()+'</span></div><div class="outgoing-chats-img"><img src="user_img.png"></div></div>';
    $(newMessages).appendTo('.msg-page').slideDown(300,scroll_down)
    send_message_backend(msg);
}

var send_message_html= function(msg) {
    input["previous_msg"]=msg;
    var newMessages = '<div class="received-chats"><div class="received-chats-img"><img src="chatbot_image.png"></div><div class="received-msg"><div class="received-msg-inbox"><p id="messages">'+msg +'</p><span class="time">'+timesstamp()+'</span></div></div></div>';
    $(newMessages).appendTo('.msg-page').slideDown(300,scroll_down)
}

var welcome_message_html= function(msg) {
    var msg_bot = "Hi, How can i help you."
    var newMessages = '<div class="received-chats"><div class="received-chats-img"><img src="chatbot_image.png"></div><div class="received-msg"><div class="received-msg-inbox"><p id="messages">'+msg_bot +'</p><span class="time">'+timesstamp()+'</span></div></div></div>';
    $(newMessages).appendTo('.msg-page').slideDown(300,scroll_down)
}

var scroll_down = function() {
    var d = $('.msg-page');
    d.scrollTop(d.prop("scrollHeight"))
}

var timesstamp = function() {
    return (new Date()).toLocaleString();
}

var send_message_backend = function(msg) {
    input["msg"] = msg;
    //alert("ajax")
    $.ajax({
        cache: false,
        url: bot_url + "?" + serialize(input),
        success: function(result) {
            //alert(result.res)
            send_message_html(result.res)
        },
        error: function(rest1) {
            //alert("error");
        }
    })
}

var serialize = function(obj) {
    var str=[];
    for (var p in  obj)
        if (obj.hasOwnProperty(p) && obj[p] != '') {
            str.push(encodeURIComponent(p)+ "=" + encodeURIComponent(obj[p]));
        }
    return str.join("&");
}


