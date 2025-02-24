## 200 DIGITS OF PI

This application exists to teach memorization with the major system through digits of pi, and an exploratory project to determine if Tkinter is a decent framework for building applications (it's not). 

### A primer on the Major System:

Humans have a consistent recall limit of six to seven numbers in working memory. This is so consistent that it's a regular test for cognitive decline or developmental delay. Numbers are very "fungible" in memory (e.g. misremembering a 5 as a 6 or turning a 3 into an 8), so it is better to translate numbers into something human brains are designed to handle; language. 

The common expectation is to translate a number into an "idea": instead of "3," you think "three musketeers," but this simply takes too long, still has fungibility, and is still tied to the number itself.

The Major System instead ties a number to (a) consonant sound and allowing those consonants to be used with vowels and semi-vowels to construct words, phrases, or familiar sounds that can be encoded and decoded quickly and consistently. 

| Digit |     Sound      |     Examples      |
| :---: | :------------: | :---------------: |
|   0   | S, Z, C (soft) |     Sea, Zero     |
|   1   |      T, D      | Tree, Door, Damp  |
|   2   |       N        | Net, Nail, Night  |
|   3   |       M        |     Moon, Man     |
|   4   |       R        | Ring, Rail, Road  |
|   5   |       L        | Lake, Lion, Load  |
|   6   | J SH CH(soft)  |  Jet, SHoe, CHip  |
|   7   |  K G CH(hard)  | King, Goat, CHaos |
|   8   |      F V       |   Finish, Value   |
|   9   |      B, P      |  Pin, Bowl, Boat  |

3.1415 → MTRTL → MOTOR OIL 
345 → MRL → "Moral"
This is a requirement for doing mental arithmetic at a reasonable speed, and as far as I'm aware - no decent tool exists to make learning this as frictionless as possible.

### How to use this application: 

Install dependencies - branch readme for setup instructions 
Run application.py

Place cursor in input field at the bottom left and type in numbers. 
Each 6th digit will automatically be checked for validity and inserted if valid, removed if not. 
Click the HINT button for the letter sounds, click HINT again for a full word/phrase. 
Click RETRY to clear history and start from 3.14.
Click RESET to completely restart the entire application (RESET is mostly for me to test code changes quickly because hot reload doesn't exist with tkinter or ctkinter, one of many problems)

Note on hints: hints present in this version were generated via OpenAI's 4.0 - past the first handful they have a variety of small errors in using consnants where they shouldn't to construct complete words. LLM's have more complete internal models of the written word, but the actual pronunciation or 'sound' is outside their understanding (which is obvious when you think about it, but might be an interesting benchmark/proxy for reasoning in LLMs). 

MVP (complete as of 02/06/2025 - ie branch):
- Load application 
	- load digits of pi
	- accept text input
	- progress in 6 digit chunks
	- hints for memorizing digits/Major System display

---

Made with python and customTinker - https://github.com/TomSchimansky/CustomTkinter
Font credit to [Daniel Linssen](https://daniellinssen.games) -  - https://managore.itch.io/m5x7

Feature list:
- Keybinds
- User input hints
- Profiles
	- menu select profiles to load
		- Load previous profile data
		- Log sessions 
		- Seralize/deserialize session data
		- Track stats ala Kovaaks
- skill decay 
- phone number memorizer 
- number > read passage of book > recall number
- timed stats for 200 digits of pi 

Nice to have:
- BladeRunner 2049 mode
- stats on failure/failure analysis
- chimp game versus battle royale (https://humanbenchmark.com/tests/chimp) 
- progress graph
- audio selection for success/failure sounds and weights and condition settings
- colored text & text animation
