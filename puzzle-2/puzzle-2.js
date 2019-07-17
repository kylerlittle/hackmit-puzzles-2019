
function walkTheDOM(node, func) {
    func(node);
    node = node.firstChild;
    while (node) {
        walkTheDOM(node, func);
        node = node.nextSibling;
    }
}

var solution = ""
walkTheDOM(document.body, function (node) {
    // if it's a text node
    if (node.nodeType === 3) {
        var text = node.data.trim();
        // if text is EXACTLY length 1, it's part of solution
        if (text.length === 1) {
            solution += text
        }
    }
});

console.log(solution)