exports.charCount = function(x) {
    string=x.replace(/\s/g, "")
    let splitStr=[...string]
    // console.log(splitStr)
    // console.log(string)
    myObject={}
    splitStr.forEach(function (x) {myObject[x] = ((myObject[x] || 0) + 1); });
    return(myObject)
};

    