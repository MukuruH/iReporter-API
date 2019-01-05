# iReporter-API #

[![Build Status](https://travis-ci.com/MukuruH/iReporter-API.svg?branch=tests_branch)](https://travis-ci.com/MukuruH/iReporter-API) [![Coverage Status](https://coveralls.io/repos/github/MukuruH/iReporter-API/badge.svg)](https://coveralls.io/github/MukuruH/iReporter-API) [![Maintainability](https://api.codeclimate.com/v1/badges/a4126b08926933948681/maintainability)](https://codeclimate.com/github/MukuruH/iReporter-API/maintainability)



Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

##About##
- Create a ​ red-flag​​ record
- Get all ​ red-flag​​ records
- Get a specific ​ red-flag​​ record
- Edit a specific ​ red-flag​​ record
- Delete a ​ red-flag​​ record


### API Endpoints

HTTP Method|Endpoint|Functionality
-----------|--------|-------------
POST|api/v1/red-flags|Create an incident
GET|api/v1/red-flags/id|Fetch a specific incident
GET|api/v1/red-flags|Fetch all incidents
PATCH|api/v1/red-flags/id/[key]|Edit specific information on an end point
DELETE|api/v1/red-flags/id|Delete an incident

## Running Tests
tests are carried out in a virtual environment with pytest module


## Built with
*Python

## Author
* **Mukuru Harold** - *Initial work* - [MukuruH]
(https://github.com/MukuruH)
