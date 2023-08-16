var io = require('socket.io-client')
var printers = require('./printers')
const url = 'https://scorebot-lb.hltv.org'
const id = process.argv[2]
var socket = io.connect(url, {
    agent: false
});
var initObject = JSON.stringify({
    token: '',
    listId: id
});
var reconnected = false;
socket.on('connect', function () {
    var done = function () { return socket.close(); };
    if (!reconnected) {
        socket.emit('readyForMatch', initObject);
    }
    socket.on('scoreboard', function (data) {
         printers.onScore(data)
    });
    socket.on('log', function (data) {
	let event = JSON.parse(data).log.slice(-1)[0]
        let type = Object.keys(event)[0]
	switch(type){
	  case "Kill":
            printers.onKill(event.Kill)
            break
          case "BombPlanted":
            printers.onBombPlant(event.BombPlanted)
            break
          case "RoundStart":
            printers.onRoundStart()
            break
          case "RoundEnd":
            printers.onRoundEnd(event.RoundEnd)
            break
          case "Assist":
            printers.onAssist(event.Assist)
            break
          case "BombDefused":
            printers.onDefuse(event.BombDefused)
            break
	  case "PlayerQuit":
          case "PlayerJoin": break
          default:printers.default(event)
	}
    });
});
socket.on('reconnect', function () {
    reconnected = true;
    socket.emit('readyForMatch', initObject);
});
socket.on('disconnect', function () {
    console.log("Bye")
});
