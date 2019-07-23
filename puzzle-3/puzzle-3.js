const clues = [
    {
        hint: 'places',
        cells: [220, 41, 15, 26, 144],
        data: 'powdered sugar',
        cssColor: 'powderblue',
        dataLoc: 0 
    },
    {
        hint: '(buzzing stinger)x2',
        cells: [234, 192, 191, 117, 12, 238],
        data: 'blithe',
        cssColor: '#008BC3',
        dataLoc: 0 
    },
    {
        hint: 'disagreement on gCal',
        cells: [27, 107, 180, 199, 101, 140, 152, 185],
        data: 'blue glass',
        cssColor: '#a8ccd7',
        dataLoc: 0 
    },
    {
        hint: 'fashionably ruined',
        cells: [53, 131, 40, 71, 22, 209, 143, 215, 208, 235],
        data: 'heritage blue',
        cssColor: '#5a6569',
        dataLoc: 0 
    },
    {
        hint: 'boarding starts 45 minutes before this',
        cells: [155, 171, 206, 254, 67, 181, 43, 17, 9, 232, 93, 98, 156, 42, 255],
        data: 'mykonos blue',
        cssColor: '#4DADE8',
        dataLoc: 3
    },
    {
        hint: 'e.g. hominidae',
        cells: [124, 81, 95, 190, 154, 160],
        data: 'snorkel blue',
        cssColor: '#00537d',
        dataLoc: 0
    },
    {
        hint: 'somone who is Stayin\' Alive',
        cells: [133, 33, 48, 57, 16, 30],
        data: 'classic blue',
        cssColor: '#48689a',
        dataLoc: 3
    },
    {
        hint: '[giggle]',
        cells: [229, 18, 197, 46],
        data: 'lichen blue',
        cssColor: '4DADE8',
        dataLoc: 0
    },
    {
        hint: 'NA of NAMA',
        cells: [58, 60, 55, 231, 7, 146, 75, 188, 178, 169, 182, 68, 134, 66, 105],
        data: 'imperial blue',
        cssColor: '4DADE8',
        dataLoc: 6
    },
    {
        hint: 'screen a movie on a wall, say',
        cells: [62, 137, 24, 227, 63, 121, 216],
        data: 'silver lake blue',
        cssColor: '#5d89ba',
        dataLoc: 3
    },
    {
        hint: '2019 Astros HOF Joe\'s',
        cells: [91, 113, 242, 110, 196, 90, 61, 187, 106, 250, 184, 247, 59, 82, 87],
        data: 'surf the web',
        cssColor: '#01818c',
        dataLoc: 3
    },
    {
        hint: 'commute time of 25.5 minutes in the US',
        cells: [88, 119, 194, 23, 116, 84, 142, 166, 25, 86, 207, 151, 211, 200, 47] ,
        data: 'alaskan blue',
        cssColor: '#7d9dc3',
        dataLoc: 7
    },
    {
        hint: 'satisfied psychic',
        cells: [74, 94, 45, 236, 19, 34, 239, 230, 109, 201, 28],
        data: 'sodalite blue',
        cssColor: '#002366',
        dataLoc: 10
    },
    {
        hint: '\"back in my day\"',
        cells: [176, 92, 29, 51, 96, 4, 135, 83, 221, 170, 198, 118, 120, 108, 225],
        data: 'mediterranian blue',
        cssColor: '#218db1',
        dataLoc: 3
    },
    {
        hint: 'thing fed into 1881 duplicating machine',
        cells: [245, 186, 193, 0, 174, 99, 219, 77, 5, 89, 159, 212, 246, 240, 195],
        data: 'iced aqua',
        cssColor: '#E1E7E4',
        dataLoc: 4
    },
    {
        hint: 'pear tree dweller',
        cells: [210, 161, 50, 130, 36, 147, 102, 114, 241],
        data: 'petit four',
        cssColor: '#0072bb',
        dataLoc: 0
    },
    {
        hint: 'price estimate',
        cells: [153, 163, 70, 72, 224] ,
        data: 'little boy blue',
        cssColor: '#6ca0dc',
        dataLoc: 0
    },
    {
        hint: 'meteoric rise to celebrity',
        cells: [203, 141, 104, 54, 253, 162, 148, 85, 97, 100, 233, 78, 8, 165, 111],
        data: 'billowing sail',
        cssColor: '#A0C4E6',
        dataLoc: 0
    },
    {
        hint: 'reacts with acid',
        cells: [122, 158, 189, 64],
        data: 'crystal blue',
        cssColor: '#68a0b0',
        dataLoc: 2
    },
    {
        hint: 'many inches',
        cells: [112, 222, 3, 213],
        data: 'airy blue',
        cssColor: '#72a0c1',
        dataLoc: 3
    },
    {
        hint: 'grape snob',
        cells: [244, 44, 69, 243, 228, 73, 52, 56, 126, 218, 248, 128, 223, 172, 20],
        data: 'blue depths',
        cssColor: '#00006c',
        dataLoc: 13
    }, 
    {
        hint: 'netflix predecessor',
        cells: [65, 145, 138, 149, 226, 132, 79, 150, 237, 168, 173, 6, 39, 183, 164],
        data: 'azure blue',
        cssColor: '#0e4bef',
        dataLoc: 9
    }, 
    {
        hint: 'aptly named place to store clothes',
        cells: [11, 205, 136, 252, 167, 139, 214, 127, 251],
        data: 'malibu blue',
        cssColor: '#66AFE9',
        dataLoc: 0
    },
    {
        hint: 'Monomania, for psychology majors',
        cells: [202, 249, 31, 13, 115, 35, 175, 14],
        data: 'dresden blue',
        cssColor: '#6db4d7',
        dataLoc: 6
    },
    {
        hint: '\"uh-huh\"',
        cells: [49, 1, 129, 179],
        data: 'crystal seas',
        cssColor: '#006994',
        dataLoc: 0
    },
    {
        hint: 'womanizing type',
        cells: [217, 125, 32, 204, 10, 80, 38, 177, 21, 103, 37, 157, 123, 2, 76],
        data: 'aquarius',
        cssColor: '#7cbee2',
        dataLoc: 4
    },
]

var inputs = Array.from(document.getElementsByTagName("input"));
var theGrid = inputs.slice(0, 256);
var theWords = inputs.slice(256, 512);

/* Create color alphabet dictionary. */
const ALPHABET = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",");
const ALPHABET_DICT = {}

for (const [index, element] of clues.entries()) {
    ALPHABET_DICT[ALPHABET[index]] = element["cssColor"];
}

/** Iterate over grid and color things appropriately */
for (const [index, inputInGrid] of theGrid.entries()) {

    const inputText = inputInGrid.value;
    console.log(inputText);
    if (inputText != "") {
        theGrid[index].style.backgroundColor = ALPHABET_DICT[inputText];
    }
}