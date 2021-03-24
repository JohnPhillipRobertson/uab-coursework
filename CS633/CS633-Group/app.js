var express = require("express"),
http = require("http"),
app = express();

app.use(express.static(__dirname + "/templates"));
http.createServer(app).listen(3000);
console.log("Connection to the login screen has been established")
