var onoff = require('onoff');
var http = require("http");
var port = 8686;
var led_status= 0;

var led = new onoff.Gpio(18, 'out');

function randomInt (low, high) {
  return Math.floor(Math.random() * (high - low) + low);
}

http.createServer(function(req,res){
  console.log('New incoming client request for ' + req.url);
  res.writeHeader(200, {'Content-Type': 'application/json'});
  switch(req.url) {
    case '/led':
      //Return led status 
      res.write('{"led" :' + led_status + '}');
      break;
    case '/led/on':
      // Turn led on and return JSON
      led.write(1, function(){ console.log("Changed LED state to: 1"); });
      res.write('{"led" :' + 1 + '}');
      break;
    case '/led/off':
      // Turn led off and return JSON
      led.write(0, function(){ console.log("Changed LED state to: 0"); });
      res.write('{"led" :' + 0 + '}');
      break;
    default:
      res.write('{"hello" : "world"}');
  }
  res.end();
}).listen(port);
console.log('Server listening on http://localhost:' + port);


process.on('SIGINT', function () {
  led.writeSync(0);
  led.unexport();
  console.log('Shutting down server...');
  process.exit();
});
