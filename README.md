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
Who doesn't love a good crossword? This one was quite fun. A true puzzle. We thought the solution here would be fairly obvious. Fill out the crossword and one obvious word would appear, GET request that endpoint, get our solutions, and be done... Turns out finding that one obvious word proved more tricky then we thought. The first thing we noticed was that in each of the puzzle answers, there was a single letter that was bolded. After solving a few, we quickly realized that it would be the alphabet from top to bottom. That was useful for helping us come up with the correct answers... but eventually we were stuck again. We noticed the very conspicuous ```data.js``` file, but we couldn't exactly figured out why it would be useful. We tried many different things, finally noticing that the grid appeared to be roughly symmetric across the vertical axis by letters. We thought potentially a design would appear. So we thought to color each letter in the grid with the corresponding data color from the file (i.e. all letter As would be colored with ```clues[0]['data']```, Bs with ```clues[1]['data']```, etc. This finally looked like something... after a few seconds, we realized it was the arc reactor from Iron Man's suit. Ironically, we had guessed ```arc_reactor``` as an endpoint earlier when we had low morale and resorted to blind guessing. The actual endpoint was ```arcreactor```. I guess it feels good to solve the puzzle correctly... but damn we could have used some of those hours for the other puzzles ¯\\_(ツ)_/¯

### Puzzle 4: The Infinity Phones
This puzzle was frustrating because of how simple the solution ended up being and how long we spent on it... We immediately thought to decode the tones at the beginning of each recording into their musical notes. One of our group members is a Music Major, so he had software to do this already. He gave us the notes for each recording probably within 5 minutes of starting this puzzle. There was a lot of second guessing as to whether this was the right strategy, if we needed to decode the tones into DTMF and then into dial tones, if we needed to analyze the spectrograms, and what did Idaho have to do with anything? We all agreed that the recordings needed to be translated into phone numbers since each recording was exactly 10 digits, but we weren't sure how the phone numbers would be used or how to translate the recordings into phone numbers. We finally noticed that each of the locations had a distinct zip code (yes the whole state of Idaho is 208 -- three of our group members our from there) and these three zip codes shared no common digits. Each of the first three notes of the recordings were completely unique from each other as well. We found our cipher :-) We tried using an online T9 simulator to see if the phone numbers would be translated into text. Eventually, we thought we may as well call the phone numbers. There was no way they actually set something up to where we'd have to call somebody, right? Wrong. Thanks Idaho Geology Department.

### Puzzle 5: Shards Puzzle
This was a puzzle in the most accurate sense of the word. We were presented with 760 50x200 images in a random order. Our job: piece the images back together to form the original image. Some puzzlers apparently printed out all of the images, cut them out, and then actually solved it like a normal puzzle. We like coding, so we implemented a puzzle solving algorithm. The idea was fairly simple, but took much care to get right. Our algorithm from a high-level viewpoint looked something like this:
```
for each shard:
  compute the most likely top, bottom, left, and right neighbors of the shard
  chunk together the two most promising candidates
```
Check out the [code](puzzle-5/shards.py) for some of the nitty gritty details.

The final stiched image looked like:
[people smiling with puzzle solution over top](/img/puzzle5.JPG)

### Puzzle 6: Training/Test Set Partition
This one was quite a fun challenge. The puzzle:
[puzzle 6 hackmit](/img/puzzle6.png)
Essentially, the task was to reverse engineer a neural net. In other words, figure out which inputs were from the training set (e.g. the set that producted the model in the first place) and which inputs were from the test set. For every image input, you were given the prediction vector for the given CIFAR image (i.e. a vector where the index is the predicted class and the value is the model's predicted probability of the input being from that class). Based on this, we were to determine whether an image helped create the neural net. Not much to go off of...

Challenge #1 was simply scraping the data from the website. The defined API took approximately 2.3 seconds to retrieve a single data point. We needed 1,000 data points at the very minimum, which is around 40 minutes of work. This is extremely slow, so we wrote a [parallelized scraper](puzzle-6/parallel_scraper.py) to get data at a much faster rate. RIP server bandwidth.

Onto solving the puzzle... our first idea was that perhaps they overfitted their model. In this case, all training data points would have an extremely high prediction probability (e.g. a probability of 1 for a single class). However, filtering to just a list of 1000 of these data points and submitting these object IDs gave us the following message:
> Accuracy between 70% and 85%

We needed an accuracy of 85% or higher. Since the dataset was a public dataset [(the CIFAR 100 dataset)](https://www.cs.toronto.edu/~kriz/cifar.html), we thought perhaps the puzzle was really simple. If the data point was from the CIFAR 100 training data set, then it was probably from the researchers training set, too, right?
> Accuracy between 70% and 85%

Next idea: what about filtering to images that were predicted correctly (i.e. highest prediction probability class is the same as the label from the public dataset)?
> Accuracy between 70% and 85%

What about the combination?
> Accuracy between 70% and 85%

What about filtering to data with lower prediction probabilities or within some arbitrary range?
> Accuracy between 70% and 85%
or
> Accuracy between 55% and 70%
or
> Accuracy below 50%

This puzzle was hard. Finally we came up with an idea that we knew would work. We were going to produce a contrived solution set that would report either "Accuracy below 50%" or "Accuracy between 55% and 70%" by changing only a single object ID in the set. If the accuracy improved by adding this one item, we knew it had to be a part of the original training data set, and so add it to our actual final submission. Creating that solution set was non-trivial, but involved using an algorithm similar to binary search. The small catch with this approach is that you were only allowed to submit a potential solution every 5 minutes. We bypassed this by submitting our requests from a randomly hashed URL. We further increased speed by parallelizing this. Sorry to whoever was trying to use the website at this time ¯\\_(ツ)_/¯ Did we mention that our parallel scraper was still running? Oops.

While this code was running, we went to Safeway to purchase some ice cream. It was 1 AM. Fun times. We came back, submitted our solution set, and finished the puzzles!
