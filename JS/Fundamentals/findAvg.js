// Write a function which calculates the average of the numbers in a given list.

// My Code - One Liner:
const findAvg = (array) => array.length ? (array.reduce((sum, num) => sum + num)) / array.length : 0;

// My Alt Code - Better Human Readability:
const findAverage = (array) => {
    if (array.length) {
        return (array.reduce((sum, num) => sum + num)) / array.length;
    }
    return 0;
}

// Best Practice:
// var find_average = (array) => {  
//     return array.length === 0 ? 0 : array.reduce((acc, ind)=> acc + ind, 0)/array.length
//   }