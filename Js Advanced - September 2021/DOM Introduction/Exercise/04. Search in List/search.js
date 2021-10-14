function search() {
    let matches = 0;
    let toSearch = document.getElementById('searchText').value;
    Array.from(document.getElementById('towns').children)
        .forEach(town => {
            if (town.textContent.includes(toSearch)) {
                town.style.fontWeight = 'bold';
                town.style.textDecoration = 'underline';
                matches++;
      }else{
         town.style.fontWeight = 'normal';
         town.style.textdecoration = 'underline';
      }
   })
   document.getElementById('result').textContent = `${matches} matches found`;
}