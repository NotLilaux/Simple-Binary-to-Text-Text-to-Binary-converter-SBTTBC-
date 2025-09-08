# Simple Binary to Text Text to Binary converter SBTTBC
The Simple Binary to Text/Text to Binary converter (SBTTBC) is a program made in python, a very simple one that converts binary to text and vice versa with a few configurations that you can tweak. Do whatever you want with this. I don't care and I'm not responsible for it.
## The simple explanation, for anyone who wants to recreate or understand the spaghetti in the code
> [!NOTE]
> I will not get into the nitty-gritty in this section. Just the basic outline of the SBTTBC.

1. Asking for user's input
2. Looping until the user types Q
3. Checking which input the user typed (is it the first option or the second one or completely new spaghetti?
   - If it's the first one, we will firstly turn the string to integers, then bytes and then finally, `decode()` those bytes. Print it of course.
   - If it's the latter, we will convert it into ASCII first using the `ord()` function, then to binary.
   - If it's a completely different letter, we can print some stuff, then it loops back again to the start. (Make sure to ask for input from the user at the very bottom otherwise you will end up with an infinite loop)

> [!IMPORTANT]
> Major things are being left out for simplicity sake, including error handling.

## The slightly-complicated explanation, for the nerds
1. Importing the `re` module
   - A library typically used for [regular expressions](https://www.w3schools.com/python/python_regex.asp).
   - It's **built-in**. (like the `math` module) No pip or conda install required.
2. Same thing as before, asking for users input twice and looping until the user types Q. However:
   - Check if the input it 8 characters or more (because binary text is at the very least 8 characters of 0s and 1s. Don't worry, we will check if the numbers are actually 0s or 1s with the RE module later on)
   - Check if the input even exists. (It could be empty.)
3. After we check those 2 things, we will finally use the RE module and store the `list` that matches the pattern in a variable. (Or overwriting the original input.)
   - I recommend putting it in a variable. If 
## Another useful tool I used in this
- [Regex 101](https://regex101.com/) <--- a useful website for checking regular expressions in all progamming languages
