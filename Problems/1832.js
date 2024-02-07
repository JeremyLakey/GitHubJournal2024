/**
 * @param {string} sentence
 * @return {boolean}
 */
const alpha = 'abcdefghijklmnopqrstuvwxyz'

var checkIfPangram = function(sentence) {
    let a = {}

    for (let i = 0; i < sentence.length; i++) {
        a[sentence[i]] = 1
    }

    //console.log(a)
    for (let i = 0; i < alpha.length; i++) {
        if (a[alpha[i]] == undefined) {
            return false;
        }
    }
    return true;
};