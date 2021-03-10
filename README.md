# SQS Lambda Example

## How To Run It
1. Install node.js LTS version & dependencies:

1.1. Install or check npm (npm -v) 

1.2. Install Serverless:

```
npm install -g serverless
```

> If there is an error with "node<10.00", first run:
> `apt-get install nodejs:i386`

2. Set your AWS credentials:
```
export AWS_ACCESS_KEY_ID=<your_key_id_here>
```
```
export AWS_SECRET_ACCESS_KEY=<your_secret_key_here>
```

3. Run with:
```
sls deploy
```

4. Run sendMessageSQS lambda from AWS Console and see doTask logs in Cloudwatch.

