let student = {
    firstName: 'Maria', 
    lastNamw: 'Lopez',
    age: 22,
    location: {
        coordinates:{ lat: 43, lng: 23},
        locationName: 'Rim',
    }
}
const {location: {coordinates}} = student;
console.log(coordinates);