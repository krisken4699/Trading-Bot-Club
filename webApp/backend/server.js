//Lib
const express = require('express');
const path = require("path");
const cors = require("cors");
const fs = require('fs');
const bodyParser = require('body-parser');

//Create App
const app = express();

//set up
app.set('port', (process.env.PORT || 4040))
// app.set('trust proxy', true);
app.set('trust proxy', function (ip) {
    // console.log(`${IP}` + ip);
    return true;
});
app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.use(express.urlencoded({ extended: false }))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json());
app.use(express.json({ extended: false }));


// app.use(cors({origin:'localhost:8000'}));
app.use(express.static('../../webApp/frontend/public'));

app.use(function (req, res) {
    console.log('Cannot find ', req.url)
    res.status(404);
});

app.listen(app.get('port'), function () {
    // console.log("Running : 3001\n192.168.10.19:3001");
    require('dns').lookup(require('os').hostname(), function (err, add, fam) {
        console.log("Running : 3001\t\t\t\thttp://" + add + ":3001\t\t\thttps://pangcu.herokuapp.com");
    })
});
process.on('uncaughtException', function (err) {
    // console.log('Small Error. Chill');
});
process.on('uncaughtRejection', function (err) {
    // console.log('Small Error. Chill');
});
process.on('warning', function (err) {
    // console.log('Small Error. Chill');
});
process.on('unhandledRejection', function (reason, promise) {
    // console.log('Small Error. Chill');
});