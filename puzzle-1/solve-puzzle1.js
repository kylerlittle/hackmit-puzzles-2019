// change the <username_hash> bit in the URL to whatever yours says in the URL

for (var x = 0; x < 400; x += 50) {
    for (var y = 0; y < 300; y += 50) {
  fetch(`/u/kylerlittle_c5f5ee/${x}/${y}`)
      .then(function(response) {
        if (response.status === 429) {
          return null;
        }
        if (response.status !== 200) {
          return null;
        }
        return response.text();
      }).then(function(text) {
        if (text == null) {
          return;
        }
        var lines = text.split("\n");
        for (var ind = 0; ind < lines.length; ind += 1) {
  
          var line = lines[ind].split(",");
          var locSpl = line[0].split("_");
          var hex = line[1];
          if (hex.length !== 7) {
            continue;
          }
  
          // Set Temp Storage for CACHE
            fillPosition(parseInt(locSpl[0]), parseInt(locSpl[1]), hex);
        }
      });
    }
  }