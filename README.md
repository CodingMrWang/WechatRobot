# WechatRobot

Let's create a wechat robot to auto reply some intelligent words when you are busy.

Firstly, install itchat package

```
sudo pip install itchat
```

# Create a Tuling Robot

Go to [Tuling Offical Website](http://www.tuling123.com/).

Set up an account and login in. Then you can create your own robot, select the character you want the robot be and set the age and name. 
After that, enter the robot and get your Api key.
![Api key](https://ws3.sinaimg.cn/large/006tNc79ly1ftfh0xtfegj317s11qtct.jpg)
Also, get your user id on the top right corner.

Replace Api key and user id in the code:

```python
 data = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": msg
        },
        "inputImage": {
            "url": "imageUrl"
        },
    },
    "userInfo": {
        "apiKey": "yourapikey",
        "userId": "youruserid"
    }
}
```
Finally, run

```
python path/to/WecharRobot.py
```

It will pop up a QR code, scan the code, 10 seconds later, your robot will start work.

This is a sample, it is really intelligent, if you want a more intelligent one, you can upgrade your robot. 
This robot can also help you search all questions like weather, time and so on.

![Sample](https://ws4.sinaimg.cn/large/006tNc79ly1ftfh9w5oe2j30u01hcn0u.jpg)
