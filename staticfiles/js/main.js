'use strict';

// (A) PREVENT CONTEXT MENU FROM OPENING
document.addEventListener("contextmenu", (elem) => {
  elem.preventDefault();
}, false);

// (B) PREVENT CLIPBOARD COPYING
document.addEventListener("copy", (elem) => {
  // (B1) CHANGE THE COPIED TEXT IF YOU WANT
  elem.clipboardData.setData("text/plain", "Copying is not allowed on this webpage");
  // (B2) PREVENT THE DEFAULT COPY ACTION
  elem.preventDefault();
}, false);


$(document).bind('keydown', 'ctrl+u', function(elem) {
	elem.preventDefault();
    return false;
},false);

