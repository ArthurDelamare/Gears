function soundex(word: string): string {

    const codes = {
        A: '0', E: '0', H: '0', I: '0', O: '0', U: '0', W: '0', Y: '0',
        B: '1', F: '1', P: '1', V: '1',
        C: '2', G: '2', J: '2', K: '2', Q: '2', S: '2', X: '2', Z: '2',
        D: '3', T: '3',
        L: '4',
        M: '5', N: '5',
        R: '6'
    };
    
    function hasKey<O>(obj: O, key: keyof any): key is keyof O {
        return key in obj
      }

    let normalizedWord = word.trim().toUpperCase().split('');
    const firstLetter = normalizedWord.shift();
    const result = firstLetter + 
    normalizedWord
    .map((value) => { 
        if (hasKey(codes, value)) {
            return codes[value] 
        }
    })
    .filter((value, index, array) => {
        return value !== array[index - 1];
    })
    .filter((value) => value !== '0')
    .join('');

    return (result + '000').slice(0, 4);
}

// For testing purpose
const community = "LaCommu";
document.body.textContent = soundex(community);