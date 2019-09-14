# OUCS4263-SoftBearEngineering RNG Project
Random number generator practice project for taking requirements.

## Authors
- Hope Anderson
- Bryant Hall
- Blake Gerard
- Cory White
- Tim Gehrsitz

## GCP with Python Guide - Blake Gerard
1. Download the files in the "GCP_Python" directory to your local machine.
2. Within your selected GCP Project, go to the App Engine dashboard and start a new service.
3. Navigate to the "Storage >> Browser" in GCP and select the App Engine service created in step 2.
4. Upload the three files from step 1 to the new project's bucket using the "Upload files" button.
5. Now that the files are stored in the project bucket, open a GCloud Shell.
6. Change directories into your preferred directory to store the files.
6. Run the command `gsutil -m cp -R gs://BUCKETNAME ./GCLOUDFOLDERNAME`, where
 * BUCKETNAME is the name of the bucket found in the Storage browser.
 * GCLOUDFOLDERNAME will create a new directory to store the files downloaded from the bucket.
7. Change directories into the GCloud Folder created in step 6.
8. Run `gcloud app deploy` and enter Y to confirm. Run `gcloud app browse` and click the link to view the random number.


## GCP with Java Guide - Bryant Hall
1.	Load up a new project in GCP
2.	Go to App Engine Dashboard
3.	Click start tutorial and select Java.
4.	Run through the tutorial and deploy the tutorial application
5.	Open Shell (ensure you are in directory appengine-try-java) and launch code editor (pencil icon at the top of the cloud shell console) for the tutorial app
6.	Enter the DemoServlet.java file by following the directory path of `appengine-try-java/src/main/java/myapp/demoserverlet.java`
7.	Within the doGet() function type:
 `int randomNumber = (int)(Math.random() * 1000000);`
8. Remove:
`resp.getWriter().println("{ \"value\": \"World\"}");`
8.	Replace with:
<pre><code>
PrintWriter out = resp.getWriter();
out.printf("{ \"value\": \"%d\"}", randomNumber);
</code></pre>
9.	Navigate to index.html in the directory path `appengine-try-java/src/main/webapp/index.html` and delete the line 
`$('#result').html("Hello, " + data.name);`
and replace with
`$('#result').html(data.value);`
10.	Return to Bash shell and type:
`gcloud config set project \ <YOUR-PROJECT-ID>`
(YOUR PROJECT-ID CAN BE FOUND AT GCP HOME DASHBOARD)
`mvn appengine:deploy`

## VM with Python Guide - Cory White
(In this we presume there is not VM already made so there may be steps that can be skipped)
1.	Go to GCP and go to the compute engine
2.	Go to vm instances and create a new machine
3.	For our purpose I just used a g1-small
4.	Allow https and https traffic and click create
5.	Once that is finished creating go back to your VM instance list and open up the ssh to the newly created VM
6.	Run the following commands:
 * `sudo apt-get update` , `sudo apt-get install python-pip`
 * Now we clone the directory and cd into VM_Python. Run `source env/bin/activate` we are now in the virtualenvironment
 *	Run `pip install flask` just to be sure flask is installed on the machine
7.	Run the "server.py" file using `sudo python server.py'
If you installed and set everything up correctly, you should recieve a message similar to:

<pre><code>
Serving Flask app "server" (lazy loading) 
* Environment: production WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. 
*Debug mode: off * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
</code></pre>

8. To connect to the server you will use your vms external ip but we need to use http to connect, not https, so the url for example would be http://11.111.11.11/. The random number will appear in the top left corner of the page.

Our working version of the site accessable to anyone.  http://34.69.126.180/  if there are any issues during the setup process, this link should show we have infact made a working version of the site as requested.

## VM with Java Guide - Tim Gehrsitz

## Tests - Hope Anderson
To runs tests from terminal within directory containing test file, type 
```bash
python3 test_servers.py
```
