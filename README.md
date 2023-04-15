# SERVERLESS API DEPLOYMENT WITH AWS LAMBDA

[![Pylint CI](https://github.com/lornamariak/aws-serverless/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/lornamariak/aws-serverless/actions/workflows/pylint.yml)

In this project, I used Fast API to read data from an external source then used AWS API Gateway to trigger AWS lambda to export the results of my query to an S3 bucket. 

This application can be used to automate the process of reading data from external APIs to internal data sources.

## Architecture

![](workflowdiagram.png)

## Technologies used

- AWS API GATEWAY
- AWS LAMBDA
- AWS S3
- FAST API

## To use
`run make install`

`run make build`
