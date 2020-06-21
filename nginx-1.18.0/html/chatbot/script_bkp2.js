

var messages = document.getElementById("messages")
var textbox = document.getElementById("textbox")
var button = document.getElementById("button")

button.addEventListener("click",function(){
    var newMessages = document.createComment("li")
    newMessages.innerHTML = textbox.value;
    alert(textbox.value)
    messages.appendChild(newMessages);
    textbox.value="";
    document.getElementById("messages").innerHTML = "Hello JavaScript!"
    document.getElementById("messages").appendChild(textbox.value)
});