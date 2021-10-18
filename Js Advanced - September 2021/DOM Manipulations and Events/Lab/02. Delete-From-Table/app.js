  // select input field and real value
  // get tbody children
  // repeat for every row
  // select second row
  // if textContent matches input value -> remove row 
  // if there is a match print "delete"
  // otherwise print "not found"

  function deleteByEmail() {
      const input = document.querySelector('input[name="email"]');
      const rows = Array.from(document.querySelector('tbody').children);

      let removed = false;
      for (let row of rows) {
          if (row.children[1].textContent == input.value) {
              row.remove();
              removed = true;
          }
      }
      if (removed) {
          document.getElementById("result").textContent = 'Deleted.';
      }else{
          document.getElementById("result").textContent = 'Not found.';
      }
  }
