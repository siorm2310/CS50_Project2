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

  socket.on("add messages", (newMessage) => {
    const template = `
    <div class="card">
    <div class="card-body">
      <h5 class="card-title">${newMessage["author"]} says:</h5>
      ${newMessage["body"]}
    </div>
    <p class="card-text">
      <small class="text-muted">from ${newMessage["time_stamp"]}</small>
    </p>
    </div>
    `;

    document.getElementById("chat_area").innerHTML += template;
  });
});
