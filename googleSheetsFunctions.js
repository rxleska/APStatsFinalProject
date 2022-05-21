
// This function takes in the rating and run time data as list as well as 2 data ranges to create the number of movies encapsulated in the ranges
// a and b are in format of [start,end)

function GetNumInRange(list1,list2,a,b) {  
    var count = 0;
    
    //Parse out the ranges starting and end points
    let rate = a.split(',')
    let run = b.split(',')
    var srate = parseFloat(rate[0].toString().substring(1))
    var erate = parseFloat(rate[1].toString().substring(0,rate[1].toString().length-1))
    var srun  = parseFloat(run[0].toString().substring(1))
    var erun  = parseFloat(run[1].toString().substring(0,run[1].toString().length-1))
  
    //counts values
    for(let i = 0; i < list1.length; i++){
      if(parseFloat(list1[i].toString()) >= srate && parseFloat(list1[i].toString()) < erate && parseFloat(list2[i].toString()) >= srun && parseFloat(list2[i].toString()) < erun){
        count++;
      }
    }
    
    return count
  
  }
  