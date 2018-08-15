const path = require('path');
const express = require('express');
const app = express();
app.use(express.json({ extended: true }));
const http = require('http').Server(app);
const port = process.env.PORT || 3000;
const api = require('./Routes/api');
const htmlPath = path.join(__dirname, 'Public');

app.use('/', express.static(htmlPath));

app.get('/status', api.getStatus, (req, res) => {
	res.json(res.item);
})

http.listen(port, () => {
  console.log(`Listening on ${port}`);
});