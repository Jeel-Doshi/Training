### Write a regular expression to search digits inside a string

Input : String

Output : Digits from string 

```sh
Input :

Hello..I am 21 years old. My bday is in 11th month. Also my fav number is 3 and I like to work in 2:2:2 pattern
```
```sh
Output :

['21', '11', '3', '2', '2', '2']
```

### Find the words with exactly 8 letters from a paragraph using regex


Input : Paragraph of string

Output : Words with exactly 8 letters

```sh
Input:

The phrase regular expressions, or regexes, is often used to mean the specific, standard textual syntax for representing patterns for matching text, as distinct from the mathematical notation described below. Each character in a regular expression (that is, each character in the string describing its pattern) is either a metacharacter, having a special meaning, or a regular character that has a literal meaning. For example, in the regex b., 'b' is a literal character that matches just 'b', while '.' is a metacharacter that matches every character except a newline
```

```sh
Output :

['specific', 'standard', 'patterns', 'matching', 'distinct', 'notation']
```

### Find the numbers starting with 212 from a string

Input : String

Output : Numbers starting with 212

```sh
Input:

212 Jeel-212Kite 21234 open0210
```

```sh
Output :

['212', '21234']
```

### Loop through the list and apply the regex to each element so that only items ending with a semicolon (;) are matched

Input : List

Output : Items ending with semicolon

```sh
Input:

['Ice cream;','Coffee','Shake;','Cocoa;','Fruit','Snow']
```

```sh
Output :

Ice cream;
Shake;
Cocoa;
```

### Write a regular expression to get only the part of the email before the "@" sign and include the "@" sign

Input : Email address

Output : Part of email with @ sign

```sh
Input:

movie.32@gmail.com
tome12@gmail.com
kite_fly@gmail.com
```

```sh
Output :

['movie.32@']
```

### Replace all special characters with space using regex

Input : String

Output : String with all special characters replaced with space 

```sh
Input:

Hello.. I am 21; years ^ old. My bday is $ in 11th month. Also % my fav number * is 3 and I like to work in 2:2:2 pattern
```

```sh
Output :

Hello   I am 21  years   old  My bday is   in 11th month  Also   my fav number   is 3 and I like to work in 2 2 2 pattern
```

### Replace the space character that occurs after a word ending with a or r with a newline character

Input : String

Output : String with space character replaced with new line character

```sh
Input:

area not an _a2_ roar took 22
```

```sh
Output :

 area 
not an _a2_ roar 
took 22
```

### Split the given input string on one or more repeated sequences of a cat using regex

Input : String

Output : Spiltted string from cat

```sh
Input:

firecatlioncatcatcatbearcatcatparrot
```

```sh
Output :

['fire', 'lion', 'bear', 'parrot']
```

### Filter all elements that contain a sequence of lowercase alphabets followed by - followed by digits. They can be optionally surrounded by {{ and }}. Any partial match shouldn't be part of the output.

Input : List of string

Output : Required string 

```sh
Input:

['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
```

```sh
Output :

['{{apple-150}}', 'grape-87']
```