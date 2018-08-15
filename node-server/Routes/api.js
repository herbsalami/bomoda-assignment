const express = require('express');
const router = express.Router();
router.use(express.json({ extended: true }));
const fetch = require('node-fetch');
require('dotenv').config();

const getStatus = (req, res, next) => {
	fetch(`${process.env.BASE_URL}/status`)
		.then(res => res.json())
		.then((json) => {
			res.item = json;
			next();
		})
}

module.exports = {
	getStatus
}