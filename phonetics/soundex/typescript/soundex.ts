function soundex(word: string): string {
    let normalizedWord = word.trim().toUpperCase()
    let code = normalizedWord[0]
    return code;
}

const community = "Louistiti";

document.body.textContent = soundex(community);