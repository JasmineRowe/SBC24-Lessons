// TODO: Add 2 new items to the sidebar called "Register" and "Help".


var sideBarEl = document.querySelector("ul");

var newSideBarEl = document.createElement("li");
newSideBarEl.textContent= "Register";


sideBarEl.appendChild(newSideBarEl);



// TODO: MEGA CHALLENGE: can you add the Help link between Reports and Settings?


var newSideBar2El = document.createElement("li");
newSideBar2El.textContent= "Help";

sideBarEl.insertBefore(newSideBar2El, sideBarEl.children[6]);
