document.addEventListener('DOMContentLoaded', () => {
    // connection to server
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on("connect",() => {});

});




