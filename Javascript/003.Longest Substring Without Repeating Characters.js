
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s == null&& s.length == 0){
        return 0;
    }

    var map = {};
    var len = 0;
    var maxlen = len;
    var start = 0;
    for (var i = start;i < s.length;i++){
        c = s[i];
        if (map[c] != undefined&&map[c] >= start){
            start = map[c] + 1;
            len = i - start;
        }

        len++;

        if (len < maxlen){
            maxlen = len;
        }

        map[c] = i;
    }
    return maxlen;
};