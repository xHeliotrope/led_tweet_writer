require('dotenv').config()

const Twitter = require('twitter')
const express = require('express')
const app = express()
const http = require('http').Server(app)
const io = require('socket.io')(http)
const fs = require('fs')

let client = new Twitter({
    consumer_key: process.env.consumer_key,
    consumer_secret: process.env.consumer_secret,
    access_token_key: process.env.access_token_key,
    access_token_secret: process.env.access_token_secret
})


app.set('port', (process.env.PORT || 5000))

let tweet = "connecting..."

client.get('statuses/user_timeline', { screen_name: 'ChirpTheMsgMstr' }, (error, tweets, response) => {
        tweets = tweets.map((tweet) => { return tweet.text });
        if (!error) { 
	tweet = tweets[0];
        fs.writeFile("./examples/message.txt", tweet, function(err){
          if(err) {
            console.log(err)
          }
          console.log("wrote : " + tweet)
        })

 	}
});


let stream = client.stream('statuses/filter', {follow: '920299462282698752'}, stream => {
    stream.on('data', event => {
        let tweet = event
	if(tweet.delete) {
	    tweet.text = "the tweet has been discarded"
	}
	tweet = tweet.text
        fs.writeFile("./examples/message.txt", tweet, function(err){
          if(err) {
            console.log(err)
          }
          console.log("wrote : " + tweet)
        })
    })
})

io.on('connection', function(socket){
    socket.on('disconnect', function(){
      console.log('user disconnected');
    })
})

http.listen(app.get('port'), function() {
  console.log('Node app is running on port ', app.get('port'))
})


