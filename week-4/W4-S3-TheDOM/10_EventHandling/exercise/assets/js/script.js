// 1. use document.getElementById to select the searchTerm Button


var searchTermEl = document.getElementById("searchTerm");


// 2. use document.getElementById to select the searchButton Button

var searchButtonEl = document.getElementById("searchButton");


// 3. add an event listener to the searchButton that calls the search function when clicked

searchButtonEl.addEventListener("click", function () {

  // 4. use the value property of the searchInput to get the search term

  const searchTermVal = searchTermEl.value;


  // 5. select the searches div using document.getElementById

  const RecentSearchesEl = document.getElementById("searches");

  // 6. create a new li element using document.createElement

  const newSearchEl = document.createElement("li");


  // 7. set the innerHTML of the new paragraph to the search term

  newSearchEl.innerHTML = searchTermVal;
 
  // 8. append the new paragraph to the searches div

  RecentSearchesEl.appendChild(newSearchEl);

 
})



