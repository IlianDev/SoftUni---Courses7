function previousDate(year, month, day) {
    const date = new Date(year, month, day)
    const resultDate = new Date();

    resultDate.setDate(date.getDate() - 1);
    console.log(resultDate);
}
previousDate(2016, 9, 30);
previousDate(2016, 10, 1)