function soundex(word) {
    var codes = {
        A: '0', E: '0', H: '0', I: '0', O: '0', U: '0', W: '0', Y: '0',
        B: '1', F: '1', P: '1', V: '1',
        C: '2', G: '2', J: '2', K: '2', Q: '2', S: '2', X: '2', Z: '2',
        D: '3', T: '3',
        L: '4',
        M: '5', N: '5',
        R: '6'
    };
    function hasKey(obj, key) {
        return key in obj;
    }
    var normalizedWord = word.trim().toUpperCase().split('');
    var firstLetter = normalizedWord.shift();
    var result = firstLetter +
        normalizedWord
            .map(function (value) {
            if (hasKey(codes, value)) {
                return codes[value];
            }
        })
            .filter(function (value, index, array) {
            return value !== array[index - 1];
        })
            .filter(function (value) { return value !== '0'; })
            .join('');
    return (result + '000').slice(0, 4);
}
// For testing purpose
var community = "LaCommu";
document.body.textContent = soundex(community);
