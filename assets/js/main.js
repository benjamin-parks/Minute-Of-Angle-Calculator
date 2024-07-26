function calculateDrop(yards) {
    switch (yards) {
        case 25:
            return 0.25;
        case 50:
            return 0.5;
        case 100:
            return 0;
        case 200:
            return 4;
        case 300:
            return 15;
        case 400:
            return 32;
        case 500:
            return 60;
        default:
            return 0;
    }
}

yards = calculateDrop(500)
console.log(yards);

// calculate moa at yards 
function calculateMoa(yards) {
    return yards / 100;
}

// MOA adjustment = MOA 

console.log(calculateMoa(500));


// how many chunks of calculated MOA fit into yardage drops

function calculateAdjustment(moa, drop) {
    return drop / moa;
}

console.log(calculateAdjustment(5, 60));