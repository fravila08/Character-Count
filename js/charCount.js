exports.charCount = function(x) {
    string=x.replace(/\s/g, "")
    let splitStr=[...string]
    // console.log(splitStr)
    // console.log(string)
    myObject={}
    splitStr.forEach(function (x) {myObject[x] = ((myObject[x] || 0) + 1); });
    let unorder= myObject
    //console.log(JSON.stringify(unorder))
    const ordered=Object.keys(unorder).sort().reduce((obj, key)=>{
        obj[key]=myObject[key]
        return obj
    }, {})
    return ordered
};


// charCount("an apple a day will keep the doctor away")