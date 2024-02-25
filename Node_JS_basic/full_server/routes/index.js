const express = require('express');
const AppController = require('../controllers/AppController');
const StudnetController = require('../controllers/StudentController');

const router = express.Router();

router.get('/', AppController.getHomepage);

module.exports = router;
