# Simple Binary to Text Text to Binary converter SBTTBC
The Simple Binary to Text/Text to Binary converter (SBTTBC) is a program made in python, a very simple one that converts binary to text and vice versa with a few configurations that you can tweak. Do whatever you want with this. I don't care and I'm not responsible for it.
## The simple explanation, for anyone who wants to recreate or understand the spaghetti in the code
> [!NOTE]
> I will not get into the nitty-gritty in this section. Just the basic outline of the SBTTBC.



1. Asking for user's input
2. Looping until the user types Q
3. Checking which input the user typed (is it the first option or the second one or completely new spaghetti?
   3.1 If it's the first one, we will firstly turn the string to integers, then bytes and then finally, decode() those bytes. Print it of course.
   3.2 If it's the latter, we will convert it into ASCII first using the ord() function, then to binary.

> [!IMPORTANT]
> Major things are being left out for simplicity sake, including error handling.
## Another useful tool I used in this
[Regex 101](https://regex101.com/) <--- a useful website for checking regular expressions in all progamming languages
