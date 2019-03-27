var http = require('http');
const crypto = require('crypto');
var url = require('url');
var fs = require('fs');

var _0x86d1=["\x68\x65\x78","\x72\x61\x6E\x64\x6F\x6D\x42\x79\x74\x65\x73"];

function generatePart1() {
    return
         {
             x: crypto[_0x86d1[1]](8)

         }[x].toString(_0x86d1[0]);
}
function generatePart2() {
    return [+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]];
}

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    passwd = generatePart1() + generatePart2();
    var url_content = url.parse(req.url, true);

    if (passwd == url_content.query.passwd) {
       res.write(fs.readFileSync('flag.txt', 'utf8'));
    } else {
        res.write('<html><body><form method="get"><input type="text" name="passwd" value="password"><input type="submit" value="login" /></form></body></html>');
    }
    res.end();
}).listen(8888);
