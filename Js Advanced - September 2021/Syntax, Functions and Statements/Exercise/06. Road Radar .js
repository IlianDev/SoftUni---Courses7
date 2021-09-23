function speedRestrinction(speed, area) {
    let motorway = 130;
    let interstate = 90;
    let city = 50;
    let residential = 20;

    let difference = 0
    let speedZone = 0;
    let overlimit = "";


    switch (area) {
        case "motorway":
            speedZone = motorway
            break;

        case "interstate":
            speedZone = interstate;
            break;

        case "city":
            speedZone = city;
            break;

        case "residential":
            speedZone = residential;
            break;
    }
    if (speed > speedZone) {
        difference = speed - speedZone;
    }
    if (difference != 0) {
        if (difference <= 20) {
            overlimit = "speeding";
        } else if (difference <= 40) {
            overlimit = "excessive speeding";
        } else {
            overlimit = "reckless driving"
        }
        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedZone} - ${overlimit}`)
    } else {
        console.log(`Driving ${speed} km/h in a ${speedZone} zone`)
    }
}

speedRestrinction(21, 'residential')