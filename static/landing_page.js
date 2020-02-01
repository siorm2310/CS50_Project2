document.addEventListener('DOMContentLoaded', () => { //perform upon loading
    // connection to server
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on("connect",() => {});// TODO: complete or discard

    document.querySelector('#nickname_form').onsubmit = () => {
        // add comparison to user list in server side
        let selectedNickname = document.querySelector('#inputNickname').value;
        socket.emit('nickname requested' , {'nickname' :selectedNickname});
    }
});



