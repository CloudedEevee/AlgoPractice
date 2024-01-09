// Change values in array: pos to neg, and vice versa

// My Code:
function invert(array) {
    let invArr = [];
    for (let num in array ) {
      invArr.push(array[num] * -1);
    }
    return invArr;
}

// Best Practice:
// const invert = array => array.map(num => -num);