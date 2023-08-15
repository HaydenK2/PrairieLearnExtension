const init = function(){
  const injectElement = document.createElement('div');
  injectElement.className = 'injector';
  injectElement.innerHTML = 'TESTING CONTENT INJECTION';
  document.body.appendChild(injectElement);
}