# 200 DIGITS OF PI

This application exists to teach memorization with the major system through digits of pi, and was an exploratory project to determine if Tkinter is a decent framework for building applications (it's not, I'm swapping to raylib and C/C++).

### A Primer on Math Memorization:

Humans have a recall limit of six or seven numbers in working memory. This limit is so consistent that it functions as a test for cognitive decline or developmental delay. Numbers are very "fungible" in memory (e.g. misremembering a 5 as a 6 or turning a 3 into an 8), so for numbers to be memorized they must be directly transcoded into something more compatible with a human brain: language.  

The typical expectation is to translate a number into an "idea": instead of "3," you think "three musketeers," but this simply takes too long, has the same fungibility issues outside of the most obvious cases, and is still tied to the number itself.

The Major System ties a number to consonant sounds and allows those consonants to be used with vowels and semi-vowels to construct words, phrases, or familiar sounds that can be encoded and decoded quickly and consistently. It is a very literal transcoding.

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

#### 3.1415 → MTRTL → MOTOR OIL 

345 → MRL → MORAL

This is a requirement for memorizing your mom's credit card to buy Runescape membership (just checking if you're awake) or doing mental arithmetic at a reasonable speed, and as far as I'm aware - no tool exists to make learning this extremely boring material as frictionless as possible.

---

## How to Run This Application: 

Install dependencies - see [previous README](https://github.com/Astramentis/TerminalCommands/blob/Interview-Publish/README.md) for setup instructions and run ```python3 application.py```

1. Place cursor in input field at the bottom left and enter numbers with keypad or number row. 

2. Each 6th digit will automatically be checked for validity and inserted if valid, removed if not. 

3. Click the HINT button for the letter sounds, click HINT again for a full word/phrase. (hints mostly missing outside the first few)

4. Click RETRY to clear history and start from 3.14.

4a. Open the practice mode and practice specific consonant and number combinations as required.

_Click RESET to completely restart the entire application_

_(RESET was mostly for me to test code quickly because hot reload doesn't exist with tkinter or ctkinter; one of MANY problems)_

**IMPORTANT WARNING ON HINTS**: the hints present in this version were generated via an LLM (exploratory project). LLMs have more complete models of the written language, but the actual pronunciation or 'sound' for mapping is mostly outside their reasoning capabilities (obvious when you think about it, and in the future may be an interesting benchmark/proxy for reasoning in LLMs). 

**MVP (complete as of 02/06/2025)**:

- Load application & display digits: 
	- load digits of pi
	- accept text input
	- progress in 6 digit chunks with a check for correct/incorrect with feedback audio
	- hints for memorizing digits/Major System display*
  	- saves metrics on user inputs and time for tracking/feedback
  	- modifiable practice mode (hardcoded)

---

Future Features:
- Keybinds
- User input bindings
- Profiles
	- menu select profiles to load
		- Load previous profile data
		- Log sessions 
		- Serialize/deserialize session data for uploading
- Skill decay 
- Phone number memorizer 
- Number > read passage of book > recall number to further test mid-long term memorization

Wacky Ideas:
- Blade Runner 2049 mode (see https://youtu.be/ZRcpnM26nJM?t=23)
- Battle Royale mode (https://humanbenchmark.com/tests/chimp)


## Credits:
Made with Python and [cTkinter](https://github.com/TomSchimansky/CustomTkinter) 

[Font](https://managore.itch.io/m5x7) credit to [Daniel Linssen](https://daniellinssen.games)