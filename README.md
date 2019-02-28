### Invoke Algorithmia functions from AWS Lambda

`lambda_function.py` is an AWS Lambda (λ) function that calls a function in Algorithmia. The Algorithmia function takes a number, rounds it down and returns the result. As this lambda function has an external dependency it has to be deployed as zip in AWS Lambda. These instructions assume that you have already created an AWS Lambda function. Take a look at [this](https://blog.runscope.com/posts/how-to-write-your-first-aws-lambda-function) blog, if you would like to set up your first λ.

#### Create λ function package

This gives you intsructions to create a zip file which includes `lamba_function.py` & its dependencies. You can read [this](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) page to get more information on package & deployment

1. Clone this repository in your working directory

2. Open `lambda_function.py` & paste in your algorithmia clinet key on the following line:  
`algorithmia_client_key = #Insert your client key as a string`

3. Navigate to `algorithmia_lambda` directory

4. We need to add Algorthmia as a package  
`algorithmia_lambda$ mkdir package`  
`algorithmia_lambda$ cd package`  

5. Install libraries in package directory  
`algorithmia_lambda/package$ pip install Algorithmia --target .`

6. Create package zip  
`algorithmia_lambda/package$ zip -r9 ../function.zip .`

5. Add function code  
`algorithmia_lambda/package$ cd ../`  
`algorithmia_lambda$ zip -g function.zip lambda_function.py`

You should now have a zip file that includes Algorithmia libraries and the λ function.

#### Deploy λ Package to AWS

You can deploy your newly created package using aws lambda cli or you can upload it via UI. 

Navigate to the λ function in the AWS console. In the Function code section, select "Upload a .zip file", select Runtime as "Python 3.7" & upload the zip file and click Save.

![Upload Lambda Function](/content/images/uploadlambdafunction.png "Upload lambda function in AWS console")

Once the function is uploaded successuly, you should see the function and the packages listed in the Environment area. Run the test and you will see in the Execution Result section that the algorithm will get called and round the number in the script.

![Uploaded Lambda Function](/content/images/uploaded.png "Uploaded lambda function")

You can deploy the function using following code via the aws cli. This assumes that you have a already created a function named `algorithmia_lambda`

```~/algorithmia_lambda$ aws lambda update-function-code --function-name algorithmia_lambda --zip-file fileb://function.zip```