from PIL import Image
import numpy

NUM_SHARDS = 760
SHARD_WIDTH = 50
SHARD_HEIGHT = 200

COLOR_IMAGES = []
for i in range(NUM_SHARDS):
    COLOR_IMAGES.append(numpy.asarray(Image.open("shard-"+str(i)+".png")))

ALL_IMAGE_IDS = set(range(NUM_SHARDS))


# Could try using median differences, average difference, or some other metric
def getSimilarityVertical(bottom, top):
    dissim = 0
    for x in range(SHARD_WIDTH):
        for k in range(3):
            # Get the minimum difference of the bottom pixels to its adjacent upper three pixels
            left_pix = int(top[SHARD_HEIGHT-1, max(x-1,0), k])
            mid_pix = int(top[SHARD_HEIGHT-1, x, k])
            right_pix = int(top[SHARD_HEIGHT-1, min(x+1, SHARD_WIDTH-1), k])

            pix = int(bottom[0, x, k])
            dissim += min(100, min(abs(left_pix - pix), abs(mid_pix - pix), abs(right_pix - pix)))
    return dissim * (SHARD_HEIGHT / SHARD_WIDTH) # make vertical and horizontal similarities comparable

def getSimilarityHorizontal(left, right):
    dissim = 0
    for y in range(SHARD_HEIGHT):
        for k in range(3):
            # Get the minimum difference of the right pixels to its left adjacent three pixels
            left_pix = int(left[max(y-1,0), SHARD_WIDTH-1, k])
            mid_pix = int(left[y, SHARD_WIDTH-1, k])
            right_pix = int(left[min(y+1, SHARD_HEIGHT-1), SHARD_WIDTH-1, k])

            pix = int(right[y, 0, k])
            dissim += min(100, min(abs(left_pix - pix), abs(mid_pix - pix), abs(right_pix - pix)))
    return dissim


def getBestScoreAbove(image_id, remaining):
    dissimilarities = []
    for i in remaining:
        if i != image_id:
            dissimilarities.append((i, getSimilarityVertical(COLOR_IMAGES[image_id], COLOR_IMAGES[i])))

    return min(dissimilarities, key= lambda tup : tup[1])

def getBestScoreBelow(image_id, remaining, rank=0):
    dissimilarities = []
    for i in remaining:
        if i != image_id:
            dissimilarities.append((i, getSimilarityVertical(COLOR_IMAGES[i], COLOR_IMAGES[image_id])))
    
    return min(dissimilarities, key= lambda tup : tup[1])


def getBestScoreRight(image_id, remaining, rank=0):
    dissimilarities = []
    for i in remaining:
        if i != image_id:
            dissimilarities.append((i, getSimilarityHorizontal(COLOR_IMAGES[image_id], COLOR_IMAGES[i])))
    
    return min(dissimilarities, key= lambda tup : tup[1])

def getBestScoreLeft(image_id, remaining, rank=0):
    dissimilarities = []
    for i in remaining:
        if i != image_id:
            dissimilarities.append((i, getSimilarityHorizontal(COLOR_IMAGES[i], COLOR_IMAGES[image_id])))
    
    return min(dissimilarities, key= lambda tup : tup[1])



class Cell:
    NUM_OTHER_CELLS = 4
    ABOVE = 0
    BELOW = 1
    RIGHT = 2
    LEFT = 3
    BEST_FUNCTIONS = (getBestScoreAbove, getBestScoreBelow, getBestScoreRight, getBestScoreLeft)

    LOC_TO_STR = {
        ABOVE: "ABOVE",
        BELOW: "BELOW",
        RIGHT: "RIGHT",
        LEFT: "LEFT"
    }

    @classmethod
    def getXOffset(cls, loc):
        return {cls.ABOVE: 0,
            cls.BELOW: 0,
            cls.LEFT: -1,
            cls.RIGHT: 1}[loc]
    
    @classmethod
    def getYOffset(cls, loc):
        return {cls.ABOVE: -1,
            cls.BELOW: 1,
            cls.LEFT: 0,
            cls.RIGHT: 0}[loc]

    @classmethod
    def reverseLoc(cls, loc):
        return {cls.LEFT: cls.RIGHT,
            cls.RIGHT: cls.LEFT,
            cls.ABOVE: cls.BELOW,
            cls.BELOW: cls.ABOVE}[loc]

    def __init__(self, image_id, x=0, y=0):
        self.image_id = image_id
        self.x = x
        self.y = y
        self.otherCells = [None] * self.NUM_OTHER_CELLS
        self.bests = [(None, None) for _ in range(self.NUM_OTHER_CELLS)]

    
    def computeCandidates(self, remaining_image_ids):
        for cell in self.getAllCells():
            for loc in range(Cell.NUM_OTHER_CELLS):
                if cell.bests[loc][0] not in remaining_image_ids and cell.otherCells[loc] is None:
                    cell.bests[loc] = Cell.BEST_FUNCTIONS[loc](cell.image_id, remaining_image_ids)
                if cell.bests[loc][0] is None:
                    raise RuntimeError("Bad Chunk state")

    def getBestScore(self):

        min_score = float('inf')
        for loc in range(self.NUM_OTHER_CELLS):
            if self.otherCells[loc] is None and self.bests[loc][1] < min_score:
                min_score = self.bests[loc][1]
        return min_score

    def fillInBestCandidate(self, remaining):
        bestCell = sorted(self.getAllCells(), key=lambda cell: cell.getBestScore())[0]

        bestScore = bestCell.getBestScore()
        bestLoc = list(map(lambda tup : tup[1], bestCell.bests)).index(bestScore)

        newCell = Cell(bestCell.bests[bestLoc][0], bestCell.x+Cell.getXOffset(bestLoc), bestCell.y+Cell.getYOffset(bestLoc))
        print("Best Candidate is", newCell.image_id, Cell.LOC_TO_STR[bestLoc], bestCell.image_id, "Score: ", bestScore)

        for cell in list(self.getAllCells()):
            cell.placeIfAdjacent(newCell)

        remaining.remove(newCell.image_id)

    def placeIfAdjacent(self, cell):
        xoffset = cell.x - self.x
        yoffset = cell.y - self.y

        for loc in range(self.NUM_OTHER_CELLS):
            if Cell.getXOffset(loc) == xoffset and Cell.getYOffset(loc) == yoffset and self.otherCells[loc] is None:
                print("Placing", cell.image_id, Cell.LOC_TO_STR[loc], self.image_id)
                self.otherCells[loc] = cell
                self.bests[loc] = (-1, -1)
                cell.otherCells[Cell.reverseLoc(loc)] = self
                cell.bests[Cell.reverseLoc(loc)] = (-1, -1)
                return # Can only be adjacent in one direction

    def getAllCells(self, checked=None):
        if checked is None:
            checked = set()

        if self in checked:
            return
        else:
            checked.add(self)
            yield self

            for loc in range(self.NUM_OTHER_CELLS):
                if self.otherCells[loc] is not None:
                    yield from self.otherCells[loc].getAllCells(checked)

    def createImage(self, _id=0):
        allCells = list(self.getAllCells())
        minX = min(allCells, key=lambda cell : cell.x).x
        minY = min(allCells, key=lambda cell : cell.y).y
        maxX = max(allCells, key=lambda cell : cell.x).x
        maxY = max(allCells, key=lambda cell : cell.y).y

        xWidth = (maxX-minX)+1
        yWidth = (maxY-minY)+1

        pixels = numpy.zeros((yWidth*SHARD_HEIGHT, xWidth*SHARD_WIDTH, 3), dtype=numpy.uint8)
        for cell in allCells:
            yStart = (cell.y-minY)*SHARD_HEIGHT
            xStart = (cell.x-minX)*SHARD_WIDTH
            pixels[yStart:yStart+SHARD_HEIGHT, xStart:xStart+SHARD_WIDTH,:] = COLOR_IMAGES[cell.image_id][:,:,:]

        
        file_name = "patched_image"+str(_id)+".png"
        print("saving image to: ", file_name)
        Image.fromarray(pixels).save(file_name)
            



remaining = set(range(NUM_SHARDS))
FIRST = 474
remaining.remove(FIRST)
chunk = Cell(FIRST)
for i in range(NUM_SHARDS-1):
    chunk.computeCandidates(remaining)
    chunk.fillInBestCandidate(remaining)
    if i % 20 == 0:
        chunk.createImage(i)
chunk.createImage("done")
