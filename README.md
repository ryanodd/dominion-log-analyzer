A python server for AWS, deployed as a `.zip`.

It consumes game logs for Dominion, and returns some stats.

1.

```
7z a -r deployment-package.zip *
```

2.

```
aws lambda update-function-code --function-name dominion-log-analyzer --zip-file fileb://deployment-package.zip
```
