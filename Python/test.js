function plusMinus(arr) {
    // Write your code here
  const size = arr.length
  
  const { 
    positiveValuesCount,
    negativeValuesCount,
    zeroValuesCount
  } = arr.reduce((output, current) => { 
    if (current > 0) {
      return { 
        ...output, 
        positiveValuesCount: output.positiveValuesCount + 1
      }
    }
    if (current < 0) {
      return {
        ...output, 
        negativeValuesCount: output.negativeValuesCount  + 1
      }
    }
    return {
      ...output, 
      zeroValuesCount: output.zeroValuesCount + 1
    }
  }, { positiveValuesCount: 0, negativeValuesCount: 0, zeroValuesCount: 0 })
  
  console.log(positiveValuesCount / size)
  console.log(negativeValuesCount / size)
  console.log(zeroValuesCount / size)
}