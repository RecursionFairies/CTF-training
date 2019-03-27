var request = require("request");
const crypto = require('crypto');

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

passwd = generatePart1() + generatePart2();

var baseurl = "http://login1.uni.hctf.fun/?passwd=";
request(baseurl + passwd, function(error, response, result) {
  console.log(result);
});
