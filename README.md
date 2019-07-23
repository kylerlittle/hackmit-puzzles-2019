# hackmit-puzzles-2019

## Description
Share code for the puzzles.

## Usage
If starting puzzle \#N, make it in a directory called ```puzzle-$N```

## Solution Descriptions
### Puzzle 1: Hulk SMASH
Initially, we thought we had to write up an auto-clicking bot. However, after checking the Javascript, it seemed clear that we could solve this without that. After toying around with the code, we realized that the line ```fillPosition(parseInt(locSpl[0]), parseInt(locSpl[1]), hex);``` would "break down" a pixel of the wall. In fact, this was being called several times in a loop... why was there a loop? We logged the output of the response to the endpoint ```/u/${username_and_hash}/${x}/${y}``` and learned that a very long list was returned rather than a single coordinate. The API call returns a list of hex values and coordinates to which those hex values correspond. And the loop was simply looping over each coordinate/HEX returned. But somehow not all calls to ```fillPosition``` were resulting in breaking down a pixel of the wall. Only the first call to the function was successful in the loop due to the boolean flag. So we just hacked together a quick script that called the API at a few dispersed keypoints in the image (12 to be exact) and remove the boolean flag. After running it, the wall was broken down :-)

### Puzzle 2: I LOVE IRONMAN
After perusing the website for a bit, we noticed an area at the bottom of the webpage which says "You are not authorized to access this area. Your browser can't handle it." We looked at the HTML and discovered that most of the transcript for IronMan was embedded within a ```<div style="display:none">``` HTML tag. It was completely out of order and contained much duplication. Eventually, we noticed that there was a single character randomly placed throughout this tag. "Duh." The hint all of the sudden made sense:

> "Honestly if we could just untangle the internal workings we can find small bits of information
> Like one character words?"

Wrote up a quick recursive traversal of the DOM using preorder traversal (thanks Google!) and outputted only lines where a single character existed and concatenated them into a string. The solution magically appeared :-)

### Puzzle 3: Acrostic
Who doesn't love a good crossword? This one was quite fun. A true puzzle. We thought the solution here would be fairly obvious. Fill out the crossword and one obvious word would appear, GET request that endpoint, get our solutions, and be done... Turns out finding that one obvious word proved more tricky then we thought. The first thing we noticed was that in each of the puzzle answers, there was a single letter that was bolded. After solving a few, we quickly realized that it would be the alphabet from top to bottom. That was useful for helping us come up with the correct answers... but eventually we were stuck again. We noticed the very conspicuous ```data.js``` file, but we couldn't exactly figured out why it would be useful. We tried many different things, finally noticing that the grid appeared to be roughly symmetric across the vertical axis by letters. We thought potentially a design would appear. So we thought to color each letter in the grid with the corresponding data color from the file (i.e. all letter As would be colored with ```clues[0]['data']```, Bs with ```clues[1]['data']```, etc. This finally looked like something... after a few seconds, we realized it was the arc reactor from Iron Man's suit. Ironically, we had guessed ```arc_reactor``` as an endpoint earlier when we had low morale and resorted to blind guessing. The actual endpoint was ```arcreactor```. I guess it feels good to solve the puzzle correctly... but damn we could have used some of those hours for the other puzzles ¯\_(ツ)_/¯

### Puzzle 4: The Infinity Phones
This puzzle was frustrating because of how simple the solution ended up being and how long we spent on it... We immediately thought to decode the tones at the beginning of each recording into their musical notes. One of our group members is a Music Major, so he had software to do this already. He gave us the notes for each recording probably within 5 minutes of starting this puzzle. There was a lot of second guessing as to whether this was the right strategy, if we needed to decode the tones into DTMF and then into dial tones, if we needed to analyze the spectrograms, and what did Idaho have to do with anything? We all agreed that the recordings needed to be translated into phone numbers since each recording was exactly 10 digits, but we weren't sure how the phone numbers would be used or how to translate the recordings into phone numbers. We finally noticed that each of the locations had a distinct zip code (yes the whole state of Idaho is 208 -- three of our group members our from there) and these three zip codes shared no common digits. Each of the first three notes of the recordings were completely unique from each other as well. We found our cipher :-) We tried using an online T9 simulator to see if the phone numbers would be translated into text. Eventually, we thought we may as well call the phone numbers. There was no way they actually set something up to where we'd have to call somebody, right? Wrong. Thanks Idaho Geology Department.

### Puzzle 5: Shards Puzzle

### Puzzle 6: Training/Test Set Partition
