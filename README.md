# flask-convert-base64-to-photo

# Parameters

It is a POST call

    pic1base64 : base64 format of uploaded image 1
    
    pic1ID : id of pic 1
    
    pic2base64 : base64 format of uploaded image 2
    
    pic2ID : id of pic 2

## How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
