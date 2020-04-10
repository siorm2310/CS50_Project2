let messageArea = document.getElementById("chat_area");
let sendMessageBtn = document.getElementById("send_message");
let messageBox = document.getElementById("msg_box");

function setMultipleAttributes(element, attributes) {
  for (let key in attributes) {
    element.setAttribute(key, attributes[key]);
  }
  return;
}

document.addEventListener("DOMContentLoaded", () => {
  // connection to server
  var socket = io.connect(
    location.protocol + "//" + document.domain + ":" + location.port
  );

  socket.on("connect", () => {
    document.getElementById("send_message").onclick = () => {
      let message = document.getElementById("msg_box");
      socket.emit("submit message", { message: message.value });
      message.value = null;
    };
  });
});
