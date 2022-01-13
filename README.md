# LeeLee

LeeLee is an assistant that allows you to:

- Read you the `highlighted text` you selected
- Translate & Read the `highlighted text` you selected
- Save your `highlighted text` into a Knowledge Base folder
- Detect and translate your voice sentences

## Installation & startup

```dos
git clone https://github.com/SinJK/LeeLee  
cd .\LeeLee\LeeLee\
pip install -r requirements.txt
python main.py
```

## How it works ?

### Read Highlighted text
Press **alt+q** and `highlight` the desired text, you should then hear LeeLee reading your text.



https://user-images.githubusercontent.com/24277344/149414986-7dcdd382-9ab0-44f2-a2f9-5c9ed9cbfbc9.mp4



### Translate Highlighted text

Press **alt+t** and `highlight` the desired text, you should then hear LeeLee reading your text in your desired language (In french in the example).  


https://user-images.githubusercontent.com/24277344/149415022-1ad67009-dd35-40c0-9a8c-00c51809b8ae.mp4




### Save your Highlighted text

Press **alt+s** and a pop-up window will appear with 2 parameters:
- Name: Name of the file
- URL(Not mandatory): If the text is issued from a website, you can add the link to the top of the file
Once done, you can press **alt+m** to open the folder with your new and saved files with their highlighted text in it.







### Speak and get a translation
Press **alt+s** and speak clearly to get your sentence translated, you should then hear LeeLee reading your translated sentence.
Here the language detected are **Spanish/English/French** and the translation goes like following:

- English to French
- Spansih to French
- French to Spanish

Of course you can chose the language you want/need.

### How to quit
You just have to press **ctrl+p** to exit the script.
