const server = require('http').createServer()
const ioServer = require('socket.io')(server)
let ioClient = require('socket.io-client')
const url = 'https://scorebot-lb.hltv.org'
const id = "2366383"
let listeners = {}
let socket = ioClient.connect(url, {
    agent: false
})
var initObject = JSON.stringify({
    token: '',
    listId: id
})
var reconnected = false;
socket.on('connect', function () {
    var done = function () { return socket.close(); };
    if (!reconnected) {
      socket.emit('readyForMatch', initObject);
    }
    socket.on('scoreboard', function (data) {
      Object.entries(listeners).forEach(l => {
        l[1].emit('scoreboard', data)
      });
    });
    socket.on('log', function (data) {
      console.log('update')
      Object.entries(listeners).forEach(l => {
        l[1].emit('log', data)
      });
    });
});
socket.on('reconnect', function () {
    reconnected = true;
    socket.emit('readyForMatch', initObject);
});
socket.on('disconnect', function () {
    console.log("Bye")
});


var interval = 0
ioServer.on('connection', client => {
  listeners[client.id] = client
  client.on('event', data => {
    console.log('Sent me something ? Dont care.')
  })
  client.on('disconnect', () => {
    console.log('bye')
    delete listeners[client.id]
  })
})
server.listen(8080, () => console.log('ready'))
